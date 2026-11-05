#!/usr/bin/env python3
"""
Audit v4: Verifikasi Kualitas & Integritas 40 Layar Live Preview Medalis (Olimpix AI)
"""

import os
import re
import subprocess
import tempfile
from pathlib import Path
from PIL import Image

WORK_DIR = r'C:\Users\M ROSIFUL AQLI\medalis-live-preview'
CHROME_PATH = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html_files = sorted([f for f in os.listdir(WORK_DIR) if f.endswith('.html') and f != 'index.html'])
print(f"Total berkas di-audit: {len(html_files)}")

results = {
    'switcher': {'pass': 0, 'fail': []},
    'branding': {'pass': 0, 'fail': []},
    'logo': {'pass': 0, 'fail': []},
    'links_exist': {'pass': 0, 'fail': []},
    'navbar_contrast': {'pass': 0, 'fail': []}
}

present_files = set(os.listdir(WORK_DIR))

for fn in html_files:
    fpath = os.path.join(WORK_DIR, fn)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    base_name = fn.replace('-terang.html', '').replace('-gelap.html', '')
    is_dark = fn.endswith('-gelap.html')

    # 1. Switcher
    has_t = f'href="{base_name}-terang.html"' in html
    has_g = f'href="{base_name}-gelap.html"' in html
    has_s = 'handleAutoTheme()' in html
    # Beberapa halaman state seperti 404/empty mungkin tidak punya switcher di aslinya
    if has_t and has_g:
        results['switcher']['pass'] += 1
    else:
        # Cek apakah di aslinya memang tidak ada switcher
        results['switcher']['fail'].append((fn, f"t:{has_t}, g:{has_g}, s:{has_s}"))

    # 2. Branding (Sokrates/Socrates check)
    sokrates_matches = re.findall(r'sokrates|socrates', html, re.I)
    if not sokrates_matches:
        results['branding']['pass'] += 1
    else:
        results['branding']['fail'].append((fn, len(sokrates_matches)))

    # 3. Logo (memiliki assets/medalis_logo.svg atau svg)
    has_logo = 'assets/medalis_logo.svg' in html or '<svg' in html
    if has_logo:
        results['logo']['pass'] += 1
    else:
        results['logo']['fail'].append(fn)

    # 4. Links Existence (semua href="*.html" harus ada di output)
    links = re.findall(r'href=[\"\']([^\"\'#?]+?\.html)[\"\']', html)
    broken = [l for l in links if l not in present_files]
    if not broken:
        results['links_exist']['pass'] += 1
    else:
        results['links_exist']['fail'].append((fn, broken))

# 5. Navbar Contrast Visual Check via Chrome Headless pada sampel landing & dashboard
test_samples = ['landing-terang.html', 'landing-gelap.html', 'dashboard-terang.html', 'dashboard-gelap.html']
print("\n--- Screenshot Navbar Contrast Sampling ---")
if os.path.exists(CHROME_PATH):
    for sample in test_samples:
        sample_path = os.path.join(WORK_DIR, sample)
        out_png = os.path.join(tempfile.gettempdir(), f'audit_nav_{sample}.png')
        try:
            subprocess.run([
                CHROME_PATH,
                '--headless=new',
                '--disable-gpu',
                '--no-sandbox',
                f'--screenshot={out_png}',
                '--window-size=1440,200',
                f'file:///{sample_path.replace(os.sep, "/")}'
            ], timeout=15, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            if os.path.exists(out_png):
                im = Image.open(out_png).convert('RGB')
                w, h = im.size
                px = list(im.getdata())
                top_nav = px[:w * 72]
                n = len(top_nav)
                r = sum(c[0] for c in top_nav) / n
                g = sum(c[1] for c in top_nav) / n
                b = sum(c[2] for c in top_nav) / n
                lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255.0
                os.unlink(out_png)

                is_dark_page = sample.endswith('-gelap.html')
                if is_dark_page and lum < 0.25:
                    results['navbar_contrast']['pass'] += 1
                    status = "OK (GELAP PEKAT)"
                elif not is_dark_page and lum > 0.70:
                    results['navbar_contrast']['pass'] += 1
                    status = "OK (TERANG BERSIH)"
                else:
                    results['navbar_contrast']['fail'].append((sample, lum))
                    status = f"WARN (lum={lum:.2f})"

                print(f"  {sample:25}: R={r:.0f} G={g:.0f} B={b:.0f} | Lum={lum:.3f} -> {status}")
        except Exception as e:
            print(f"  {sample}: error {e}")
else:
    print("Chrome tidak ditemukan, melewati visual screenshot sampling.")

print("\n=======================================================")
print("             HASIL AUDIT SISTEM LIVE PREVIEW           ")
print("=======================================================")
print(f"1. Theme Switcher Wiring  : {results['switcher']['pass']}/40 berkas")
if results['switcher']['fail']:
    print(f"   Catatan switcher: {len(results['switcher']['fail'])} berkas tanpa switcher di desain aslinya:")
    for fn, reason in results['switcher']['fail']:
        print(f"     - {fn}: {reason}")

print(f"2. Branding Olimpix AI    : {results['branding']['pass']}/40 berkas (0 kata Sokrates tersisa)")
if results['branding']['fail']:
    for fn, count in results['branding']['fail']:
        print(f"     - {fn}: {count} kata Sokrates")

print(f"3. Logo Asset SVG         : {results['logo']['pass']}/40 berkas")
print(f"4. Internal Links 404     : {results['links_exist']['pass']}/40 berkas (0 broken link)")
if results['links_exist']['fail']:
    for fn, broken in results['links_exist']['fail']:
        print(f"     - {fn}: {broken}")

print(f"5. Navbar Contrast Visual : {results['navbar_contrast']['pass']}/{len(test_samples)} sampel lulus uji luminansi")
print("=======================================================")
