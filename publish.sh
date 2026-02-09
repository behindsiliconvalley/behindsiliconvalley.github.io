#!/bin/bash
# Publish Behind Silicon Valley site updates
cd /Users/haniagarcia/Documents/behindsilliconvalley

echo "📡 Publishing behindsiliconvalley.com..."
echo ""
read -p "What did you change? " msg

git add .
git commit -m "${msg:-Site update $(date '+%b %d %H:%M')}"
git push

echo ""
echo "✅ Done! Site will be live in 1-2 minutes."
echo "🔗 https://behindsiliconvalley.com"
