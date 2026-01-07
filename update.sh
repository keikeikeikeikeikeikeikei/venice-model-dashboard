#!/bin/bash
set -e

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🚀 Starting Venice Pricing Update..."

# 1. Fetch ALL data
echo "📥 Fetching and consolidating data..."
uv run python scripts/fetch.py

# 2. Generate Dashboard
echo "📊 Generating Main Dashboard..."
uv run python scripts/build.py

# 3. Take Screenshot
echo "📸 Updating Screenshot..."
uv run python scripts/take_screenshot.py

echo "✅ Update Complete! Open docs/index.html to view."
