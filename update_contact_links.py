import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update header link
    content = content.replace('href="#contact">Contact Us</a>', 'href="contact.html">Contact Us</a>')
    
    # Update footer link
    content = content.replace('href="#">Contact Us</a>', 'href="contact.html">Contact Us</a>')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all contact links!")
