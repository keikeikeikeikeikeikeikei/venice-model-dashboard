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
            --success-color: #198754;
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
            padding: 12px;
            margin-bottom: 20px;
        }}

        .stat-item {{
            padding: 8px;
            margin-bottom: 8px;
            background-color: var(--card-bg);
            border-radius: 4px;
            text-align: center;
        }}
        
        .stat-item:last-child {{
            margin-bottom: 0;
        }}

        .stat-label {{
            color: #6c757d;
            font-size: 0.75em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 4px;
        }}

        .stat-value {{
            font-weight: 700;
            font-size: 1.5em;
            color: var(--primary-color);
            line-height: 1;
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
        
        .filtered-out {{
            display: none;
        }}
        
        .filtered-out.show-excluded {{
            display: table-row;
            opacity: 0.3;
            pointer-events: none;
        }} 

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
                    <div class="stat-label">Matching Models</div>
                    <div class="stat-value" id="statsCount">0</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">Excluded Models</div>
                    <div class="stat-value" id="statsExcluded">0</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">Avg Input Price</div>
                    <div class="stat-value" id="statsAvgInput">-</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">Avg Output Price</div>
                    <div class="stat-value" id="statsAvgOutput">-</div>
                </div>
            </div>

            <div class="filter-section">
                <h3>Capabilities</h3>
                <div class="filter-option">
                    <input type="checkbox" id="filterReasoning">
                    <label for="filterReasoning">Reasoning</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="filterVision">
                    <label for="filterVision">Vision</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="filterReasoningVision">
                    <label for="filterReasoningVision">Reasoning + Vision</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="filterWebSearch">
                    <label for="filterWebSearch">Web Search</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="filterFunctionCalling">
                    <label for="filterFunctionCalling">Function Calling</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="filterCodeOptimized">
                    <label for="filterCodeOptimized">Code Optimized</label>
                </div>
                <div class="filter-option">
                    <input type="checkbox" id="filterResponseSchema">
                    <label for="filterResponseSchema">Response Schema</label>
                </div>
            </div>

            <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid var(--border-color);">
                <div class="filter-option">
                    <input type="checkbox" id="showExcluded">
                    <label for="showExcluded">Show Excluded Models</label>
                </div>
            </div>

            <button class="clear-filters-btn" id="clearFiltersBtn">Clear All Filters</button>
        </aside>

        <main class="main-content">
            <h1>Venice Text Models</h1>

            <div class="controls">
                <div class="search-box">
                    <input type="text" id="searchInput" placeholder="Search by name, ID, capability, or source...">
                </div>
                <div class="sort-box">
                    <select id="sortSelect">
                        <option value="price_low" selected>Sort by Price (Input Low)</option>
                        <option value="default">Default Sort</option>
                        <option value="name">Sort by Name</option>
                        <option value="date_new">Sort by Date (Newest)</option>
                        <option value="context_high">Sort by Context (High to Low)</option>
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
        </main>
    </div>

    <script>
        // Embedded JSON Data
        const modelsData = {json_str};

        const searchInput = document.getElementById('searchInput');
        const sortSelect = document.getElementById('sortSelect');
        const tableBody = document.getElementById('tableBody');
        const clearFiltersBtn = document.getElementById('clearFiltersBtn');
        const showExcluded = document.getElementById('showExcluded');
        
        // Filter checkboxes
        const filters = {{
            reasoning: document.getElementById('filterReasoning'),
            vision: document.getElementById('filterVision'),
            reasoningVision: document.getElementById('filterReasoningVision'),
            webSearch: document.getElementById('filterWebSearch'),
            functionCalling: document.getElementById('filterFunctionCalling'),
            codeOptimized: document.getElementById('filterCodeOptimized'),
            responseSchema: document.getElementById('filterResponseSchema')
        }};

        // Stats elements
        const statsCount = document.getElementById('statsCount');
        const statsExcluded = document.getElementById('statsExcluded');
        const statsAvgInput = document.getElementById('statsAvgInput');
        const statsAvgOutput = document.getElementById('statsAvgOutput');

        function formatDate(timestamp) {{
            return new Date(timestamp * 1000).toLocaleDateString();
        }}

        function updateStats(matchingData, totalCount) {{
            statsCount.textContent = matchingData.length;
            statsExcluded.textContent = totalCount - matchingData.length;
            
            if (matchingData.length > 0) {{
                const inputPrices = matchingData
                    .map(m => m.model_spec?.pricing?.input?.usd)
                    .filter(p => p !== undefined);
                const outputPrices = matchingData
                    .map(m => m.model_spec?.pricing?.output?.usd)
                    .filter(p => p !== undefined);
                
                const avgInput = inputPrices.length > 0 
                    ? (inputPrices.reduce((a, b) => a + b, 0) / inputPrices.length).toFixed(2)
                    : '-';
                const avgOutput = outputPrices.length > 0 
                    ? (outputPrices.reduce((a, b) => a + b, 0) / outputPrices.length).toFixed(2)
                    : '-';
                
                statsAvgInput.textContent = avgInput !== '-' ? `$${{avgInput}}` : '-';
                statsAvgOutput.textContent = avgOutput !== '-' ? `$${{avgOutput}}` : '-';
            }} else {{
                statsAvgInput.textContent = '-';
                statsAvgOutput.textContent = '-';
            }}
        }}

        function renderTable(matchingSet) {{
            tableBody.innerHTML = '';
            const shouldShowExcluded = showExcluded.checked;
            
            modelsData.forEach(model => {{
                const spec = model.model_spec || {{}};
                const pricing = spec.pricing || {{}};
                const constraints = spec.constraints || {{}};
                const capabilities = spec.capabilities || {{}};
                
                const row = document.createElement('tr');
                const isMatching = matchingSet.has(model.id);
                if (!isMatching) {{
                    row.classList.add('filtered-out');
                    if (shouldShowExcluded) {{
                        row.classList.add('show-excluded');
                    }}
                }}
                
                // Helper for capabilities
                const cap = (name, val) => val ? `<span class="capability-tag cap-true">${{name}}</span>` : '';

                // Pricing display
                const inputPrice = pricing.input?.usd !== undefined ? `${{pricing.input.usd}}` : '-';
                const outputPrice = pricing.output?.usd !== undefined ? `${{pricing.output.usd}}` : '-';
                
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
                        ${{cap('Schema', capabilities.supportsResponseSchema)}}
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
                const spec = model.model_spec || {{}};
                const capabilities = spec.capabilities || {{}};
                
                // Text search
                const term = searchInput.value.toLowerCase();
                const name = (spec.name || '').toLowerCase();
                const id = model.id.toLowerCase();
                const source = (spec.modelSource || '').toLowerCase();
                
                // Build searchable capability string
                const capStrings = [];
                if (capabilities.supportsReasoning) capStrings.push('reasoning');
                if (capabilities.supportsVision) capStrings.push('vision');
                if (capabilities.supportsWebSearch) capStrings.push('web search');
                if (capabilities.supportsFunctionCalling) capStrings.push('function calling');
                if (capabilities.optimizedForCode) capStrings.push('code');
                if (capabilities.supportsResponseSchema) capStrings.push('schema');
                const capText = capStrings.join(' ');
                
                const matchesSearch = name.includes(term) || id.includes(term) || 
                                     source.includes(term) || capText.includes(term);
                
                if (!matchesSearch) return false;
                
                // Capability filters
                if (filters.reasoning.checked && !capabilities.supportsReasoning) return false;
                if (filters.vision.checked && !capabilities.supportsVision) return false;
                if (filters.reasoningVision.checked && 
                    !(capabilities.supportsReasoning && capabilities.supportsVision)) return false;
                if (filters.webSearch.checked && !capabilities.supportsWebSearch) return false;
                if (filters.functionCalling.checked && !capabilities.supportsFunctionCalling) return false;
                if (filters.codeOptimized.checked && !capabilities.optimizedForCode) return false;
                if (filters.responseSchema.checked && !capabilities.supportsResponseSchema) return false;
                
                return true;
            }});

            // Create a set of matching model IDs for efficient lookup
            const matchingSet = new Set(filtered.map(m => m.id));
            
            updateStats(filtered, modelsData.length);
            renderTable(matchingSet);
        }}

        // Event listeners
        searchInput.addEventListener('input', filterAndSortData);
        sortSelect.addEventListener('change', filterAndSortData);
        showExcluded.addEventListener('change', filterAndSortData);
        
        Object.values(filters).forEach(checkbox => {{
            checkbox.addEventListener('change', filterAndSortData);
        }});

        clearFiltersBtn.addEventListener('click', () => {{
            searchInput.value = '';
            Object.values(filters).forEach(checkbox => {{
                checkbox.checked = false;
            }});
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
