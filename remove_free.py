import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

changes = [
    (r'>FREE CONSULTATION FOR YOUR PROJECT<', r'>CONSULTATION FOR YOUR PROJECT<'),
    (r'>GET YOUR FREE CONSULTATION<', r'>GET YOUR CONSULTATION<'),
    (r'offer free consultation to achieve', r'offer consultation to achieve')
]

for pat, repl in changes:
    text, count = re.subn(pat, repl, text, flags=re.IGNORECASE)
    print(f"Replaced {count} instances of {pat}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
