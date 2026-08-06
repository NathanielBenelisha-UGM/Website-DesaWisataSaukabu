import os

for root, dirs, files in os.walk('e:\\KKN-WEBSITE_SAUKABU'):
    for file in files:
        if file.endswith('.css') or file.endswith('.html'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if '.page-view' in line:
                        print(f"FOUND .page-view in {file}:{i+1}: {line.strip()}")
