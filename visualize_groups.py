import os
import re

work_dir = r"C:\Users\M ROSIFUL AQLI\medalis-live-preview"

groups = {
    "Navbar Publik (Landing & Harga)": [
        "landing-terang.html", "landing-gelap.html",
        "pricing-terang.html", "pricing-gelap.html"
    ],
    "Navbar Dashboard (Beranda | Modul | Tryout | Guru AI | Timeline)": [
        "dashboard-terang.html", "dashboard-gelap.html",
        "daftar-modul-terang.html", "daftar-modul-gelap.html",
        "ebook-reader-terang.html", "ebook-reader-gelap.html",
        "lobby-tryout-terang.html", "lobby-tryout-gelap.html",
        "guru-ai-terang.html", "guru-ai-gelap.html",
        "prep-timeline-terang.html", "prep-timeline-gelap.html",
        "hasil-tryout-terang.html", "hasil-tryout-gelap.html",
        "pembahasan-terang.html", "pembahasan-gelap.html",
        "state-anti-cheat-terang.html", "state-anti-cheat-gelap.html",
        "state-offline-terang.html", "state-offline-gelap.html",
        "state-empty-terang.html", "state-empty-gelap.html",
        "state-404-terang.html", "state-404-gelap.html",
        "early-learner-tk-terang.html", "early-learner-tk-gelap.html"
    ],
    "Navbar Kompleks (Laporan WhatsApp)": [
        "laporan-whatsapp-terang.html", "laporan-whatsapp-gelap.html"
    ]
}

for group_name, files in groups.items():
    print(f"\n{'='*70}")
    print(f"GRUP: {group_name}")
    print(f"{'='*70}")
    for f in files:
        p = os.path.join(work_dir, f)
        with open(p, "r", encoding="utf-8") as fp:
            html = fp.read()
        
        header_match = re.search(r"<header[^>]*>(.*?)</header>", html, re.S)
        if header_match:
            hdr = header_match.group(0)
            h_classes = re.search(r'class="([^"]*)"', hdr)
            hor = "No class" if not h_classes else h_classes.group(1)
            print(f"\n[{f}]")
            print(f"  Header classes: {hor[:80]}")
            
            nav_links = re.findall(r"<a[^>]*>(.*?)</a>", hdr, re.S)
            clean_links = []
            for link in nav_links:
                clean = " ".join(re.sub(r"<[^>]+>", " ", link).split()).strip()
                if clean and len(clean) > 1:
                    clean_links.append(clean)
            if clean_links:
                print(f"  Menu Nav: {' | '.join(clean_links[:8])}")
            else:
                print(f"  Menu Nav: [KOSONG / TIDAK ADA NAV]")
        else:
            print(f"\n[{f}]")
            print(f"  STATUS: TIDAK ADA <header>")
