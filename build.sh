#!/bin/bash
# Build script for updating static files from Zola markdown source
# Run this script whenever you update content in zola-site/

set -e  # Exit on any error

echo "🔄 Building Zola site from markdown source..."
cd zola-site

# Ensure static assets are current
echo "📁 Copying static assets..."
cp -r ../css static/ 2>/dev/null || true
cp -r ../images static/ 2>/dev/null || true

# Build the site
echo "🏗️  Building with Zola..."
zola build

echo "📋 Copying generated files to root..."
cd ..

# Copy all generated files except CNAME and other special files
cp zola-site/public/index.html .
cp -r zola-site/public/css . 2>/dev/null || true
cp -r zola-site/public/images . 2>/dev/null || true

echo "✅ Static files updated from markdown source!"
echo ""
echo "📝 Content source: zola-site/content/_index.md"
echo "🎨 Template source: zola-site/templates/index.html"
echo "⚙️  Config source: zola-site/config.toml"
echo ""
echo "Next steps:"
echo "  git add ."
echo "  git commit -m 'Update content from markdown source'"
echo "  git push origin master"