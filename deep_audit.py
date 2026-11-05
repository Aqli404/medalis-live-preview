import os
import re

work_dir = r"C:\Users\M ROSIFUL AQLI\medalis-live-preview"
files = [
    "landing-terang.html", "landing-gelap.html",
    "dashboard-terang.html", "dashboard-gelap.html",
    "daftar-modul-terang.html", "daftar-modul-gelap.html",
    "lobby-tryout-terang.html", "lobby-tryout-gelap.html",
    "lembar-tryout-terang.html", "lembar-tryout-gelap.html",
    "hasil-tryout-terang.html", "hasil-tryout-gelap.html",
    "pembahasan-terang.html", "pembahasan-gelap.html",
    "guru-ai-terang.html", "guru-ai-gelap.html",
    "prep-timeline-terang.html", "prep-timeline-gelap.html",
    "pricing-terang.html", "pricing-gelap.html",
    "early-learner-tk-terang.html", "early-learner-tk-gelap.html",
    "laporan-whatsapp-terang.html", "laporan-whatsapp-gelap.html"
]

for f in files:
    p = os.path.join(work_dir, f)
    with open(p, "r", encoding="utf-8") as fp:
        html = fp.read()
    m = re.search(r"<header[^>]*>.*?</header>", html, re.S)
    print(f"=== {f} ===")
    if m:
        hdr = m.group(0)
        h_tag = re.search(r"<header[^>]*>", hdr).group(0)
        print("  Header Tag:", h_tag)
        # Search active links
        links = re.findall(r'<a([^>]*)>(.*?)</a>', hdr, re.S)
        for attrs, text in links:
            clean_t = " ".join(re.sub(r'<[^>]+>', ' ', text).split()).strip()
            is_active = ('aria-current="page"' in attrs or 
                         'bg-primary' in attrs or 
                         'bg-[#D4A747]' in attrs or 
                         'bg-[#0B1E3A]' in attrs or 
                         'bg-surface' in attrs or 
                         'font-bold' in attrs or 
                         'font-semibold' in attrs)
            if is_active and clean_t in ['Beranda', 'Modul', 'Tryout', 'Guru AI', 'Timeline', 'Fitur Utama', 'Solusi', 'Kurikulum', 'Harga', 'FAQ', 'Harga']:
                print(f"    * NAV LINK: {clean_t:20s} [ACTIVE/HIGHLIGHTED]")
            elif clean_t in ['Beranda', 'Modul', 'Tryout', 'Guru AI', 'Timeline', 'Fitur Utama', 'Solusi', 'Kurikulum', 'Harga', 'FAQ']:
                print(f"    * NAV LINK: {clean_t:20s} [inactive]")
    else:
        print("  NO HEADER")
