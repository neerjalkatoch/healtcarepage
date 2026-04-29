import os, re

DIR = os.path.dirname(os.path.abspath(__file__))

# ── The LeadConnector iframe block ──────────────────────────────────────────
IFRAME_BLOCK = '''<div class="w-full" style="min-height:870px;">
    <iframe
        src="https://api.leadconnectorhq.com/widget/form/E9X0wnd5S2qsrjVxJBVV"
        style="width:100%;height:100%;min-height:870px;border:none;border-radius:8px"
        id="inline-E9X0wnd5S2qsrjVxJBVV"
        data-layout="{\'id\':\'INLINE\'}"
        data-trigger-type="alwaysShow"
        data-trigger-value=""
        data-activation-type="alwaysActivated"
        data-activation-value=""
        data-deactivation-type="neverDeactivate"
        data-deactivation-value=""
        data-form-name="Form 5"
        data-height="854"
        data-layout-iframe-id="inline-E9X0wnd5S2qsrjVxJBVV"
        data-form-id="E9X0wnd5S2qsrjVxJBVV"
        title="Form 5">
    </iframe>
    <script src="https://link.msgsndr.com/js/form_embed.js"></script>
</div>'''

# ── The nav Case Studies anchor to remove ───────────────────────────────────
CASE_STUDY_NAV = '<a class="text-slate-600 font-nav-link text-nav-link hover:text-[#6B52C8] transition-colors" href="#case-studies">Case Studies</a>'

html_files = [f for f in os.listdir(DIR) if f.endswith('.html')]

for fname in html_files:
    path = os.path.join(DIR, fname)
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()

    original = content

    # 1. Remove the Case Studies nav link everywhere
    content = content.replace(CASE_STUDY_NAV, '')

    # 2. contact.html – replace the entire <form …>…</form> block inside the
    #    "Contact Form Section" with the iframe.
    if fname == 'contact.html':
        # Replace the whole contact-form section content (header card + form)
        # Pattern: the wrapping card div that starts with bg-primary-container
        content = re.sub(
            r'<div\s+class="bg-primary-container p-12 text-center text-on-primary-container">.*?</form>\s*</div>',
            f'''<div class="bg-primary-container p-12 text-center text-on-primary-container">
                    <h2 class="font-h2 text-h2 mb-2">Book Your Free Strategy Call</h2>
                    <p class="font-body opacity-90">Schedule a consultation with our strategic directors today.</p>
                </div>
                <div class="p-8 md:p-12">
                    {IFRAME_BLOCK}
                </div>''',
            content,
            flags=re.DOTALL
        )

    # 3. service_*.html and index.html – replace the "Final CTA" purple section
    #    (the big rounded card with bg-primary-container that has CTA buttons)
    #    Pattern covers the entire section from <!-- Final CTA --> to </section>
    content = re.sub(
        r'<!--\s*Final CTA\s*-->\s*<section[^>]*>.*?</section>',
        f'''<!-- Final CTA -->
        <section class="max-w-[1200px] mx-auto px-6 py-section-v">
            <div class="bg-primary-container rounded-[32px] p-8 md:p-16 relative overflow-hidden shadow-[0_18px_52px_-15px_rgba(107,82,200,0.3)]">
                <div class="absolute -top-1/2 -right-1/4 w-[600px] h-[600px] bg-white/10 rounded-full blur-[80px]"></div>
                <div class="relative z-10 text-center mb-10">
                    <h2 class="font-h1 text-h1 text-white mb-4">Book Your Free Strategy Call</h2>
                    <p class="font-body text-on-primary-container max-w-xl mx-auto text-lg">Tell us about your business and we\'ll reach out to craft a custom growth plan.</p>
                </div>
                <div class="relative z-10 bg-white rounded-2xl p-2">
                    {IFRAME_BLOCK}
                </div>
            </div>
        </section>''',
        content,
        flags=re.DOTALL
    )

    # 4. index.html – replace the hero CTA buttons pair with the iframe form
    #    The two buttons: "Book Your Free Strategy Call" and "Request CRM Demo"
    if fname == 'index.html':
        content = re.sub(
            r'<div class="flex flex-wrap gap-4 pt-4">\s*<button[^>]*>[\s\S]*?Book Your Free Strategy Call[\s\S]*?</button>\s*<button[^>]*>[\s\S]*?Request CRM Demo[\s\S]*?</button>\s*</div>',
            f'''<div class="pt-4">
                {IFRAME_BLOCK}
            </div>''',
            content,
            flags=re.DOTALL
        )

    if content != original:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f'Updated: {fname}')
    else:
        print(f'No changes: {fname}')

print('Done.')
