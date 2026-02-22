import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The broken string looks like:
# data-text="s:14;l:17;fw:400,500,500,400;" data-actions='o:click;a:simplelink;target:_self;url:javascript:void(0);https://
# followed by the next line. 
# We just need to replace "url:javascript:void(0);https://" with "url:javascript:void(0);'"

content, count = re.subn(r'url:javascript:void\(0\);https://(\n|\r\n)?', r"url:javascript:void(0);'\g<1>", content)
print(f"Fixed {count} instances.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
