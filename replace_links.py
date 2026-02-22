import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all <a href="http[s]://anpsthemes.com..."> with <a href="javascript:void(0)">
def repl_a(m):
    return m.group(1) + '"javascript:void(0)"'

# Look for <a ... href="something containing anpsthemes.com" ...>
content = re.sub(r'(<a[^>]*href\s*=\s*)[\'"][^\'"]*anpsthemes\.com[^\'"]*[\'"]', repl_a, content)

# Also forms
def repl_form(m):
    return m.group(1) + '"javascript:void(0)"'

content = re.sub(r'(<form[^>]*action\s*=\s*)[\'"][^\'"]*anpsthemes\.com[^\'"]*[\'"]', repl_form, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
