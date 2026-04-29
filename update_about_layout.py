import re

# Read index.html to get the correct header and footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

header_match = re.search(r'(<!-- Contact Info Top Bar -->.*?</header>)', index_content, re.DOTALL)
new_header = header_match.group(1) if header_match else ""

footer_match = re.search(r'(<!-- Footer -->\s*<footer.*?</footer>)', index_content, re.DOTALL)
new_footer = footer_match.group(1) if footer_match else ""

# Update aboutus.html
with open('aboutus.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <nav>
content = re.sub(r'<!-- TopNavBar -->\s*<nav.*?</nav>', new_header, content, flags=re.DOTALL)

# Replace <footer>
content = re.sub(r'<!-- Footer -->\s*<footer.*?</footer>', new_footer, content, flags=re.DOTALL)

with open('aboutus.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated aboutus.html layout")

