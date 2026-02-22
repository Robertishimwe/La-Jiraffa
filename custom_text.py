import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

changes = [
    # Slide 1 text
    (r'We\s*provide top-notch construction services<br />\s*tailored to your needs\. From planning to\s*execution,<br />\s*we ensure quality and excellence\.',
     r'La Jiraffa delivers premium construction services<br />\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tacross Rwanda. From planning to\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\texecution,<br />\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\twe ensure transparency and excellence.'),
     
    # Slide 2 text 
    (r'We\s*offer free consulting and the best project\s*management<br /> for your idea, 100% delivery\s*guaranteed\. <br /> See for yourself, get on board now\.',
     r'We offer expert consulting and the best project\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tmanagement<br /> tailored to your vision, 100%\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tguaranteed. <br /> Experience the La Jiraffa difference today.'),
     
    # Slide 2 title
    (r'Realize\s*your project',
     r'Realize your vision'),
     
    # Slide 3 text
    (r'AND\s*JOIN OVER 1200 SATISFIED CUSTOMERS',
     r'AND JOIN OUR SATISFIED CUSTOMERS IN RWANDA')
]

for pat, repl in changes:
    text, count = re.subn(pat, repl, text)
    print(f"Replaced {count} instances of {pat[:30]}...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
