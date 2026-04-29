import os
import re

# Read index.html to get the correct header and footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

header_match = re.search(r'(<!-- Contact Info Top Bar -->.*?</header>)', index_content, re.DOTALL)
new_header = header_match.group(1) if header_match else ""

footer_match = re.search(r'(<!-- Footer -->\s*<footer.*?</footer>)', index_content, re.DOTALL)
new_footer = footer_match.group(1) if footer_match else ""

for filename in os.listdir('.'):
    if not filename.endswith('.html') or filename == 'index.html':
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove ALL duplicated Contact Info Top Bars and TopNavBar Shells and headers/navs up to <main
    # We will just find <body ...> and <main and replace EVERYTHING in between with new_header
    # Wait, some files don't have <main>, they have <main> right after header.
    # Let's replace from <body... > to <main...>
    
    body_match = re.search(r'(<body[^>]*>)(.*?)<main', content, re.DOTALL)
    if body_match:
        body_tag = body_match.group(1)
        # Put new_header right after body_tag
        content = re.sub(r'(<body[^>]*>).*?<main', body_tag + '\n    ' + new_header + '\n    <main', content, flags=re.DOTALL)
    else:
        print(f"Could not find <main> in {filename}")

    # Now fix footer: replace everything from <!-- Footer --> or <footer to </body>
    # Wait, some might have multiple footers if duplicated
    footer_match = re.search(r'(<!-- Footer -->|<footer[^>]*>).*?(</body>)', content, re.DOTALL)
    if footer_match:
        content = re.sub(r'(<!-- Footer -->|<footer[^>]*>).*?(</body>)', new_footer + '\n' + r'\2', content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {filename}")

