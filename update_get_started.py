import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

button_pattern = r'<button class="bg-\[#6B52C8\] text-white px-6 py-3 rounded-full font-nav-link text-nav-link hover:opacity-80 active:scale-95 transition-all duration-300">\s*Get Started\s*</button>'
anchor_replacement = '<a href="contact.html" class="bg-[#6B52C8] text-white px-6 py-3 rounded-full font-nav-link text-nav-link hover:opacity-80 active:scale-95 transition-all duration-300 inline-flex items-center justify-center">Get Started</a>'

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if re.search(button_pattern, content):
        content = re.sub(button_pattern, anchor_replacement, content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
        
