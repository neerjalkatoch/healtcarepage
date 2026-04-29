import os, re

DIR = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────
# THE CANONICAL HEADER  (taken from index.html after all edits)
# ─────────────────────────────────────────────────────────────────
CANONICAL_HEADER = """\
<!-- Contact Info Top Bar -->
<div class="w-full bg-[#4A3899] text-white py-2 px-6">
<div class="max-w-[1200px] mx-auto flex justify-between items-center font-body-sm">
<div class="flex items-center gap-6">
<span class="flex items-center gap-2">
<span class="material-symbols-outlined text-sm">mail</span>
                    hello@mdastra.com
                </span>
<span class="flex items-center gap-2">
<span class="material-symbols-outlined text-sm">call</span>
                    +1 (888) 123-4567
                </span>
</div>
<div class="flex items-center gap-4">
<a class="hover:text-secondary-fixed transition-colors" href="#">Client Login</a>
<span class="opacity-30">|</span>
<a class="hover:text-secondary-fixed transition-colors" href="#">Support</a>
</div>
</div>
</div>
<!-- TopNavBar -->
<header class="bg-white/90 backdrop-blur-md sticky top-0 z-50 border-b border-slate-200/50 shadow-[0_18px_52px_-15px_rgba(107,82,200,0.09)]">
<nav class="flex justify-between items-center w-full max-w-[1200px] mx-auto px-6 h-20">
<div class="flex items-center gap-8">
<a class="text-2xl font-bold text-slate-900 font-h1 flex items-center" href="/">
<img alt="MD Astra Logo" class="h-20 md:h-24 w-auto object-contain" src="./assets/logo.png"/>
</a>
</div>
<div class="hidden md:flex items-center gap-8">
<a class="text-slate-600 font-nav-link text-nav-link hover:text-[#6B52C8] transition-colors" href="/">Home</a>
<a class="text-slate-600 font-nav-link text-nav-link hover:text-[#6B52C8] transition-colors" href="aboutus.html">About Us</a>
<div class="relative group">
    <a class="text-slate-600 font-nav-link text-nav-link hover:text-[#6B52C8] transition-colors flex items-center gap-1 cursor-pointer" href="#services">
        Services <span class="material-symbols-outlined text-[16px] group-hover:rotate-180 transition-transform duration-300">expand_more</span>
    </a>
    <div class="absolute top-full left-0 mt-4 w-64 bg-white rounded-lg shadow-[0_18px_52px_-15px_rgba(107,82,200,0.15)] border border-slate-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 flex flex-col overflow-hidden z-50">
        <div class="absolute -top-4 left-0 w-full h-4"></div>
        <a href="service_seo.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Local SEO</a>
        <a href="service_webdev.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Website Development</a>
        <a href="service_gmb.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Google Business Profile</a>
        <a href="service_content.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Content Marketing</a>
        <a href="service_social.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Social Media Marketing</a>
        <a href="service_google_ads.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Google Ads</a>
    </div>
</div>
<div class="relative group">
    <a class="text-slate-600 font-nav-link text-nav-link hover:text-[#6B52C8] transition-colors flex items-center gap-1 cursor-pointer" href="#industries">
        Industries <span class="material-symbols-outlined text-[16px] group-hover:rotate-180 transition-transform duration-300">expand_more</span>
    </a>
    <div class="absolute top-full left-0 mt-4 w-56 bg-white rounded-lg shadow-[0_18px_52px_-15px_rgba(107,82,200,0.15)] border border-slate-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 flex flex-col overflow-hidden z-50">
        <div class="absolute -top-4 left-0 w-full h-4"></div>
        <a href="scratch_ecommerce.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Ecommerce</a>
        <a href="scratch_education.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Education &amp; Coaching</a>
        <a href="scratch_fashion.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Fashion &amp; Lifestyle</a>
        <a href="scratch_healthcare.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Healthcare</a>
        <a href="scratch_legal.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Legal Services</a>
        <a href="scratch_localservice.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Local Services</a>
        <a href="scratch_realestate.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Real Estate</a>
        <a href="scratch_restaurant.html" class="px-4 py-3 text-sm font-nav-link text-slate-600 hover:bg-purple-50 hover:text-[#6B52C8] transition-colors border-b border-slate-50 last:border-0">Restaurants</a>
    </div>
</div>
<a class="text-slate-600 font-nav-link text-nav-link hover:text-[#6B52C8] transition-colors" href="contact.html">Contact Us</a>
</div>
<div class="flex items-center gap-4">
<a href="contact.html" class="bg-[#6B52C8] text-white px-6 py-3 rounded-full font-nav-link text-nav-link hover:opacity-80 active:scale-95 transition-all duration-300 inline-flex items-center justify-center">Get Started</a>
</div>
</nav>
</header>"""

# Regex to match everything from the top bar comment through </header>
# This covers all variants found across pages
HEADER_PATTERN = re.compile(
    r'(?s)<!--\s*Contact Info Top Bar\s*-->.*?</header>',
    re.DOTALL
)

html_files = sorted(f for f in os.listdir(DIR) if f.endswith('.html'))

changed = []
for fname in html_files:
    path = os.path.join(DIR, fname)
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()

    original = content

    # 1. Replace the entire header block with the canonical one
    content, n_header = HEADER_PATTERN.subn(CANONICAL_HEADER, content, count=1)

    # 2. Replace "Common Inquiries" with "FAQ" (case-insensitive, all forms)
    content = re.sub(r'Common Inquiries', 'FAQ', content, flags=re.IGNORECASE)

    # 3. Also catch any stray Case Studies links that may remain
    content = re.sub(
        r'<a[^>]+href="#case-studies"[^>]*>Case Studies</a>\s*',
        '',
        content,
        flags=re.IGNORECASE
    )

    if content != original:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(content)
        changed.append(fname)
        print(f'  Updated ({n_header} header swap): {fname}')
    else:
        print(f'  No change: {fname}')

print(f'\nDone. {len(changed)} file(s) updated.')
