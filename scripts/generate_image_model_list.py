#!/usr/bin/env python3
"""generate_image_model_list.py

Reads `data/venice_models_image.json` and generates `output/venice_models_image.html`.
The output HTML is self-contained with embedded JSON data and client-side sorting/filtering.
"""
import json
import pathlib
import datetime

# Paths
BASE_DIR = pathlib.Path(__file__).resolve().parent
JSON_PATH = BASE_DIR.parent / "data" / "venice_models_image.json"
HTML_PATH = BASE_DIR.parent / "output" / "venice_models_image.html"

def generate_html(models_data):
    # Convert models to JSON string for embedding
    json_str = json.dumps(models_data, indent=4)
    
    # Extract all unique traits
    all_traits = set()
    for model in models_data:
        traits = model.get('model_spec', {}).get('traits', [])
        all_traits.update(traits)
    all_traits = sorted(all_traits)
    
    # Generate trait filter checkboxes dynamically
    trait_checkboxes = ""
    for trait in all_traits:
        safe_id = trait.replace('-', '_').replace(' ', '_')
        trait_checkboxes += f"""
                <div class="filter-option">
                    <input type="checkbox" id="filterTrait_{safe_id}" data-trait="{trait}">
                    <label for="filterTrait_{safe_id}">{trait.replace('_', ' ').title()}</label>
                </div>"""
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Venice Image Models</title>
    <style>
        :root {{
            --bg-color: #f8f9fa;
            --text-color: #212529;
            --card-bg: #ffffff;
            --border-color: #dee2e6;
            --primary-color: #0d6efd;
            --hover-bg: #e9ecef;
            --sidebar-width: 280px;
        }}

        @media (prefers-color-scheme: dark) {{
            :root {{
                --bg-color: #212529;
                --text-color: #f8f9fa;
                --card-bg: #343a40;
                --border-color: #495057;
                --primary-color: #0d6efd;
                --hover-bg: #495057;
            }}
        }}

        * {{
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--bg-color);
            color: var(--text-color);
        }}

        .layout {{
            display: flex;
            min-height: 100vh;
        }}

        .sidebar {{
            width: var(--sidebar-width);
            background-color: var(--card-bg);
            border-right: 1px solid var(--border-color);
            padding: 20px;
            position: sticky;
            top: 0;
            height: 100vh;
            overflow-y: auto;
        }}

        .main-content {{
            flex: 1;
            padding: 20px;
        }}

        h1 {{
            margin: 0 0 30px 0;
        }}

        .sidebar h2 {{
            font-size: 1.2em;
            margin: 0 0 15px 0;
            color: var(--text-color);
        }}

        .filter-section {{
            margin-bottom: 25px;
        }}

        .filter-section h3 {{
            font-size: 0.9em;
            font-weight: 600;
            margin: 0 0 10px 0;
            color: var(--text-color);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .filter-option {{
            display: flex;
            align-items: center;
            margin-bottom: 8px;
            cursor: pointer;
        }}

        .filter-option input[type="checkbox"] {{
            margin-right: 8px;
            cursor: pointer;
            width: 16px;
            height: 16px;
        }}

        .filter-option label {{
            cursor: pointer;
            font-size: 0.95em;
            user-select: none;
        }}

        .stats-panel {{
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 8px 15px;
            align-items: center;
        }}

        .stat-item {{
            display: contents;
        }}

        .stat-label {{
            color: #6c757d;
            font-size: 0.85em;
            margin: 0;
        }}

        .stat-value {{
            font-weight: 600;
            font-size: 1em;
            color: var(--primary-color);
            text-align: right;
        }}

        .clear-filters-btn {{
            width: 100%;
            padding: 10px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.9em;
            font-weight: 500;
            margin-top: 15px;
        }}

        .clear-filters-btn:hover {{
            opacity: 0.9;
        }}

        .controls {{
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}

        .search-box {{
            flex: 1;
            min-width: 250px;
        }}

        .search-box input {{
            width: 100%;
            padding: 10px 15px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            font-size: 16px;
            background-color: var(--card-bg);
            color: var(--text-color);
        }}

        .sort-box select {{
            padding: 10px 15px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            font-size: 16px;
            background-color: var(--card-bg);
            color: var(--text-color);
            cursor: pointer;
        }}

        .table-container {{
            overflow-x: auto;
            background-color: var(--card-bg);
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            min-width: 1000px;
        }}

        th, td {{
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
            vertical-align: top;
        }}

        th {{
            background-color: var(--card-bg);
            font-weight: 600;
            cursor: pointer;
            user-select: none;
            white-space: nowrap;
            position: sticky;
            top: 0;
            z-index: 10;
        }}

        th:hover {{
            background-color: var(--hover-bg);
        }}

        tr:hover {{
            background-color: var(--hover-bg);
        }}

        .model-name {{
            font-weight: 600;
            font-size: 1.1em;
            margin-bottom: 4px;
        }}

        .model-id {{
            font-size: 0.85em;
            color: #6c757d;
            font-family: monospace;
        }}

        .price-tag {{
            display: inline-block;
            padding: 2px 6px;
            border-radius: 4px;
            background-color: rgba(13, 110, 253, 0.1);
            color: var(--primary-color);
            font-size: 0.9em;
            font-weight: 500;
            white-space: nowrap;
        }}

        .tag {{
            display: inline-block;
            padding: 2px 8px;
            margin: 2px;
            border-radius: 12px;
            background-color: var(--border-color);
            font-size: 0.85em;
        }}

        .capability-tag {{
            font-size: 0.8em;
            padding: 2px 6px;
            border-radius: 4px;
            margin: 2px;
            display: inline-block;
        }}
        .cap-true {{ background-color: rgba(25, 135, 84, 0.15); color: #198754; }}
        .cap-false {{ display: none; }} 

        a {{
            color: var(--primary-color);
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        @media (max-width: 1024px) {{
            .layout {{
                flex-direction: column;
            }}

            .sidebar {{
                width: 100%;
                height: auto;
                position: relative;
                border-right: none;
                border-bottom: 1px solid var(--border-color);
            }}
        }}
    </style>
</head>
<body>
    <div class="layout">
        <aside class="sidebar">
            <h2>Filters</h2>
            
            <div class="stats-panel">
                <div class="stat-item">
                    <div class="stat-label">Showing Models</div>
                    <div class="stat-value" id="statsCount">0</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">Avg Generation Price</div>
                    <div class="stat-value" id="statsAvgGen">-</div>
                </div>
            </div>

            <div class="filter-section">
                <h3>Features</h3>
                <div class="filter-option">
                    <input type="checkbox" id="filterWebSearch">
                    <label for="filterWebSearch">Web Search</label>
                </div>
            </div>

            <div class="filter-section">
                <h3>Traits</h3>{trait_checkboxes}
            </div>

            <button class="clear-filters-btn" id="clearFiltersBtn">Clear All Filters</button>
        </aside>

        <main class="main-content">
            <h1>Venice Image Models</h1>

            <div class="controls">
                <div class="search-box">
                    <input type="text" id="searchInput" placeholder="Search by name, ID, trait, or source...">
                </div>
                <div class="sort-box">
                    <select id="sortSelect">
                        <option value="price_low" selected>Sort by Price (Generation Low)</option>
                        <option value="name">Sort by Name</option>
                        <option value="date_new">Sort by Date (Newest)</option>
                    </select>
                </div>
            </div>

            <div class="table-container">
                <table id="modelsTable">
                    <thead>
                        <tr>
                            <th onclick="sortTable('name')">Model</th>
                            <th onclick="sortTable('date')">Created</th>
                            <th onclick="sortTable('price')">Pricing (USD)</th>
                            <th>Constraints</th>
                            <th>Features</th>
                            <th>Source</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody">
                        <!-- Data will be populated here -->
                    </tbody>
                </table>
            </div>
        </main>
    </div>

    <script>
        // Embedded JSON Data
        const modelsData = {json_str};

        const searchInput = document.getElementById('searchInput');
        const sortSelect = document.getElementById('sortSelect');
        const tableBody = document.getElementById('tableBody');
        const clearFiltersBtn = document.getElementById('clearFiltersBtn');
        const filterWebSearch = document.getElementById('filterWebSearch');
        
        // Get all trait checkboxes
        const traitCheckboxes = Array.from(document.querySelectorAll('[data-trait]'));

        // Stats elements
        const statsCount = document.getElementById('statsCount');
        const statsAvgGen = document.getElementById('statsAvgGen');

        function formatDate(timestamp) {{
            return new Date(timestamp * 1000).toLocaleDateString();
        }}

        function updateStats(data) {{
            statsCount.textContent = data.length;
            
            if (data.length > 0) {{
                const genPrices = data
                    .map(m => m.model_spec?.pricing?.generation?.usd)
                    .filter(p => p !== undefined);
                
                const avgGen = genPrices.length > 0 
                    ? (genPrices.reduce((a, b) => a + b, 0) / genPrices.length).toFixed(3)
                    : '-';
                
                statsAvgGen.textContent = avgGen !== '-' ? `$${{avgGen}}` : '-';
            }} else {{
                statsAvgGen.textContent = '-';
            }}
        }}

        function renderTable(data) {{
            tableBody.innerHTML = '';
            data.forEach(model => {{
                const spec = model.model_spec || {{}};
                const pricing = spec.pricing || {{}};
                const constraints = spec.constraints || {{}};
                
                const row = document.createElement('tr');
                
                // Helper for capabilities
                const cap = (name, val) => val ? `<span class="capability-tag cap-true">${{name}}</span>` : '';

                // Pricing display
                const genPrice = pricing.generation?.usd !== undefined ? `${{pricing.generation.usd}}` : '-';
                const upscale2x = pricing.upscale?.['2x']?.usd !== undefined ? `${{pricing.upscale['2x'].usd}}` : '-';
                
                row.innerHTML = `
                    <td>
                        <div class="model-name">${{spec.name || model.id}}</div>
                        <div class="model-id">${{model.id}}</div>
                        <div style="margin-top:4px;">
                           ${{(spec.traits || []).map(t => `<span class="tag">${{t}}</span>`).join('')}}
                        </div>
                    </td>
                    <td>${{formatDate(model.created)}}</td>
                    <td>
                        <div>Gen: <span class="price-tag">${{genPrice}}</span></div>
                        <div style="margin-top:2px; font-size:0.85em; color:#666;">Upscale 2x: ${{upscale2x}}</div>
                    </td>
                    <td>
                        <small>Steps: ${{constraints.steps?.default}} (Max: ${{constraints.steps?.max}})</small><br>
                        <small>Limit: ${{constraints.promptCharacterLimit}} chars</small>
                    </td>
                    <td>
                        ${{cap('Web Search', spec.supportsWebSearch)}}
                    </td>
                    <td>
                        ${{spec.modelSource ? `<a href="${{spec.modelSource}}" target="_blank">Source</a>` : '-'}}
                    </td>
                `;
                tableBody.appendChild(row);
            }});
            
            updateStats(data);
        }}

        function filterAndSortData() {{
            let filtered = modelsData.filter(model => {{
                const spec = model.model_spec || {{}};
                
                // Text search
                const term = searchInput.value.toLowerCase();
                const name = (spec.name || '').toLowerCase();
                const id = model.id.toLowerCase();
                const source = (spec.modelSource || '').toLowerCase();
                const traits = (spec.traits || []).join(' ').toLowerCase();
                
                const matchesSearch = name.includes(term) || id.includes(term) || 
                                     source.includes(term) || traits.includes(term);
                
                if (!matchesSearch) return false;
                
                // Web Search filter
                if (filterWebSearch.checked && !spec.supportsWebSearch) return false;
                
                // Trait filters
                const checkedTraits = traitCheckboxes
                    .filter(cb => cb.checked)
                    .map(cb => cb.dataset.trait);
                
                if (checkedTraits.length > 0) {{
                    const modelTraits = spec.traits || [];
                    const hasAnyTrait = checkedTraits.some(trait => modelTraits.includes(trait));
                    if (!hasAnyTrait) return false;
                }}
                
                return true;
            }});

            const sortValue = sortSelect.value;
            filtered.sort((a, b) => {{
                switch (sortValue) {{
                    case 'name':
                        return (a.model_spec?.name || a.id).localeCompare(b.model_spec?.name || b.id);
                    case 'date_new':
                        return b.created - a.created;
                    case 'price_low':
                        return (a.model_spec?.pricing?.generation?.usd || 0) - (b.model_spec?.pricing?.generation?.usd || 0);
                    default:
                        return 0;
                }}
            }});

            renderTable(filtered);
        }}

        // Event listeners
        searchInput.addEventListener('input', filterAndSortData);
        sortSelect.addEventListener('change', filterAndSortData);
        filterWebSearch.addEventListener('change', filterAndSortData);
        
        traitCheckboxes.forEach(checkbox => {{
            checkbox.addEventListener('change', filterAndSortData);
        }});

        clearFiltersBtn.addEventListener('click', () => {{
            searchInput.value = '';
            filterWebSearch.checked = false;
            traitCheckboxes.forEach(cb => cb.checked = false);
            filterAndSortData();
        }});

        // Initial render
        filterAndSortData();
    </script>
</body>
</html>
"""
    return html_content

def main():
    if not JSON_PATH.exists():
        print(f"Error: JSON file not found at {JSON_PATH}")
        return

    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            models_data = json.load(f)
        
        html_output = generate_html(models_data)
        
        with open(HTML_PATH, "w", encoding="utf-8") as f:
            f.write(html_output)
            
        print(f"✅ Generated {HTML_PATH} ({len(models_data)} models)")
        
    except Exception as e:
        print(f"Error generating HTML: {e}")

if __name__ == "__main__":
    main()
