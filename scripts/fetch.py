#!/usr/bin/env python3
"""
Fetch all Venice model data and pricing in one go.
Saves to a single `data/venice_data.json`.
"""
import json
import pathlib
import time
import urllib.request
import requests

# API Configuration
API_BASE = "https://api.venice.ai/api/v1"
MODELS_ENDPOINT = f"{API_BASE}/models?type=all"
QUOTE_ENDPOINT = f"{API_BASE}/video/quote"

# Paths
# __file__ = scripts/fetch.py
# parent = scripts
# parent.parent = venice-pricing (Root)
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_FILE = DATA_DIR / "venice_data.json"

def fetch_all_models():
    """Fetch all models from the main endpoint."""
    print(f"📥 Fetching all models from {MODELS_ENDPOINT}...")
    try:
        req = urllib.request.Request(
            MODELS_ENDPOINT, 
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
        # print(f"  ⚠️  Quote failed for {model['id']}: {e}")
        return None

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Fetch raw models
    all_models = fetch_all_models()
    if not all_models:
        return

    # 2. Group by type
    grouped = {
        "text": [],
        "image": [],
        "video": [],
        "other": []
    }
    
    print(f"📦 Processing {len(all_models)} models...")
    
    for model in all_models:
        m_type = model.get('type', 'other')
        if m_type in grouped:
            grouped[m_type].append(model)
        else:
            grouped['other'].append(model)
            
    # 3. Enrich video models with pricing
    video_models = grouped['video']
    print(f"💰 Fetching quotes for {len(video_models)} video models...")
    
    for i, model in enumerate(video_models, 1):
        # Progress indicator
        print(f"\r  [{i}/{len(video_models)}] Fetching quote for {model['id']}...", end="", flush=True)
        
        price = get_video_quote(model)
        if price is not None:
            if 'pricing' not in model: model['pricing'] = {}
            model['pricing']['base_price_usd'] = price
        
        # Rate limit
        time.sleep(0.2)
        
    print(f"\n✅ Data preparation complete.")
    
    # 4. Save single JSON
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(grouped, f, indent=2, ensure_ascii=False)
        
    print(f"💾 Saved consolidated data to {OUTPUT_FILE}")
    print(f"  - Text: {len(grouped['text'])}")
    print(f"  - Image: {len(grouped['image'])}")
    print(f"  - Video: {len(grouped['video'])}")

if __name__ == "__main__":
    main()
