#!/usr/bin/env python3
"""generate_video_model_list.py

Reads `data/venice_models_video.json` and generates `output/venice_models_video.html`.
The output HTML is self-contained with embedded JSON data and client-side sorting/filtering.
"""
import json
import pathlib
import datetime

# Paths
BASE_DIR = pathlib.Path(__file__).resolve().parent
JSON_PATH = BASE_DIR.parent / "data" / "venice_models_video.json"
HTML_PATH = BASE_DIR.parent / "output" / "venice_models_video.html"

def generate_html(models_data):
    # Convert models to JSON string for embedding
    json_str = json.dumps(models_data, indent=4)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Venice Video Models</title>
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

        .tag {{
            display: inline-block;
            padding: 2px 8px;
            margin: 2px;
            border-radius: 12px;
            background-color: var(--border-color);
            font-size: 0.85em;
        }}

        .spec-list {{
            margin: 0;
            padding-left: 1.2em;
            font-size: 0.9em;
        }}

        .bool-tag {{
            font-size: 0.8em;
            padding: 2px 6px;
            border-radius: 4px;
            margin-right: 4px;
        }}
        .bool-true {{ background-color: rgba(25, 135, 84, 0.15); color: #198754; }}
        .bool-false {{ background-color: rgba(220, 53, 69, 0.15); color: #dc3545; }}

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
        <h1>Venice Video Models</h1>

        <div class="controls">
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="Search by name, ID, or source...">
            </div>
            <div class="sort-box">
                <select id="sortSelect">
                    <option value="name">Sort by Name</option>
                    <option value="date_new">Sort by Date (Newest)</option>
                    <option value="date_old">Sort by Date (Oldest)</option>
                </select>
            </div>
        </div>

        <div class="table-container">
            <table id="modelsTable">
                <thead>
                    <tr>
                        <th onclick="sortTable('name')">Model</th>
                        <th onclick="sortTable('date')">Created</th>
                        <th>Type</th>
                        <th>Resolutions</th>
                        <th>Durations</th>
                        <th>Stats / Audio</th>
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
                const constraints = spec.constraints || {{}};
                
                // Helper to create list items
                const createList = (items) => {{
                    if (!items || items.length === 0) return '<span style="color: #999;">-</span>';
                    return `<ul class="spec-list">${{items.map(i => `<li>${{i}}</li>`).join('')}}</ul>`;
                }};

                const row = document.createElement('tr');
                
                // Format Model Type
                let modelType = constraints.model_type || model.type || 'video';
                
                // Audio Status
                const hasAudio = constraints.audio ? '<span class="bool-tag bool-true">Audio</span>' : '<span class="bool-tag bool-false">No Audio</span>';
                
                row.innerHTML = `
                    <td>
                        <div class="model-name">${{spec.name || model.id}}</div>
                        <div class="model-id">${{model.id}}</div>
                    </td>
                    <td>${{formatDate(model.created)}}</td>
                    <td>
                        <span class="tag">${{modelType}}</span>
                    </td>
                    <td>
                        ${{createList(constraints.resolutions)}}
                        ${{constraints.aspect_ratios && constraints.aspect_ratios.length > 0 ? '<div style="margin-top:4px; font-size:0.85em; color:#666;"><strong>AR:</strong> ' + constraints.aspect_ratios.join(', ') + '</div>' : ''}}
                    </td>
                    <td>
                        ${{createList(constraints.durations)}}
                    </td>
                    <td>
                        ${{hasAudio}}
                    </td>
                    <td>
                        ${{spec.modelSource ? `<a href="${{spec.modelSource}}" target="_blank">View Source</a>` : '-'}}
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
                    case 'date_old':
                        return a.created - b.created;
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
