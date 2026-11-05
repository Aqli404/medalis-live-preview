#!/usr/bin/env python3
"""
Builder v4: Mengonversi 20 Layar Ekspor Google Stitch (Zip 4) Menjadi Live Preview
Prinsip:
1. Mempertahankan 100% desain, struktur HTML, dan styling asli per layar (TIDAK Mendesain Ulang).
2. Menghubungkan seluruh UX (Routing, CTA, Navigasi data-path, Theme Switcher) tanpa bug.
3. Branding Olimpix AI menyeluruh (menggantikan Sokrates).
4. Asset lokal logo SVG dan robot avatar Olimpix AI.
"""

import os
import re
import shutil
from pathlib import Path

# Paths
V4_BASE = r'C:\Users\M ROSIFUL AQLI\Downloads\medalis_stitch_v4\stitch_proyek_medalis_web_dan_apps'
WORK_DIR = r'C:\Users\M ROSIFUL AQLI\medalis-live-preview'
ASSETS_DIR = os.path.join(WORK_DIR, 'assets')
LOGO_SVG_SRC = r'C:\Users\M ROSIFUL AQLI\Downloads\medalis_logo_m.svg'

os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. Pastikan aset lokal siap
logo_svg_dst = os.path.join(ASSETS_DIR, 'medalis_logo.svg')
if os.path.exists(LOGO_SVG_SRC):
    shutil.copy2(LOGO_SVG_SRC, logo_svg_dst)
    print(f"[ASSET] medalis_logo.svg disalin ({os.path.getsize(logo_svg_dst)} bytes)")

avatar_dst = os.path.join(ASSETS_DIR, 'olimpix_ai_avatar.png')
print(f"[ASSET] olimpix_ai_avatar.png siap ({os.path.getsize(avatar_dst) if os.path.exists(avatar_dst) else 0} bytes)")

# 2. Pemetaan 20 Pasang Layar Terang & Gelap dari Zip 4
PAIRS = [
    ('landing',          'landing_page_terang_1',                    'landing_page_gelap_4'),
    ('login',            'login_terang_2',                           'login_gelap'),
    ('onboarding',       'onboarding_terang',                        'onboarding_gelap'),
    ('dashboard',        'dashboard_siswa_terang_3',                 'dashboard_siswa_gelap_4'),
    ('daftar-modul',     'daftar_modul_terang_2',                    'daftar_modul_gelap_3'),
    ('ebook-reader',     'ebook_reader_terang_3',                    'ebook_reader_gelap_4'),
    ('lobby-tryout',     'lobby_tryout_terang_3',                    'lobby_tryout_gelap_3'),
    ('lembar-tryout',    'tryout_ksnr_matematika_smp_terang',        'tryout_ksnr_matematika_smp_gelap'),
    ('hasil-tryout',     'hasil_tryout_terang_2',                    'hasil_tryout_gelap_2'),
    ('pembahasan',       'pembahasan_terang_2',                      'pembahasan_gelap_3'),
    ('guru-ai',          'guru_ai_sokrates_terang_3',                'guru_ai_sokrates_gelap_2'),
    ('prep-timeline',    'prep_timeline_terang',                     'prep_timeline_gelap_2'),
    ('pricing',          'pricing_terang_2',                         'pricing_gelap_3'),
    ('early-learner-tk', 'early_learner_tk_terang_3',                'early_learner_tk_gelap_2'),
    ('tk-menara-balok',  'early_learner_tk_menara_balok_terang_3',   'early_learner_tk_menara_balok_gelap_4'),
    ('laporan-whatsapp', 'laporan_whatsapp_terang_2',                'laporan_whatsapp_gelap'),
    ('state-anti-cheat', 'state_peringatan_anti_cheat_terang_2',     'state_peringatan_anti_cheat_gelap_2'),
    ('state-offline',    'state_mode_offline_terang_3',              'state_mode_offline_gelap_2'),
    ('state-empty',      'state_empty_state_terang_2',               'state_empty_state_gelap'),
    ('state-404',        'state_halaman_404_terang_8',               'state_halaman_404_gelap_2'),
]

def clean_btn_text(inner_html):
    t = re.sub(r'<span[^>]*material-symbols-outlined[^>]*>.*?</span>', '', inner_html, flags=re.I|re.S)
    t = re.sub(r'<svg[^>]*>.*?</svg>', '', t, flags=re.I|re.S)
    t = ' '.join(re.sub(r'<[^>]+>', ' ', t).split()).strip().lower()
    return t

