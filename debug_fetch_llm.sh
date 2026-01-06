#!/bin/bash
set -e

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🐞 DEBUG MODE: Starting Venice Pricing Update (LLM Only)..."

# 1. Fetch ONLY Text data (Fast, preserves video data)
echo "📥 Fetching TEXT models only (skipping video quotes)..."
uv run python scripts/fetch.py --type text

# 2. Generate Dashboard
echo "📊 Regenerating Dashboard..."
uv run python scripts/build.py

echo "✅ Debug Update Complete! Open docs/index.html to view."
