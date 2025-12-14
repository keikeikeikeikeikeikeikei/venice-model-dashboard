#!/bin/bash
set -e

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🚀 Starting Venice Pricing Update..."

# 1. Fetch latest data
echo "📥 Fetching latest data from Venice API..."
python3 fetch_venice_pricing.py

# 2. Fetch video pricing
echo "💰 Fetching video model pricing..."
python3 fetch_video_pricing.py

# 3. Merge data for dashboard
python3 merge_dashboard_data.py

# 4. Generate HTML files
echo "⚙️ Generating HTML model lists..."
python3 generate_model_list.py
python3 generate_image_model_list.py
python3 generate_video_model_list.py

echo "📊 Generating Main Dashboard..."
python3 generate_dashboard.py

echo "✅ All data updated successfully!"
