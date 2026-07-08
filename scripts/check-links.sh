#!/usr/bin/env bash
#
# check-links.sh
#
# Wrapper around `zola check` that keeps CI green when the only problem is that
# an external site could not be reached (network error, timeout, rate-limiting,
# or a temporary server outage), while STILL failing on links that are actually
# broken (404/Client errors, missing anchors, unparseable URLs, and any
# template/content/internal-link error).
#
# Rationale: `zola check` always crawls every external link and exits non-zero
# on ANY failure. That makes the scheduled/PR link check flaky, because it turns
# a transient "couldn't reach the server" into a hard failure. We only want to
# fail the build for links that are genuinely wrong, and merely warn when we
# were unable to reach the target.
#
# Usage:
#   scripts/check-links.sh [zola-site-dir]
#
#   zola-site-dir   Directory containing config.toml (default: the "zola-site"
#                   folder next to this script's repository root).
#
# Environment:
#   LINK_CHECK_STRICT=1   Treat every zola check failure as fatal (restore the
#                         default `zola check` behaviour, no tolerance).
#
# Exit status:
#   0  no problems, or the only problems were unreachable/transient links
#   1  at least one genuinely broken link (or other check error) was found
#   2  usage / setup error

set -u

# Resolve the Zola site directory. Default to <repo-root>/zola-site so the
# script works no matter the current working directory.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_DIR="${1:-${SCRIPT_DIR}/../zola-site}"

if [ ! -f "${SITE_DIR}/config.toml" ]; then
    echo "error: no config.toml found in '${SITE_DIR}'" >&2
    exit 2
fi

if ! command -v zola >/dev/null 2>&1; then
    echo "error: 'zola' is not installed or not on PATH" >&2
    exit 2
fi

echo "Running 'zola check' in ${SITE_DIR} ..."

# Capture combined output so we can both show it and classify the failures.
output="$(cd "${SITE_DIR}" && zola check 2>&1)"
status=$?

# Always surface the raw zola output in the logs.
printf '%s\n' "${output}"

if [ "${status}" -eq 0 ]; then
    echo "✓ zola check passed — all links valid"
    exit 0
fi

# Strict mode: opt out of the tolerance behaviour entirely.
if [ "${LINK_CHECK_STRICT:-0}" = "1" ]; then
    echo "✗ zola check failed (LINK_CHECK_STRICT=1 — no tolerance applied)" >&2
    exit 1
fi

# zola formats each broken link / anchor error as a numbered list item:
#   "  1. Broken link in <file> to <url>: <message>"
#   "  2. The anchor in the link `@/...` in <file> does not exist."
#   "  3. could not parse domain `<url>` from link: `...`"
# Pull out just those numbered problem lines for classification.
problem_lines="$(printf '%s\n' "${output}" | grep -E '^[[:space:]]*[0-9]+\.[[:space:]]')"

if [ -z "${problem_lines}" ]; then
    # Non-zero exit but no recognisable broken-link list: this is some other
    # failure (template error, build/content error, panic, ...). Fail hard.
    echo "✗ zola check failed with an error that is not a link-reachability issue" >&2
    exit 1
fi

# Classify each problem line. A line is "tolerable" only when it indicates we
# could not reach the target (network/DNS/timeout/connection errors), the
# server rate-limited us (429), or the server returned a transient 5xx.
# Everything else (4xx client errors, missing anchors, unparseable URLs,
# internal link errors) is a genuine problem and must fail the build.
real_failures=""
tolerated=""

# Case-insensitive patterns that mean "we could not reach the target".
unreachable_re='error sending request|timed out|timeout|connection (refused|reset|closed|error)|dns error|failed to lookup|name resolution|could not resolve|tcp connect|network is unreachable|no route to host|handshake|broken pipe|connect error'
# Transient HTTP responses: rate-limiting and server-side errors.
transient_re='\(429|too many requests|server error status code'

while IFS= read -r line; do
    [ -z "${line}" ] && continue
    if printf '%s' "${line}" | grep -qiE "${unreachable_re}"; then
        tolerated+="${line}"$'\n'
    elif printf '%s' "${line}" | grep -qiE "${transient_re}"; then
        tolerated+="${line}"$'\n'
    else
        real_failures+="${line}"$'\n'
    fi
done <<< "${problem_lines}"

if [ -n "${tolerated}" ]; then
    echo ""
    echo "::warning::Some external links could not be reached (treated as transient, not failing the build):"
    printf '%s' "${tolerated}"
fi

if [ -n "${real_failures}" ]; then
    echo ""
    echo "✗ Found genuinely broken link(s) that must be fixed:" >&2
    printf '%s' "${real_failures}" >&2
    exit 1
fi

echo ""
echo "✓ No genuinely broken links — only unreachable/transient failures, which are tolerated."
exit 0
