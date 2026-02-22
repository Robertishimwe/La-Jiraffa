import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def repl_a(m):
    return m.group(1) + '"javascript:void(0)"'

# Strip external hrefs in anchor tags
content = re.sub(r'(<a[^>]*href\s*=\s*)[\'"](http://|https://)(?!localhost|127\.0\.0\.1)[^\'"]*[\'"]', repl_a, content)

# Strip external urls in data-actions
def repl_data(m):
    return m.group(1) + 'javascript:void(0);' + m.group(2)

content = re.sub(r'(data-actions\s*=\s*[\'"][^\'"]*url:)(http://|https://)(?!localhost|127\.0\.0\.1)[^;\'"]+(;[\'"])', repl_data, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
