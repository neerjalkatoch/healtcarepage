import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Replace the text-only "MD Astra" in the footer with the actual logo image
# Pattern 1: The main footer section with text "MD Astra"
old_footer_brand = '<div class="text-xl font-bold text-slate-900 font-h1">MD Astra</div>'
new_footer_brand = '''<a href="/" class="flex items-center gap-3">
<img alt="MD Astra Logo" class="h-14 w-auto object-contain" src="./assets/logo.png"/>
</a>'''

count = 0
for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False
    
    # Update footer brand text to logo
    if old_footer_brand in content:
        content = content.replace(old_footer_brand, new_footer_brand)
        changed = True
    
    if changed:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated footer logo in: {filename}")

print(f"\nTotal files updated: {count}")
