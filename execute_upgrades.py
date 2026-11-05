#!/usr/bin/env python3
import os
import re
import glob
import navbars
import patch_landing
import past_papers
import calendar_section

WORK_DIR = "/root/medalis-live-preview"
os.chdir(WORK_DIR)

files = glob.glob("*.html")
print(f"Total HTML files detected: {len(files)}")

# 1. Klasifikasi file HTML ke tipe navbar yang sesuai
PUBLIC_PAGES = ["landing", "pricing", "login", "onboarding", "laporan-whatsapp"]
EXAM_PAGES = ["lembar-tryout"]
STUDENT_PAGES = [
    "dashboard", "daftar-modul", "prep-timeline", "lobby-tryout",
    "guru-ai", "ebook-reader", "hasil-tryout", "pembahasan",
    "early-learner-tk", "tk-menara-balok", "state-anti-cheat",
    "state-offline", "state-empty", "state-404"
]

def replace_header(html, new_header):
    # Regex replace existing <header>...</header>
    if "<header" in html and "</header>" in html:
        return re.sub(r'<header\b[^>]*?>.*?</header>', new_header, html, count=1, flags=re.S)
    else:
        # Jika belum ada header, pasang tepat setelah <body>
        return re.sub(r'(<body\b[^>]*?>)', r'\1\n' + new_header, html, count=1, flags=re.I)

def ensure_safe_area_mobile(html):
    # Tambahkan padding bawah di main agar tidak tertutup mobile bottom nav
    if 'pb-20' not in html and 'pb-24' not in html:
        html = re.sub(r'(<main\b[^>]*?class=[\"\'][^\"\']*?)(\")|(<main\b)', r'\1 pb-24 lg:pb-8\2', html, count=1)
    # Tambahkan overflow-x: hidden di body
    html = re.sub(r'(<body\b[^>]*?class=[\"\'][^\"\']*?)(\")', r'\1 overflow-x-hidden\2', html, count=1)
    return html

def clean_ai_words(html):
    # Bersihkan sisa kata "Olimpix AI", "Guru AI"
    html = re.sub(r'Olimpix\s+AI\s*\(Bukan\s+Mentor\s+Manusia\)', 'Tutor Penalaran Interaktif (Olimpix Engine)', html, flags=re.I)
    html = re.sub(r'Bukan\s+Mentor\s+Manusia', 'Tutor Penalaran Interaktif', html, flags=re.I)
    html = re.sub(r'Olimpix\s+AI', 'Olimpix Engine', html)
    html = re.sub(r'Guru\s+AI', 'Tutor Olimpix', html)
    html = re.sub(r'Guru\s+Sokrates', 'Tutor Olimpix', html, flags=re.I)
    html = re.sub(r'Sokrates\s+AI', 'Olimpix Engine', html, flags=re.I)
    return html

for fname in files:
    is_dark = fname.endswith("-gelap.html")
    base_name = fname.replace("-gelap.html", "").replace("-terang.html", "").replace(".html", "")
    
    with open(fname, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # A. Inject & Standardize Navbar
    if base_name in PUBLIC_PAGES:
        nav = navbars.get_public_navbar(is_dark=is_dark)
        html = replace_header(html, nav)
    elif base_name in EXAM_PAGES:
        nav = navbars.get_exam_navbar(is_dark=is_dark)
        html = replace_header(html, nav)
    else:
        nav = navbars.get_student_navbar(base_name, is_dark=is_dark)
        html = replace_header(html, nav)

    # B. Mobile-Friendly Fixes
    html = ensure_safe_area_mobile(html)

    # C. Bersihkan Kata AI & Reposisi Branding
    html = clean_ai_words(html)

    # D. Custom Page Injections
    if base_name == "landing":
        html = patch_landing.update_landing_content(html, is_dark=is_dark)

    if base_name == "daftar-modul":
        # Sisipkan seksi Past Papers jika belum ada
        if "Koleksi Past Papers Olimpiade" not in html:
            past_papers_html = past_papers.get_past_papers_section(is_dark=is_dark)
            # Pasang di bawah filter section atau di dalam main
            if "</section>" in html:
                # Sisipkan setelah section filter ketiga
                parts = html.split("</section>")
                if len(parts) >= 3:
                    html = "</section>".join(parts[:3]) + "</section>\n" + past_papers_html + "\n" + "</section>".join(parts[3:])
                else:
                    html = re.sub(r'(</main>)', past_papers_html + r'\n\1', html, count=1)
            else:
                html = re.sub(r'(</main>)', past_papers_html + r'\n\1', html, count=1)

    if base_name == "prep-timeline":
        # Ganti isi timeline lama dengan Kalender Lomba Terpadu
        cal_html = calendar_section.get_calendar_section(is_dark=is_dark)
        # Ganti content di dalam <main>...</main>
        html = re.sub(r'(<main\b[^>]*?>).*?(</main>)', r'\1\n' + cal_html + r'\n\2', html, flags=re.S)

    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"[OK] {fname} upgraded successfully.")

print("All HTML files upgraded.")
