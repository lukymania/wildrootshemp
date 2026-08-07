#!/bin/bash
# Wild Roots Hemp Deploy Script
# Usage: ./deploy.sh YOUR_GITHUB_PAT_TOKEN

set -e

if [ -z "$1" ]; then
    echo "Usage: ./deploy.sh YOUR_GITHUB_PAT_TOKEN"
    echo ""
    echo "To create a GitHub PAT token:"
    echo "1. Go to https://github.com/settings/tokens"
    echo "2. Click 'Generate new token (classic)'"
    echo "3. Check the 'repo' scope"
    echo "4. Generate and copy the token"
    exit 1
fi

TOKEN="$1"
REPO="https://$TOKEN@github.com/lukymania/wildrootshemp.git"

echo "Setting up remote with authentication..."
git remote remove origin 2>/dev/null || true
git remote add origin "$REPO"

echo "Pushing to GitHub Pages..."
git push -u origin main --force

echo ""
echo "============================================"
echo "Deploy complete! Site will be live shortly:"
echo "  https://wildrootshemp.com"
echo ""
echo "If this is your first push, enable Pages:"
echo "  https://github.com/lukymania/wildrootshemp/settings/pages"
echo "  Set source to 'Deploy from a branch' -> 'main' -> '/' (root)"
echo "============================================"
