#!/usr/bin/env python3
"""generate_video_model_list_enhanced.py

Simplified enhanced script for Venice video models with sidebar filters.
"""
import json
import pathlib

# Paths
BASE_DIR = pathlib.Path(__file__).resolve().parent
JSON_PATH = BASE_DIR.parent / "data" / "venice_models_video.json"
HTML_PATH = BASE_DIR.parent / "output" / "venice_models_video.html"

def generate_html(models_data):
    json_str = json.dumps(models_data, indent=4)
    
    # Extract unique resolutions
    all_resolutions = set()
    for model in models_data:
        resolutions = model.get('model_spec', {}).get('constraints', {}).get('resolutions', [])
        all_resolutions.update(resolutions)
    all_resolutions = sorted(all_resolutions, key=lambda x: int(x.replace('p', '')) if 'p' in x else 0)
    
    # Generate resolution checkboxes
    resolution_filters = ""
    for res in all_resolutions:
        safe_id = res.replace('p', '')
        resolution_filters += f'''
                <div class="filter-option">
                    <input type="checkbox" id="filterRes_{safe_id}" data-resolution="{res}">
                    <label for="filterRes_{safe_id}">{res}</label>
                </div>'''
    
    return f'''<!DOCTYPE html>
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

        * {{ box-sizing: border-box; }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
             margin: 0;
            padding: 0;
            background-color: var(--bg-color);
            color: var(--text-color);
        }}

        .layout {{ display: flex; min-height: 100vh; }}

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

        .main-content {{ flex: 1; padding: 20px; }}
        h1 {{ margin: 0 0 30px 0; }}
        .sidebar h2 {{ font-size: 1.2em; margin: 0 0 15px 0; }}
        
        .filter-section {{ margin-bottom: 25px; }}
        .filter-section h3 {{
            font-size: 0.9em;
            font-weight: 600;
            margin: 0 0 10px 0;
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
            margin-top: 15px;
        }}

        .controls {{ display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap; }}
        .search-box {{ flex: 1; min-width: 250px; }}
        .search-box input {{
            width: 100%;
            padding: 10px 15px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background-color: var(--card-bg);
            color: var(--text-color);
        }}

        .sort-box select {{
            padding: 10px 15px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
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

        table {{ width: 100%; border-collapse: collapse; min-width: 1000px; }}
        th, td {{ padding: 12px 16px; text-align: left; border-bottom: 1px solid var(--border-color); }}
        th {{
            background-color: var(--card-bg);
            font-weight: 600;
            cursor: pointer;
            user-select: none;
            position: sticky;
            top: 0;
            z-index: 10;
        }}

        th:hover {{ background-color: var(--hover-bg); }}
        tr:hover {{ background-color: var(--hover-bg); }}

        .model-name {{ font-weight: 600; font-size: 1.1em; margin-bottom: 4px; }}
        .model-id {{ font-size: 0.85em; color: #6c757d; font-family: monospace; }}
        .tag {{ display: inline-block; padding: 2px 8px; margin: 2px; border-radius: 12px; background-color: var(--border-color); font-size: 0.85em; }}
        .bool-tag {{ font-size: 0.8em; padding: 2px 6px; border-radius: 4px; margin-right: 4px; }}
        .bool-true {{ background-color: rgba(25, 135, 84, 0.15); color: #198754; }}
        .bool-false {{ background-color: rgba(220, 53, 69, 0.15); color: #dc3545; }}
        .price-note {{ font-size: 0.9em; color: #6c757d; font-style: italic; }}
        a {{ color: var(--primary-color); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}

        @media (max-width: 1024px) {{
            .layout {{ flex-direction: column; }}
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
            </div>

            <div class="filter-section">
                <h3>Model Type</h3>
                <div class="filter-option">
                    <input type="checkbox" id="filterTextToVideo">
                    <label for="filterTextToVideo">Text-to-Video</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="filterImageToVideo">
                    <label for="filterImageToVideo">Image-to-Video</label>
                </div>
            </div>

            <div class="filter-section">
                <h3>Audio</h3>
                <div class="filter-option">
                    <input type="checkbox" id="filterAudio">
                    <label for="filterAudio">Has Audio</label>
                </div>
            </div>

            <div class="filter-section">
                <h3>Resolution</h3>{resolution_filters}
            </div>

            <button class="clear-filters-btn" id="clearFiltersBtn">Clear All Filters</button>
        </aside>

        <main class="main-content">
            <h1>Venice Video Models</h1>

            <div class="controls">
                <div class="search-box">
                    <input type="text" id="searchInput" placeholder="Search by name, ID, or source...">
                </div>
                <div class="sort-box">
                    <select id="sortSelect">
                        <option value="name">Sort by Name</option>
                        <option value="date_new">Sort by Date (Newest)</option>
                    </select>
                </div>
            </div>

            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Model</th>
                            <th>Created</th>
                            <th>Pricing</th>
                            <th>Type</th>
                            <th>Resolutions</th>
                            <th>Audio</th>
                            <th>Source</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody"></tbody>
                </table>
            </div>
        </main>
    </div>

    <script>
        const modelsData = {json_str};
        const searchInput = document.getElementById('searchInput');
        const sortSelect = document.getElementById('sortSelect');
        const tableBody = document.getElementById('tableBody');
        const clearFiltersBtn = document.getElementById('clearFiltersBtn');
        const filterTextToVideo = document.getElementById('filterTextToVideo');
        const filterImageToVideo = document.getElementById('filterImageToVideo');
        const filterAudio = document.getElementById('filterAudio');
        const resolutionCheckboxes = Array.from(document.querySelectorAll('[data-resolution]'));
        const statsCount = document.getElementById('statsCount');

        function formatDate(timestamp) {{
            return new Date(timestamp * 1000).toLocaleDateString();
        }}

        function renderTable(data) {{
            statsCount.textContent = data.length;
            tableBody.innerHTML = '';
            
            data.forEach(model => {{
                const spec = model.model_spec || {{}};
                const constraints = spec.constraints || {{}};
                const modelType = constraints.model_type || 'video';
                const hasAudio = constraints.audio ? '<span class="bool-tag bool-true">Audio</span>' : '<span class="bool-tag bool-false">No Audio</span>';
                const resolutions = (constraints.resolutions || []).join(', ') || '-';
                
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>
                        <div class="model-name">${{spec.name || model.id}}</div>
                        <div class="model-id">${{model.id}}</div>
                    </td>
                    <td>${{formatDate(model.created)}}</td>
                    <td><span class="price-note">Dynamic</span></td>
                    <td><span class="tag">${{modelType}}</span></td>
                    <td>${{resolutions}}</td>
                    <td>${{hasAudio}}</td>
                    <td>${{spec.modelSource ? `<a href="${{spec.modelSource}}" target="_blank">Source</a>` : '-'}}</td>
                `;
                tableBody.appendChild(row);
            }});
        }}

        function filterAndSortData() {{
            let filtered = modelsData.filter(model => {{
                const spec = model.model_spec || {{}};
                const constraints = spec.constraints || {{}};
                
                // Text search
                const term = searchInput.value.toLowerCase();
                const name = (spec.name || '').toLowerCase();
                const id = model.id.toLowerCase();
                const source = (spec.modelSource || '').toLowerCase();
                if (!name.includes(term) && !id.includes(term) && !source.includes(term)) return false;
                
                // Model type filter
                const modelType = constraints.model_type || '';
                if (filterTextToVideo.checked && !modelType.includes('text-to-video')) return false;
                if (filterImageToVideo.checked && !modelType.includes('image-to-video')) return false;
                
                // Audio filter
                if (filterAudio.checked && !constraints.audio) return false;
                
                // Resolution filter
                const checkedResolutions = resolutionCheckboxes
                    .filter(cb => cb.checked)
                    .map(cb => cb.dataset.resolution);
                if (checkedResolutions.length > 0) {{
                    const modelResolutions = constraints.resolutions || [];
                    const hasAnyResolution = checkedResolutions.some(res => modelResolutions.includes(res));
                    if (!hasAnyResolution) return false;
                }}
                
                return true;
            }});

            filtered.sort((a, b) => {{
                if (sortSelect.value === 'name') {{
                    return (a.model_spec?.name || a.id).localeCompare(b.model_spec?.name || b.id);
                }}
                return b.created - a.created;
            }});

            renderTable(filtered);
        }}

        searchInput.addEventListener('input', filterAndSortData);
        sortSelect.addEventListener('change', filterAndSortData);
        filterTextToVideo.addEventListener('change', filterAndSortData);
        filterImageToVideo.addEventListener('change', filterAndSortData);
        filterAudio.addEventListener('change', filterAndSortData);
        resolutionCheckboxes.forEach(cb => cb.addEventListener('change', filterAndSortData));

        clearFiltersBtn.addEventListener('click', () => {{
            searchInput.value = '';
            filterTextToVideo.checked = false;
            filterImageToVideo.checked = false;
            filterAudio.checked = false;
            resolutionCheckboxes.forEach(cb => cb.checked = false);
            filterAndSortData();
        }});

        filterAndSortData();
    </script>
</body>
</html>'''

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
