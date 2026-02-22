import re

matches = []
with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'anpsthemes.com' in line or 'href="' in line or 'href=\'' in line or 'href=' in line:
            # Let's just find anything with anpsthemes.com
            if 'anpsthemes.com' in line:
                matches.append(f"{i+1}: {line.strip()}")

with open('external_links.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(matches))