def transform_file(base_name, theme, src_folder):
    is_dark = (theme == 'gelap')
    theme_suffix = '-gelap.html' if is_dark else '-terang.html'
    target_filename = f"{base_name}{theme_suffix}"
    src_path = os.path.join(V4_BASE, src_folder, 'code.html')

    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Source file missing: {src_path}")

    with open(src_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # --- 1. SUNTIKKAN INTERAKTIF CSS & JS ---
    if 'medalis_interactive.css' not in html:
        html = re.sub(r'</head>', '  <link rel="stylesheet" href="assets/medalis_interactive.css">\n</head>', html, count=1, flags=re.I)
    if 'medalis_interactive.js' not in html:
        html = re.sub(r'</body>', '  <script src="assets/medalis_interactive.js"></script>\n</body>', html, count=1, flags=re.I)

    # --- 2. LOGO WIRING (TIDAK MERUBAH LAYOUT, HANYA ARAHKAN SRC & ANCHOR) ---
    # Arahkan logo image ke assets/medalis_logo.svg lokal
    html = re.sub(r'(<img[^>]*?alt=[\"\']medalis_logo_transparent\.png[\"\'][^>]*?)src=[\"\'][^\"\']*?[\"\']',
                  r'\1src="assets/medalis_logo.svg"', html)
    html = re.sub(r'(<img[^>]*?src=[\"\'][^\"\']*?[\"\'][^>]*?)alt=[\"\']medalis_logo_transparent\.png[\"\']',
                  r'\1alt="medalis_logo_transparent.png" src="assets/medalis_logo.svg"', html)
    html = re.sub(r'(<img[^>]*?alt=[\"\']Logo Medalis[\"\'][^>]*?)src=[\"\'][^\"\']*?[\"\']',
                  r'\1src="assets/medalis_logo.svg"', html)
    html = re.sub(r'(<img[^>]*?alt=[\"\']Medalis Logo[\"\'][^>]*?)src=[\"\'][^\"\']*?[\"\']',
                  r'\1src="assets/medalis_logo.svg"', html)

    # Wire logo link
    logo_target = f"landing{theme_suffix}" if base_name in ('landing', 'login', 'onboarding') else f"dashboard{theme_suffix}"
    
    # Bungkus atau update logo anchor jika ada di header
    # Jika sudah di dalam <a ...>
    def repl_logo_a(m):
        full = m.group(0)
        return re.sub(r'href=[\"\'][^\"\']*?[\"\']', f'href="{logo_target}"', full)

    html = re.sub(r'<a\b[^>]*?>\s*(?:<img[^>]*?assets/medalis_logo\.svg[^>]*?>|<div[^>]*?>\s*<img[^>]*?assets/medalis_logo\.svg[^>]*?>).*?</a>', repl_logo_a, html, flags=re.S)

    # Jika logo ada di dalam <div> shrink-0 yang belum dibungkus <a>
    def wrap_logo_div(m):
        full = m.group(0)
        return f'<a href="{logo_target}" style="text-decoration:none;" class="flex items-center shrink-0">{full}</a>'

    html = re.sub(r'(<div class="flex items-center[^\"]*?shrink-0">\s*<img[^>]*?assets/medalis_logo\.svg[^>]*?>\s*<span[^>]*?>MEDALIS</span>\s*</div>)', wrap_logo_div, html, flags=re.S)

    # --- 3. THEME SWITCHER WIRING (KONVERSI TOMBOL MENJADI LINK AKTIF DENGAN KELAS ASLI) ---
    def repl_theme_button(m):
        full = m.group(0)
        attrs = m.group(1)
        inner = m.group(2)
        txt = re.sub(r'<[^>]+>', ' ', inner).strip().lower()
        words = txt.split()
        if not words:
            return full
        last_word = words[-1]
        if last_word not in ('terang', 'gelap', 'sistem', 'auto'):
            return full

        clean_attrs = re.sub(r'\s*type=[\"\']button[\"\']', '', attrs)
        clean_attrs = re.sub(r'\s*href=[\"\'][^\"\']*?[\"\']', '', clean_attrs)
        if last_word == 'terang':
            return f'<a href="{base_name}-terang.html"{clean_attrs} style="text-decoration:none;">{inner}</a>'
        elif last_word == 'gelap':
            return f'<a href="{base_name}-gelap.html"{clean_attrs} style="text-decoration:none;">{inner}</a>'
        elif last_word in ('sistem', 'auto'):
            return f'<a href="javascript:void(0)" onclick="handleAutoTheme()"{clean_attrs} style="text-decoration:none; cursor:pointer;" title="Ikuti tema sistem OS">{inner}</a>'
        return full

    html = re.sub(r'<button\b([^>]*?)>(.*?)</button>', repl_theme_button, html, flags=re.S)

    # Unhide switcher jika ada hidden xl:flex / hidden md:flex pada container switcher
    # Hanya pada kontainer yang berisi Terang/Gelap
    def unhide_switcher(m):
        block = m.group(0)
        if 'Terang' in block and 'Gelap' in block:
            block = re.sub(r'\bhidden\s+(?:xl|md|lg):flex\b', 'flex', block)
        return block

    html = re.sub(r'<div[^>]*class="[^"]*?(?:hidden\s+(?:xl|md|lg):flex)[^"]*?"[^>]*>.*?</div>', unhide_switcher, html, flags=re.S)

    # --- 4. NAVIGASI HEADER DATA-PATH WIRING ---
    def repl_datapath(m):
        tag = m.group(1)
        attrs = m.group(2)
        inner = m.group(3)
        path_m = re.search(r'data-path=[\"\']([^\"\']+)[\"\']', attrs)
        if not path_m:
            return m.group(0)
        path = path_m.group(1).lower()

        target = None
        if path in ('fitur-utama', 'fitur'):
            target = '#fitur'
        elif path == 'solusi':
            target = '#solusi'
        elif path == 'kurikulum':
            target = f'daftar-modul{theme_suffix}'
        elif path == 'harga':
            target = f'pricing{theme_suffix}'
        elif path == 'faq':
            target = '#faq'
        elif path in ('login', 'masuk'):
            target = f'login{theme_suffix}'
        elif path in ('daftar', 'coba-gratis'):
            target = f'login{theme_suffix}'
        elif path == 'beranda':
            target = f'dashboard{theme_suffix}'
        elif path == 'modul':
            target = f'daftar-modul{theme_suffix}'
        elif path == 'tryout':
            target = f'lobby-tryout{theme_suffix}'
        elif 'guru-ai' in path or 'olimpix' in path:
            target = f'guru-ai{theme_suffix}'
        elif path == 'timeline':
            target = f'prep-timeline{theme_suffix}'

        if target:
            clean_attrs = re.sub(r'href=[\"\'][^\"\']*?[\"\']', f'href="{target}"', attrs)
            if 'href=' not in clean_attrs:
                clean_attrs = f' href="{target}"' + clean_attrs
            return f'<{tag}{clean_attrs}>{inner}</{tag}>'
        return m.group(0)

    html = re.sub(r'<(a|button)\b([^>]*?data-path=[^>]*?)>(.*?)</\1>', repl_datapath, html, flags=re.S)

    # --- 5. GLOBAL BUTTON & LINK WIRING BERDASARKAN TEKS ---
    def repl_links(m):
        tag = m.group(1)
        attrs = m.group(2)
        inner = m.group(3)

        # Jangan ganggu tombol switcher yang baru dikonversi
        if f'{base_name}-terang.html' in attrs or f'{base_name}-gelap.html' in attrs or 'handleAutoTheme()' in attrs:
            return m.group(0)
        # Jangan ganggu logo
        if 'assets/medalis_logo.svg' in inner:
            return m.group(0)

        t = clean_btn_text(inner)
        if not t or len(t) > 65:
            return m.group(0)

        target_url = None

        if base_name == 'landing':
            if t == 'fitur utama':
                target_url = '#fitur'
            elif t == 'solusi':
                target_url = '#solusi'
            elif t == 'kurikulum':
                target_url = f'daftar-modul{theme_suffix}'
            elif t == 'harga':
                target_url = f'pricing{theme_suffix}'
            elif t == 'faq':
                target_url = '#faq'
            elif 'lihat cara kerjanya' in t:
                target_url = '#fitur'

        if base_name == 'laporan-whatsapp':
            if t == 'kurikulum':
                target_url = f'daftar-modul{theme_suffix}'
            elif t == 'harga':
                target_url = f'pricing{theme_suffix}'
            elif t == 'solusi':
                target_url = f'landing{theme_suffix}#solusi'
            elif t == 'faq':
                target_url = f'landing{theme_suffix}#faq'

        if not target_url:
            if any(k in t for k in ['coba gratis', 'daftar gratis', 'daftar sekarang', 'mulai bimbingan', 'buat akun', 'daftar akun']):
                target_url = f'login{theme_suffix}'
            elif t in ('masuk', 'login'):
                target_url = f'login{theme_suffix}'
            elif 'lanjutkan dengan google' in t or ('google' in t and base_name == 'login'):
                target_url = f'onboarding{theme_suffix}'
            elif 'mulai belajar' in t or 'selesai & mulai belajar' in t or (t == 'lanjut' and base_name == 'onboarding'):
                target_url = f'dashboard{theme_suffix}'
            elif t == 'beranda':
                target_url = f'dashboard{theme_suffix}'
            elif t in ('modul', 'katalog modul', 'buka katalog lengkap') or any(k in t for k in ['kembali ke modul', 'kembali ke daftar modul', 'jelajahi modul juara', 'jelajahi modul']):
                target_url = f'daftar-modul{theme_suffix}'
            elif t in ('tryout', 'simulasi tryout') or any(k in t for k in ['kembali ke daftar tryout', 'kembali ke tryout']):
                target_url = f'lobby-tryout{theme_suffix}'
            elif any(k in t for k in ['kembali ke hasil tryout', 'kembali ke hasil']):
                target_url = f'hasil-tryout{theme_suffix}'
            elif 'guru ai' in t or 'olimpix' in t or t == 'tanya guru ai':
                target_url = f'guru-ai{theme_suffix}'
            elif t == 'timeline' or 'jadwal ujian' in t or 'buka jadwal' in t:
                target_url = f'prep-timeline{theme_suffix}'
            elif 'lanjutkan modul' in t or 'lanjut baca' in t or 'lanjutkan belajar' in t:
                target_url = f'daftar-modul{theme_suffix}'
            elif any(k in t for k in ['baca modul', 'buka modul', 'pelajari modul', 'baca materi']):
                target_url = f'ebook-reader{theme_suffix}'
            elif 'kembali ke katalog' in t or (t == 'kembali' and base_name == 'ebook-reader'):
                target_url = f'daftar-modul{theme_suffix}'
            elif any(k in t for k in ['mulai tryout', 'kerjakan sekarang', 'mulai ujian', 'uji coba demo cbt']):
                target_url = f'lembar-tryout{theme_suffix}'
            elif any(k in t for k in ['selesai ujian', 'kumpulkan', 'akhiri ujian', 'selesai']):
                target_url = f'hasil-tryout{theme_suffix}'
            elif any(k in t for k in ['lihat pembahasan', 'bedah solusi', 'pembahasan soal', 'kunci jawaban']):
                target_url = f'pembahasan{theme_suffix}'
            elif any(k in t for k in ['ulangi tryout', 'kembali ke lobby', 'ulangi tryout mandiri']) or (t == 'kembali' and base_name in ('hasil-tryout', 'lobby-tryout')):
                target_url = f'lobby-tryout{theme_suffix}'
            elif any(k in t for k in ['premium', 'upgrade', 'paket belajar', 'langganan', 'buka akses premium', 'harga']):
                target_url = f'pricing{theme_suffix}'
            elif any(k in t for k in ['pilih paket', 'ambil paket', 'langganan sekarang', 'pilih paket ini', 'pilih paket bulanan', 'pilih paket 3 bulan', 'pilih paket 1 tahun', 'pilih paket belajar sekarang']):
                target_url = f'dashboard{theme_suffix}'
            elif any(k in t for k in ['laporan whatsapp', 'pantau progres bunda', 'kontak bunda', 'unduh raport', 'raport lengkap']):
                target_url = f'laporan-whatsapp{theme_suffix}'
            elif any(k in t for k in ['menara balok', 'balok tinggi']):
                target_url = f'tk-menara-balok{theme_suffix}'
            elif (t == 'kembali' or 'selesai bermain' in t) and base_name == 'tk-menara-balok':
                target_url = f'early-learner-tk{theme_suffix}'
            elif t == 'kembali' and base_name == 'onboarding':
                target_url = f'login{theme_suffix}'
            elif 'pedoman akademik' in t or 'etika' in t or 'pakta integritas' in t:
                target_url = f'state-anti-cheat{theme_suffix}'
            elif 'status layanan server' in t or 'status server' in t:
                target_url = f'state-offline{theme_suffix}'
            elif 'pusat bantuan' in t or 'bantuan' in t:
                target_url = f'guru-ai{theme_suffix}'
            elif 'simulasi tryout terjadwal' in t:
                target_url = f'lobby-tryout{theme_suffix}'
            elif 'bank soal olimpiade' in t:
                target_url = f'daftar-modul{theme_suffix}'
            elif 'analisis capaian siswa' in t:
                target_url = f'hasil-tryout{theme_suffix}'
            elif 'kurikulum nasional' in t:
                target_url = '#fitur'
            elif 'kontak dewan akademik' in t:
                target_url = f'guru-ai{theme_suffix}'
            elif 'kebijakan privasi' in t:
                target_url = f'state-anti-cheat{theme_suffix}'

        if target_url:
            clean_attrs = re.sub(r'type=[\"\']button[\"\']', '', attrs)
            if 'href=' in clean_attrs:
                clean_attrs = re.sub(r'href=[\"\'][^\"\']*?[\"\']', f'href="{target_url}"', clean_attrs)
            else:
                clean_attrs = f' href="{target_url}"' + clean_attrs
            return f'<a{clean_attrs} style="text-decoration:none;">{inner}</a>'

        return m.group(0)

    html = re.sub(r'<(button|a)\b([^>]*?)>(.*?)</\1>', repl_links, html, flags=re.S)

    # --- 6. KHUSUS ONBOARDING: KARTU TK JADI LINK KE EARLY LEARNER TK ---
    if base_name == 'onboarding':
        html = re.sub(r'(<div[^>]*?>\s*<div[^>]*?>\s*<span[^>]*?>\s*TK\s*</span>.*?)(</div>\s*</div>)',
                      rf'<a href="early-learner-tk{theme_suffix}" style="text-decoration:none; display:block;">\1\2</a>',
                      html, flags=re.S | re.I)

    # --- 7. SECTION IDS UNTUK SMOOTH SCROLL DI LANDING PAGE ---
    if base_name == 'landing':
        # Beri id dan tombol aksi pada Floating CBT HUD Card
        def enrich_hud(m):
            box = m.group(0)
            if 'id="hero-cbt-hud"' in box:
                return box
            box = re.sub(r'class="absolute -bottom-8 -left-4 sm:-left-8',
                         r'id="hero-cbt-hud" class="hero-cbt-draggable absolute -bottom-8 -left-4 sm:-left-8', box, count=1)
            hud_ctrl = (
                r'<div class="flex items-center gap-1.5">'
                r'<button type="button" id="hud-minimize-btn" class="p-1 rounded-md text-[#94A3B8] hover:text-[#0B1E3A] dark:hover:text-white transition-colors" title="Sembunyikan / Perkecil Kartu">'
                r'<span class="material-symbols-outlined text-[16px]">remove</span>'
                r'</button>'
                r'</div></div>'
            )
            box = re.sub(r'</div>\s*<div class="flex items-baseline', hud_ctrl + r'<div class="flex items-baseline', box, count=1)
            cta_cbt = (
                f'<a href="lembar-tryout{theme_suffix}" class="mt-3 w-full py-2 px-3 rounded-lg bg-[#D4A747] hover:bg-[#c29535] text-[#0B1E3A] font-semibold text-xs flex items-center justify-center gap-1.5 shadow-sm transition-all select-none" style="text-decoration:none;">'
                f'<span>Buka Simulasi Ujian Live</span>'
                f'<span class="material-symbols-outlined text-[15px]">arrow_forward</span>'
                f'</a></div></div></div></div>'
            )
            box = re.sub(r'</div>\s*</div>\s*</div>\s*</div>$', cta_cbt, box)
            return box

        html = re.sub(r'<div class="absolute -bottom-8 -left-4 sm:-left-8[^>]*?>.*?</div>\s*</div>\s*</div>\s*</div>', enrich_hud, html, count=1, flags=re.S)

        # Injeksi Section IDs secara presisi per tag <section> (BUKAN REGEX TAMAK)
        parts = re.split(r'(<section\b[^>]*?>)', html)
        out = [parts[0]]
        for i in range(1, len(parts), 2):
            sec_tag = parts[i]
            sec_body = parts[i+1] if i+1 < len(parts) else ''
            
            target_id = None
            if 'Kenyataan pahit' in sec_body:
                target_id = 'solusi'
            elif 'Enam pilar' in sec_body:
                target_id = 'fitur'
            elif 'Ketenangan pikiran Bunda' in sec_body:
                target_id = 'laporan-wa'
            elif 'Pilihan investasi' in sec_body:
                target_id = 'harga'
            elif 'Etika, Privasi' in sec_body:
                target_id = 'faq'

            if target_id and 'id=' not in sec_tag:
                sec_tag = re.sub(r'>$', f' id="{target_id}">', sec_tag)
            out.append(sec_tag)
            if i+1 < len(parts):
                out.append(sec_body)
        html = ''.join(out)

    # --- 8. COPYWRITING REBRANDING (SOKRATES -> OLIMPIX AI) ---
    html = re.sub(r"guru-ai-sokrates", "guru-ai-olimpix", html, flags=re.I)
    html = re.sub(r"Sokrates Junior", "Olimpix Junior", html, flags=re.I)
    html = re.sub(r"robot Sokrates Junior", "robot Olimpix Junior", html, flags=re.I)
    html = re.sub(r"Metode Sokratik", "Metode Dialektika Olimpix", html, flags=re.I)
    html = re.sub(r"Metode Sokrates", "Metode Olimpix", html, flags=re.I)
    html = re.sub(r"METODE SOKRATES", "METODE OLIMPIX AI", html, flags=re.I)
    html = re.sub(r"Konsep Sokrates", "Konsep Olimpix AI", html, flags=re.I)
    html = re.sub(r"Guru AI Sokrates", "Olimpix AI", html, flags=re.I)
    html = re.sub(r"sokrates|socrates", "Olimpix AI", html, flags=re.I)

    # --- 9. AVATAR 3D ROBOT OLIMPIX AI INJECTIONS ---
    if base_name == 'guru-ai':
        # Ganti avatar bot chat dengan gambar olimpix_ai_avatar.png
        html = re.sub(r'<img[^>]*?src=[\"\']https://lh3\.googleusercontent\.com/[^\"\']*?[\"\'][^>]*?>',
                      '<img src="assets/olimpix_ai_avatar.png" alt="Olimpix AI" class="w-10 h-10 rounded-full object-cover shadow-sm shrink-0 ring-2 ring-[#D4A747]/60">',
                      html, count=4)
    elif base_name == 'dashboard':
        # Pasang robot avatar di kartu rekomendasi AI
        html = re.sub(r'(<div class="inline-flex items-center gap-2">)(<img[^>]*?>|<span[^>]*?>psychology</span>)',
                      r'\1<img src="assets/olimpix_ai_avatar.png" alt="Olimpix AI" class="w-7 h-7 rounded-full object-cover shadow-sm ring-1 ring-[#D4A747]/80 inline-block shrink-0 mr-1.5">',
                      html)

    # --- 10. WRITE FILE HASIL ---
    dst_path = os.path.join(WORK_DIR, target_filename)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return target_filename

def build_all():
    print(f"\n=======================================================")
    print(f" MEMBANGUN ULANG 40 LAYAR DARI EXPORT ASLI ZIP 4 STITCH")
    print(f"=======================================================")
    success_count = 0
    for base, t_src, g_src in PAIRS:
        try:
            fn_t = transform_file(base, 'terang', t_src)
            fn_g = transform_file(base, 'gelap', g_src)
            print(f" [OK] {base:18} -> {fn_t} & {fn_g}")
            success_count += 2
        except Exception as e:
            print(f" [ERR] {base:18} -> GALAT: {e}")

    print(f"\nSelesai: {success_count}/40 berkas berhasil di-generate.")

    # Update index.html
    index_path = os.path.join(WORK_DIR, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=landing-terang.html">
  <title>Olimpix AI — Bimbingan Olimpiade & Simulasi CBT Berstandar Puspresnas</title>
  <script>window.location.href = "landing-terang.html";</script>
</head>
<body style="font-family: sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; background-color: #F7F5EE; color: #0B1E3A;">
  <p>Mengarahkan ke <a href="landing-terang.html" style="color: #D4A747; font-weight: bold;">Olimpix AI Live Preview...</a></p>
</body>
</html>''')

if __name__ == '__main__':
    build_all()
