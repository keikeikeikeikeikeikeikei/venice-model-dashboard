import urllib.request
import json

def fetch_and_save_models():
    url = "https://api.venice.ai/api/v1/models?type=all"
    print(f"Fetching data from {url}...")
    
    try:
        # Create a request with a user agent to avoid potential 403s (though curl worked fine)
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (compatible; VenicePricingFetcher/1.0)'
            }
        )
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
        if 'data' not in data:
            print("Error: 'data' field not found in API response.")
            return

        models = data['data']
        print(f"Found {len(models)} models.")

        # Group models by type
        models_by_type = {}
        for model in models:
            model_type = model.get('type', 'unknown')
            if model_type not in models_by_type:
                models_by_type[model_type] = []
            models_by_type[model_type].append(model)

        # Prepare paths
        import pathlib
        base_dir = pathlib.Path(__file__).parent
        data_dir = base_dir.parent / 'data'
        data_dir.mkdir(parents=True, exist_ok=True)

        # Save to files
        for model_type, type_models in models_by_type.items():
            filename = data_dir / f"venice_models_{model_type}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(type_models, f, indent=2, ensure_ascii=False)
            print(f"Saved {len(type_models)} models of type '{model_type}' to {filename}")

        # Save all models to a single JS file for the specific dashboard
        js_filename = data_dir / "all_models.js"
        with open(js_filename, 'w', encoding='utf-8') as f:
            f.write("window.veniceModels = ")
            json.dump(models_by_type, f, indent=2, ensure_ascii=False)
            f.write(";")
        print(f"Saved combined data to {js_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_save_models()
