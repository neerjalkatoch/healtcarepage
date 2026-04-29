import os
import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract Top Bar + Header
header_match = re.search(r'(<!-- Contact Info Top Bar -->.*?</header>)', index_content, re.DOTALL)
if not header_match:
    print("Could not find header in index.html")
    exit(1)
new_header = header_match.group(1)

# Extract Footer
footer_match = re.search(r'(<!-- Footer -->\s*<footer.*?</footer>)', index_content, re.DOTALL)
if not footer_match:
    print("Could not find footer in index.html")
    exit(1)
new_footer = footer_match.group(1)

# Function to update file
def update_file(filename, is_service=False):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Header
    if is_service:
        # service files have <nav class="fixed top-0 ..."> ... </nav> right after <body>
        content = re.sub(r'<!-- TopNavBar Shell -->\s*<nav.*?</nav>', new_header, content, flags=re.DOTALL)
        # also some files might just have <nav ...> without TopNavBar Shell
        content = re.sub(r'(<body.*?>\s*)<nav.*?</nav>', r'\1' + new_header, content, flags=re.DOTALL)
    else:
        # scratch files already have <!-- Contact Info Top Bar --> ... </header> or <header> ... </header>
        content = re.sub(r'<!-- Contact Info Top Bar -->.*?</header>', new_header, content, flags=re.DOTALL)
        
    # Update Footer
    content = re.sub(r'<!-- Footer -->\s*<footer.*?</footer>', new_footer, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

for f in html_files:
    update_file(f, f.startswith('service_'))

print("Done!")
