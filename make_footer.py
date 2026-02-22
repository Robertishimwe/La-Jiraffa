import os
import re

index_path = r"C:\Users\TestSolutions\Documents\La-Jiraffa\index.html"
contact_path = r"C:\Users\TestSolutions\Documents\La-Jiraffa\contact.html"
footer_js_path = r"C:\Users\TestSolutions\Documents\La-Jiraffa\js\footer.js"

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the footer from index.html
footer_match = re.search(r'(<footer class="site-footer style-1">.*?</footer>)', index_content, re.DOTALL)
if footer_match:
    footer_html = footer_match.group(1)
    
    # Create the JS file content
    # Using template literals in JS, need to escape backticks and ${ if any
    escaped_html = footer_html.replace('`', '\\`').replace('${', '\\${')
    
    js_content = f"""// Reusable Footer Component
document.addEventListener("DOMContentLoaded", function() {{
    const footerPlaceholder = document.getElementById("la-jiraffa-footer-placeholder");
    if (footerPlaceholder) {{
        footerPlaceholder.innerHTML = `{escaped_html}`;
    }}
}});
"""
    
    os.makedirs(os.path.dirname(footer_js_path), exist_ok=True)
    with open(footer_js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"Created {footer_js_path}")
    
    # Replace in index.html
    new_index_content = index_content.replace(footer_html, '<div id="la-jiraffa-footer-placeholder"></div>\n\t\t<script src="js/footer.js"></script>')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_index_content)
    print("Updated index.html")
    
    # Process contact.html
    with open(contact_path, 'r', encoding='utf-8') as f:
        contact_content = f.read()
    
    contact_footer_match = re.search(r'(<footer class="site-footer style-1">.*?</footer>)', contact_content, re.DOTALL)
    if contact_footer_match:
        contact_footer_html = contact_footer_match.group(1)
        new_contact_content = contact_content.replace(contact_footer_html, '<div id="la-jiraffa-footer-placeholder"></div>\n\t\t<script src="js/footer.js"></script>')
        with open(contact_path, 'w', encoding='utf-8') as f:
            f.write(new_contact_content)
        print("Updated contact.html")
    else:
        print("Footer not found in contact.html")
else:
    print("Footer not found in index.html")
