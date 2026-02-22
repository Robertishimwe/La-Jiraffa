import re

found = False
with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if re.search(r'<a[^>]*href\s*=\s*[\'"](http://|https://)(?!localhost|127\.0\.0\.1)[^\'"]*[\'"]', line):
            print(f"Found external link at line {i+1}: {line.strip()}")
            found = True
        if re.search(r'<form[^>]*action\s*=\s*[\'"](http://|https://)(?!localhost|127\.0\.0\.1)[^\'"]*[\'"]', line):
            print(f"Found external form action at line {i+1}: {line.strip()}")
            found = True
        if re.search(r'data-actions\s*=\s*[\'"][^\'"]*url:(http://|https://)(?!localhost|127\.0\.0\.1)', line):
            print(f"Found external redirect in data-action at line {i+1}: {line.strip()}")
            found = True
        if re.search(r'window\.location|location\.href|location\.replace', line):
            print(f"Found JS redirect at line {i+1}: {line.strip()}")
            found = True

if not found:
    print("ALL CLEAR: No outbound links found.")
