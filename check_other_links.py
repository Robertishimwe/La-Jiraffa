import re

with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if re.search(r'<a[^>]*href\s*=\s*[\'"](http://|https://)(?!localhost|127\.0\.0\.1)', line):
            print(f'{i+1}: {line.strip()}')
