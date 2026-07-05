#!/usr/bin/env bash
#
# check-unmerged-branches.sh
#
# Go through every remote branch and report whether it still carries content
# changes that have NOT been merged into the target branch (default: master).
#
# This is squash-merge aware: it does not rely on commit ancestry or commit
# counts (which are misleading when PRs are squash-merged). Instead it performs
# an in-memory trial merge of each branch into the target and checks whether the
# resulting tree differs from the target tree. If the tree is identical, the
# branch's content is already in the target even if its commits are not.
#
# Usage:
#   scripts/check-unmerged-branches.sh [target-branch] [remote]
#
# Examples:
#   scripts/check-unmerged-branches.sh              # compare against origin/master
#   scripts/check-unmerged-branches.sh main         # compare against origin/main
#   scripts/check-unmerged-branches.sh master upstream
#
# Exit status:
#   0  no unmerged branches found
#   1  one or more branches still have unmerged content
#   2  usage / setup error

set -u

TARGET_BRANCH="${1:-master}"
REMOTE="${2:-origin}"
TARGET_REF="${REMOTE}/${TARGET_BRANCH}"

if ! git rev-parse --git-dir >/dev/null 2>&1; then
    echo "error: not inside a git repository" >&2
    exit 2
fi

# Make sure we have every remote branch and full history locally. A shallow
# clone or a stale remote-tracking set would give wrong answers (branches would
# look like "unrelated histories" because their common ancestor is cut off).
if [ "$(git rev-parse --is-shallow-repository 2>/dev/null)" = "true" ]; then
    git fetch --quiet --unshallow "${REMOTE}" 2>/dev/null
fi
git fetch --quiet "${REMOTE}" "refs/heads/*:refs/remotes/${REMOTE}/*" 2>/dev/null

if ! git rev-parse --verify --quiet "${TARGET_REF}^{commit}" >/dev/null; then
    echo "error: target branch '${TARGET_REF}' not found" >&2
    exit 2
fi

target_tree="$(git rev-parse "${TARGET_REF}^{tree}")"

unmerged_clean=()   # branches that would merge cleanly and add content
unmerged_conflict=() # branches with unmerged content that conflicts with target
unmerged_unrelated=() # branches with unrelated histories (cannot auto-merge)
merged=()           # branches whose content is already in the target

while IFS= read -r ref; do
    branch="${ref#"${REMOTE}"/}"

    # Skip the target itself and any symbolic HEAD pointer.
    [ "${branch}" = "${TARGET_BRANCH}" ] && continue
    [ "${branch}" = "HEAD" ] && continue

    # Fast path: branch is an ancestor of target => fully merged.
    if git merge-base --is-ancestor "${ref}" "${TARGET_REF}" 2>/dev/null; then
        merged+=("${branch}")
        continue
    fi

    # Trial-merge the branch into the target without touching the working tree.
    merge_out="$(git merge-tree --write-tree "${TARGET_REF}" "${ref}" 2>/dev/null)"
    merge_rc=$?
    new_tree="$(printf '%s\n' "${merge_out}" | head -1)"

    if [ -z "${new_tree}" ]; then
        # merge-tree produced no tree (e.g. unrelated histories); can't be
        # merged normally, but it is definitely not merged into the target.
        unmerged_unrelated+=("${branch}")
    elif [ "${new_tree}" = "${target_tree}" ]; then
        # Merging changes nothing => content already present in target.
        merged+=("${branch}")
    elif [ ${merge_rc} -ne 0 ]; then
        unmerged_conflict+=("${branch}")
    else
        unmerged_clean+=("${branch}")
    fi
done < <(git for-each-ref --format='%(refname:short)' "refs/remotes/${REMOTE}")

print_list() {
    local title="$1"; shift
    printf '\n%s (%d)\n' "${title}" "$#"
    if [ "$#" -eq 0 ]; then
        printf '  (none)\n'
        return
    fi
    for b in "$@"; do
        printf '  - %s\n' "${b}"
    done
}

echo "Comparing all '${REMOTE}' branches against '${TARGET_REF}'"

print_list "UNMERGED - clean (would merge into ${TARGET_BRANCH} without conflicts)" ${unmerged_clean[@]+"${unmerged_clean[@]}"}
print_list "UNMERGED - conflicts (has content not in ${TARGET_BRANCH}, needs conflict resolution)" ${unmerged_conflict[@]+"${unmerged_conflict[@]}"}
print_list "UNMERGED - unrelated history (cannot auto-merge; e.g. gh-pages)" ${unmerged_unrelated[@]+"${unmerged_unrelated[@]}"}
print_list "Already merged (content already in ${TARGET_BRANCH}; safe to delete)" ${merged[@]+"${merged[@]}"}

total_unmerged=$(( ${#unmerged_clean[@]} + ${#unmerged_conflict[@]} + ${#unmerged_unrelated[@]} ))
printf '\nSummary: %d unmerged, %d already merged.\n' "${total_unmerged}" "${#merged[@]}"

[ "${total_unmerged}" -eq 0 ] && exit 0 || exit 1
