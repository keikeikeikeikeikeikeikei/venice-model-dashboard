#!/usr/bin/env python3
"""
Generates the main dashboard (index.html) from venice_data.json.
"""
import json
import pathlib
from jinja2 import Environment, FileSystemLoader, select_autoescape

def generate_dashboard():
    # Paths
    # scripts/build.py
    base_dir = pathlib.Path(__file__).resolve().parent
    root_dir = base_dir.parent
    
    templates_dir = base_dir / "templates"
    data_file = root_dir / "data" / "venice_data.json"
    output_file = root_dir / "docs" / "index.html"
    
    # Check data
    if not data_file.exists():
        print(f"❌ Data file not found: {data_file}")
        return

    # Load Data
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    print(f"📊 Loaded data for dashboard generation")

    # Setup Jinja2
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )
    
    # Render
    template = env.get_template('dashboard.html')
    html_content = template.render(models_json=json.dumps(data, indent=2))
    
    # Save
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"✅ Generated Dashboard at {output_file}")

if __name__ == "__main__":
    generate_dashboard()
