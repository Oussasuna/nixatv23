import re

files_to_update = ['index.html', 'setup.html']

for filename in files_to_update:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace <a href="https://wa.me/... " with <a target="_blank" href="https://wa.me/... "
    # Make sure we don't double add it if it's already there
    # It's easier to just do a regex replace
    content = re.sub(r'<a ([^>]*)href="(https://wa\.me/[^"]+)"([^>]*)>', r'<a \1href="\2" target="_blank"\3>', content)
    
    # Remove duplicates just in case
    content = content.replace('target="_blank" target="_blank"', 'target="_blank"')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added target='_blank' to all wa.me links.")
