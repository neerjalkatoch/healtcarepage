import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Header logo replacement
header_logo_old = r'<img alt="MD Astra Logo" class="h-14 w-auto object-contain" src="./assets/logo.png"/>'
header_logo_new = r'<img alt="MD Astra Logo" class="h-20 w-auto object-contain scale-125 origin-left brightness-110" src="./assets/logo.png"/>'

# Footer logo replacement
footer_logo_pattern = r'<div class="flex items-center gap-2">\s*<img alt="Logo Footer".*?/>\s*<span class="font-h2 text-xl font-bold text-slate-900">MD Astra</span>\s*</div>'
footer_logo_new = r'''<div class="flex items-center gap-2">
<img alt="MD Astra Logo Footer" class="h-16 w-auto object-contain brightness-110 grayscale hover:grayscale-0 transition-all duration-300" src="./assets/logo.png"/>
</div>'''

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update header
    content = content.replace(header_logo_old, header_logo_new)
    
    # Update footer
    content = re.sub(footer_logo_pattern, footer_logo_new, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated logos across all pages")
