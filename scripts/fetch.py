#!/usr/bin/env python3
"""
Fetch Venice model data and pricing.
Saves to `data/venice_data.json`.
Supports filtering by type and skipping video quotes for faster debugging.
"""
import json
import pathlib
import time
import urllib.request
import requests
import argparse
import sys

# API Configuration
API_BASE = "https://api.venice.ai/api/v1"
MODELS_ENDPOINT = f"{API_BASE}/models"
QUOTE_ENDPOINT = f"{API_BASE}/video/quote"

# Paths
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_FILE = DATA_DIR / "venice_data.json"

def fetch_models(model_type='all'):
    """Fetch models from the main endpoint, optionally filtering by type."""
    url = f"{MODELS_ENDPOINT}?type={model_type}"
    print(f"📥 Fetching models from {url}...")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'VenicePricingFetcher/1.0'}
        )
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get('data', [])
    except Exception as e:
        print(f"❌ Error fetching models: {e}")
        return []

def get_video_quote(model):
    """Get pricing quote for a specific video model."""
    constraints = model.get('model_spec', {}).get('constraints', {})
    model_type = constraints.get('model_type', 'text-to-video')
    
    # Build params based on constraints
    params = {
        'model': model['id'],
        'prompt': 'quote'
    }
    
    # Add resolution (lowest)
    resolutions = constraints.get('resolutions', [])
    if resolutions:
        params['resolution'] = resolutions[-1]
    
    # Add duration (shortest)
    durations = constraints.get('durations', [])
    if durations:
        params['duration'] = durations[0]
    
    # Add aspect ratio
    aspect_ratios = constraints.get('aspect_ratios', [])
    if aspect_ratios:
        params['aspect_ratio'] = aspect_ratios[0]
    
    if 'image-to-video' in model_type:
        params['image_url'] = 'https://venice.ai/favicon.ico'
        
    if constraints.get('audio_configurable'):
        params['audio'] = constraints.get('audio', False)

    try:
        response = requests.post(QUOTE_ENDPOINT, json=params)
        response.raise_for_status()
        return response.json().get('quote')
    except Exception as e:
        return None

def load_existing_data():
    if OUTPUT_FILE.exists():
        try:
            with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return {
        "text": [],
        "image": [],
        "video": [],
        "other": []
    }

def main():
    parser = argparse.ArgumentParser(description="Fetch Venice.ai model data")
    parser.add_argument("--type", choices=['all', 'text', 'image', 'video'], default='all', help="Model type to fetch")
    parser.add_argument("--skip-quotes", action="store_true", help="Skip fetching video quotes (faster)")
    args = parser.parse_args()

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # 3. Load existing data to merge (Load FIRST to ensure we have base)
    existing_data = load_existing_data()
    
    # Cache old video prices to avoid re-fetching and noise
    old_video_prices = {}
    for v in existing_data.get('video', []):
        if 'id' in v and 'pricing' in v:
            old_video_prices[v['id']] = v['pricing']

    # 1. Fetch raw models
    fetched_models = fetch_models(args.type)
    if not fetched_models:
        print("⚠️ No models fetched or API error.")
        # If specific type requested and failed, maybe don't abort completely if we want to just save nothing?
        # But usually we return.
        # return 
        # Actually, let's continue so we don't break if transient error? 
        # No, if fetch fails, we shouldn't wipe data.
        if not existing_data.get('text'): # If completely empty
             return
    
    final_data = existing_data # Start with existing

    # 2. Group by type (for the newly fetched data)
    new_grouped = {
        "text": [],
        "image": [],
        "video": [],
        "other": []
    }
    
    if fetched_models:
        print(f"📦 Processing {len(fetched_models)} fetched models...")
        for model in fetched_models:
            m_type = model.get('type', 'other')
            if m_type in new_grouped:
                new_grouped[m_type].append(model)
            else:
                new_grouped['other'].append(model)

        # 4. Merge logic
        if args.type == 'all':
            final_data = new_grouped
        else:
            final_data[args.type] = new_grouped[args.type]

    # 5. Enrich video models with pricing
    video_models = final_data.get('video', [])
    
    should_fetch_quotes = (not args.skip_quotes) and (args.type in ['all', 'video'])
    
    if video_models and should_fetch_quotes:
        print(f"💰 Checking quotes for {len(video_models)} video models...")
        fetch_count = 0
        for i, model in enumerate(video_models, 1):
            mid = model['id']
            # REUSE PRICE if available
            if mid in old_video_prices:
                model['pricing'] = old_video_prices[mid]
                # print(f"  Using cached price for {mid}")
                continue

            # Fetch NEW price
            print(f"\r  [{i}/{len(video_models)}] Fetching NEW quote for {mid}...", end="", flush=True)
            price = get_video_quote(model)
            if price is not None:
                if 'pricing' not in model: model['pricing'] = {}
                model['pricing']['base_price_usd'] = price
            fetch_count += 1
            time.sleep(0.2)
        
        if fetch_count > 0:
            print(f"\n✅ Fetched {fetch_count} new quotes.")
        else:
            print("\n✅ All video prices reused from cache.")

    elif args.skip_quotes:
        print("⏩ Skipping video quote fetching.")
    else:
        # We didn't fetch video (e.g. type=text), so we don't refresh quotes. 
        # Existing quotes in final_data['video'] are preserved.
        print("ℹ️ Preserving existing video data/quotes.")

    print(f"✅ Data preparation complete.")
    
    # 6. Save
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, indent=2, ensure_ascii=False)
        
    print(f"💾 Saved data to {OUTPUT_FILE}")
    print(f"  - Text: {len(final_data.get('text', []))}")
    print(f"  - Image: {len(final_data.get('image', []))}")
    print(f"  - Video: {len(final_data.get('video', []))}")

if __name__ == "__main__":
    main()