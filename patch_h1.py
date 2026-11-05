import re

for fname in ["landing-terang.html", "landing-gelap.html"]:
    with open(fname, "r", encoding="utf-8") as f:
        html = f.read()

    is_dark = fname.endswith("-gelap.html")
    text_color = "text-white" if is_dark else "text-[#0B1E3A]"

    # Ganti H1 Stitch
    new_h1 = f'''<h1 class="font-headline-xl text-3xl sm:text-4xl lg:text-[50px] font-extrabold {text_color} tracking-tight leading-[1.15] mb-4">
BIMBINGAN INTENSIF & SIMULASI CBT<br>
<span class="text-[#D4A747]">MENUJU PODIUM EMAS OLIMPIADE</span>
</h1>'''

    html = re.sub(
        r'<h1 class="font-headline-xl[^>]*?>.*?</h1>',
        new_h1,
        html,
        count=1,
        flags=re.S
    )

    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"H1 patched in {fname}")
