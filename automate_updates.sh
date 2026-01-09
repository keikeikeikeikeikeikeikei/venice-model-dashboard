#!/bin/bash

# Configuration
# Get the directory where this script is located
BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LOG_FILE="$BASE_DIR/automation_log.txt"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Ensure uv is in PATH (Launchd has limited PATH)
export PATH="/Users/namunakasadara/.local/bin:$PATH"

# Function to log with timestamp
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Clear previous stderr/stdout logs to avoid mixing old errors
: > "$BASE_DIR/automation_stdout.log"
: > "$BASE_DIR/automation_stderr.log"

echo "------------------------------------------" >> "$LOG_FILE"
log "🚀 Starting Automation Update"

# Function to process a repository
process_repo() {
    local repo_path=$1
    local repo_name=$2
    local data_file=$3
    local ignore_keys=$4
    
    log "Processing $repo_name..."
    cd "$repo_path" || { log "❌ Failed to enter $repo_path"; return; }
    
    # 1. Store current data if it exists
    if [[ -f "$data_file" ]]; then
        cp "$data_file" "${data_file}.old"
    fi
    
    # 2. Run ONLY the fetch step
    log "  📥 Fetching latest data..."
    uv run python scripts/fetch.py >> "$LOG_FILE" 2>&1
    
    # 3. Compare data
    local changed=0
    local diff_summary=""
    if [[ -f "${data_file}.old" ]]; then
        # Use our comparison script and capture its output
        local ignore_args=""
        if [[ -n "$ignore_keys" ]]; then
            ignore_args="--ignore $ignore_keys"
        fi
        diff_summary=$(python3 "$BASE_DIR/scripts/compare_json.py" "$data_file" "${data_file}.old" $ignore_args)
        if [[ $? -eq 1 ]]; then
            changed=1
        fi
        rm "${data_file}.old"
    else
        # If no old data exists, consider it changed
        changed=1
        diff_summary="Initial data fetch"
    fi
    
    # 4. If changed, build and push
    if [[ $changed -eq 1 ]]; then
        log "  ✨ Changes detected: $diff_summary"
        log "  📊 Building and pushing..."
        uv run python scripts/build.py >> "$LOG_FILE" 2>&1
        
        # Take screenshot if script exists
        if [[ -f "scripts/take_screenshot.py" ]]; then
            log "  📸 Taking screenshot..."
            uv run python scripts/take_screenshot.py >> "$LOG_FILE" 2>&1
        fi

        # Fetch model cards if we are in the root or have specific scripts
        if [[ "$repo_name" == "Venice Pricing" ]]; then
            log "  🃏 Fetching Venice model cards..."
            uv run --with requests python "$BASE_DIR/scripts/fetch_venice_model_cards.py" >> "$LOG_FILE" 2>&1
        elif [[ "$repo_name" == "OpenRouter Dashboard" ]]; then
            log "  🃏 Fetching Free model cards..."
            uv run --with requests python "$BASE_DIR/scripts/fetch_free_model_cards.py" >> "$LOG_FILE" 2>&1
        fi
        
        # Clean up empty model card directories
        log "  🧹 Cleaning up empty model cards..."
        python3 "$BASE_DIR/scripts/clean_empty_model_cards.py" >> "$LOG_FILE" 2>&1
        
        # Check if build actually modified anything tracked by git
        if [[ -n $(git status --porcelain) ]]; then
            git add .
            # Include the diff summary in the commit message for better history
            git commit -m "chore: automated pricing update ($DATE)" -m "$diff_summary" >> "$LOG_FILE" 2>&1
            git push origin main >> "$LOG_FILE" 2>&1
            log "  ✅ Changes pushed to GitHub."
        else
            log "  💤 Build completed but no git changes."
        fi
    else
        log "  💤 No meaningful data changes. Skipping push."
    fi
}

# Process Venice Pricing
# We ignore 'created' key because it changes every fetch
process_repo "$BASE_DIR/venice-pricing" "Venice Pricing" "data/venice_data.json" "created"

# Process OpenRouter Dashboard
process_repo "$BASE_DIR/openrouter-pricing" "OpenRouter Pricing" "data/openrouter_data.json" ""

log "🏁 Automation Update Finished"
echo "------------------------------------------" >> "$LOG_FILE"
