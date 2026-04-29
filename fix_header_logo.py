import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

old_header = 'class="h-20 w-auto object-contain scale-125 origin-left brightness-110"'
new_header = 'class="h-16 w-auto object-contain"'

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_header in content:
        content = content.replace(old_header, new_header)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed header logo in: {filename}")

print("Done!")
