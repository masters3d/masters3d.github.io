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

# Copy all generated HTML files
cp zola-site/public/index.html .
cp zola-site/public/tech/index.html tech.html 2>/dev/null || echo "⚠️  Tech page not generated"
cp zola-site/public/media/index.html media.html 2>/dev/null || echo "⚠️  Media page not generated"

# Copy static assets
cp -r zola-site/public/css . 2>/dev/null || true
cp -r zola-site/public/images . 2>/dev/null || true

echo "✅ All pages updated from markdown source!"
echo ""
echo "📝 Content sources:"
echo "  - Main page: zola-site/content/_index.md"
echo "  - Tech page: zola-site/content/tech/_index.md"
echo "  - Media page: zola-site/content/media/_index.md"
echo ""
echo "🎨 Template sources:"
echo "  - Main template: zola-site/templates/index.html"
echo "  - Tech template: zola-site/templates/tech.html"
echo "  - Media template: zola-site/templates/media.html"
echo ""
echo "⚙️  Config source: zola-site/config.toml"
echo ""
echo "Next steps:"
echo "  git add ."
echo "  git commit -m 'Update content from markdown source'"
echo "  git push origin master"