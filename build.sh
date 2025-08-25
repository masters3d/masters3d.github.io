#!/bin/bash
# Build script for updating static files
# Run this script whenever you update content in zola-site/

echo "🔄 Building Zola site..."
cd zola-site
zola build

echo "📋 Copying static files to root..."
cd ..
cp -r zola-site/public/* .

echo "✅ Static files updated! Ready to commit and push."
echo ""
echo "Next steps:"
echo "  git add ."
echo "  git commit -m 'Update static content'"
echo "  git push origin master"