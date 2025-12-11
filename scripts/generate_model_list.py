#!/usr/bin/env python3
"""generate_model_list.py

Reads `venice_models_text.json` and generates `venice_models_text_full.html`.
The output HTML uses client-side rendering with embedded JSON to support
dynamic sorting and filtering, consistent with other model pages.
"""
import json
import pathlib

# Paths
BASE_DIR = pathlib.Path(__file__).resolve().parent
JSON_PATH = BASE_DIR.parent / "data" / "venice_models_text.json"
HTML_PATH = BASE_DIR.parent / "output" / "venice_models_text_full.html"

def generate_html(models_data):
    # Convert models to JSON string for embedding
    json_str = json.dumps(models_data, indent=4)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Venice Text Models</title>
    <style>
        :root {{
            --bg-color: #f8f9fa;
            --text-color: #212529;
            --card-bg: #ffffff;
            --border-color: #dee2e6;
            --primary-color: #0d6efd;
            --hover-bg: #e9ecef;
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

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: var(--bg-color);
            color: var(--text-color);
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        h1 {{
            text-align: center;
            margin-bottom: 30px;
        }}

        .controls {{
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
            flex-wrap: wrap;
            padding: 20px;
            background-color: var(--card-bg);
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}

        .search-box {{
            flex: 1;
            min-width: 200px;
        }}

        .search-box input {{
            width: 100%;
            padding: 8px 12px;
            border: 1px solid var(--border-color);
            border-radius: 4px;
            font-size: 16px;
            background-color: var(--bg-color);
            color: var(--text-color);
        }}

        .sort-box select {{
            padding: 8px 12px;
            border: 1px solid var(--border-color);
            border-radius: 4px;
            font-size: 16px;
            background-color: var(--bg-color);
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
    </style>
</head>
<body>
    <div class="container">
        <h1>Venice Text Models</h1>

        <div class="controls">
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="Search by name, ID, or source...">
            </div>
            <div class="sort-box">
                <select id="sortSelect">
                    <option value="default">Default Sort</option>
                    <option value="name">Sort by Name</option>
                    <option value="date_new">Sort by Date (Newest)</option>
                    <option value="context_high">Sort by Context (High to Low)</option>
                    <option value="price_low">Sort by Price (Input Low)</option>
                </select>
            </div>
        </div>

        <div class="table-container">
            <table id="modelsTable">
                <thead>
                    <tr>
                        <th onclick="sortTable('name')">Model</th>
                        <th onclick="sortTable('date')">Created</th>
                        <th onclick="sortTable('price')">Pricing (USD/1M)</th>
                        <th onclick="sortTable('context')">Context</th>
                        <th>Capabilities</th>
                        <th>Constraints</th>
                        <th>Source</th>
                    </tr>
                </thead>
                <tbody id="tableBody">
                    <!-- Data will be populated here -->
                </tbody>
            </table>
        </div>
    </div>

    <script>
        // Embedded JSON Data
        const modelsData = {json_str};

        const searchInput = document.getElementById('searchInput');
        const sortSelect = document.getElementById('sortSelect');
        const tableBody = document.getElementById('tableBody');

        function formatDate(timestamp) {{
            return new Date(timestamp * 1000).toLocaleDateString();
        }}

        function renderTable(data) {{
            tableBody.innerHTML = '';
            data.forEach(model => {{
                const spec = model.model_spec || {{}};
                const pricing = spec.pricing || {{}};
                const constraints = spec.constraints || {{}};
                const capabilities = spec.capabilities || {{}};
                
                const row = document.createElement('tr');
                
                // Helper for capabilities
                const cap = (name, val) => val ? `<span class="capability-tag cap-true">${{name}}</span>` : '';

                // Pricing display
                const inputPrice = pricing.input?.usd !== undefined ? `$${{pricing.input.usd}}` : '-';
                const outputPrice = pricing.output?.usd !== undefined ? `$${{pricing.output.usd}}` : '-';
                
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
                        <div>In: <span class="price-tag">${{inputPrice}}</span></div>
                        <div style="margin-top:2px;">Out: <span class="price-tag">${{outputPrice}}</span></div>
                    </td>
                    <td>
                        ${{spec.availableContextTokens?.toLocaleString() || '-'}}
                    </td>
                    <td>
                        ${{cap('Reasoning', capabilities.supportsReasoning)}}
                        ${{cap('Vision', capabilities.supportsVision)}}
                        ${{cap('Web Search', capabilities.supportsWebSearch)}}
                        ${{cap('Func Call', capabilities.supportsFunctionCalling)}}
                        ${{cap('Code Opt', capabilities.optimizedForCode)}}
                    </td>
                    <td>
                        <small>Temp: ${{constraints.temperature?.default || '-'}}</small><br>
                        <small>Top P: ${{constraints.top_p?.default || '-'}}</small>
                    </td>
                    <td>
                        ${{spec.modelSource ? `<a href="${{spec.modelSource}}" target="_blank">Source</a>` : '-'}}
                    </td>
                `;
                tableBody.appendChild(row);
            }});
        }}

        function filterAndSortData() {{
            let filtered = modelsData.filter(model => {{
                const term = searchInput.value.toLowerCase();
                const name = (model.model_spec?.name || '').toLowerCase();
                const id = model.id.toLowerCase();
                const source = (model.model_spec?.modelSource || '').toLowerCase();
                return name.includes(term) || id.includes(term) || source.includes(term);
            }});

            const sortValue = sortSelect.value;
            filtered.sort((a, b) => {{
                switch (sortValue) {{
                    case 'name':
                        return (a.model_spec?.name || a.id).localeCompare(b.model_spec?.name || b.id);
                    case 'date_new':
                        return b.created - a.created;
                    case 'context_high':
                         return (b.model_spec?.availableContextTokens || 0) - (a.model_spec?.availableContextTokens || 0);
                    case 'price_low':
                        return (a.model_spec?.pricing?.input?.usd || 0) - (b.model_spec?.pricing?.input?.usd || 0);
                    default:
                        return 0;
                }}
            }});

            renderTable(filtered);
        }}

        searchInput.addEventListener('input', filterAndSortData);
        sortSelect.addEventListener('change', filterAndSortData);

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
