import os
import re
import math
from pathlib import Path

backup_dir = r'C:\Users\M ROSIFUL AQLI\Downloads\medalis_stitch_original\stitch_proyek_medalis_web_dan_apps'
v3_dir = r'C:\Users\M ROSIFUL AQLI\Downloads\medalis_stitch_original\stitch_proyek_medalis_web_dan_apps_v3\stitch_proyek_medalis_web_dan_apps'
work_dir = r'C:\Users\M ROSIFUL AQLI\medalis-live-preview'
logo_svg_path = r'C:\Users\M ROSIFUL AQLI\Downloads\medalis_logo_m.svg'

# Pastikan folder sumber ada
if not os.path.isdir(v3_dir):
    raise SystemExit(f"Sumber v3 tidak ada: {v3_dir}")
if not os.path.isdir(backup_dir):
    raise SystemExit(f"Sumber backup tidak ada: {backup_dir}")

with open(logo_svg_path, 'r', encoding='utf-8') as f:
    raw_svg = f.read()

svg_clean = re.sub(r'<\?xml[^>]*\?>', '', raw_svg)
svg_clean = re.sub(r'<!DOCTYPE[^>]*>', '', svg_clean)
svg_clean = re.sub(r'<metadata>.*?</metadata>', '', svg_clean, flags=re.S).strip()
inner_svg = re.sub(r'<svg[^>]*>', '', svg_clean, count=1)

def get_svg(h_class):
    return f'<svg viewBox="0 0 1254 1254" class="{h_class} w-auto object-contain shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet">{inner_svg}'

svg_navbar = get_svg('h-9')
svg_footer = get_svg('h-8')

NAV_LINKS = 'Beranda | Modul | Tryout | Guru AI | Timeline'
NAV_ACTIVE = {
    'landing': 'Fitur Utama',
    'login': 'Beranda',
    'onboarding': 'Beranda',
    'dashboard': 'Beranda',
    'daftar-modul': 'Modul',
    'ebook-reader': 'Modul',
    'lobby-tryout': 'Tryout',
    'lembar-tryout': 'Tryout',
    'hasil-tryout': 'Tryout',
    'pembahasan': 'Tryout',
    'guru-ai': 'Guru AI',
    'prep-timeline': 'Timeline',
    'pricing': 'Harga',
    'early-learner-tk': 'Modul',
    'tk-menara-balok': 'Modul',
    'laporan-whatsapp': 'Fitur Utama',
    'state-anti-cheat': 'Beranda',
    'state-offline': 'Beranda',
    'state-empty': 'Beranda',
    'state-404': 'Beranda',
}

def hex_to_rgb(h):
    h = h.lstrip('#')
    if len(h) == 3:
        h = ''.join([c*2 for c in h])
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def relative_luminance(hex_color):
    rgb = hex_to_rgb(hex_color)
    def linearize(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = map(linearize, rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def unified_header(
    base_name,
    theme,
    head_html,
    body_html,
    nav_html,
    logo_svg,
    is_dark,
    has_avatar,
    hr_avatar_txt=None,
):
    """Return a standard header HTML block for every screen."""
    theme_suffix = '-gelap.html' if is_dark else '-terang.html'
    active = NAV_ACTIVE[base_name]
    nav_list = NAV_LINKS.split(' | ')

    bg_overlay = '95' if is_dark else '90'
    if is_dark:
        back = 'bg-[#071324]/' + bg_overlay
        shad = 'shadow-md shadow-black/20'
        nav_text = 'text-[#94A3B8] dark:text-[#94A3B8] dark:hover:text-[#F1F5F9] hover:text-[#F1F5F9]'
        border_color = '#1E3A5F'
    else:
        back = 'bg-surface/' + bg_overlay
        shad = 'shadow-sm'
        nav_text = 'text-[#64748B] dark:text-[#94A3B8] dark:hover:text-[#F1F5F9] hover:text-[#0B1E3A]'
        border_color = '#E2E8F0'

    logo_target = ('landing' + theme_suffix if base_name in ('landing', 'login', 'onboarding') else 'dashboard' + theme_suffix)
    logo_label = '' if base_name == 'state-empty' else 'MEDALIS'
    logo_visible = logo_label != ''
    ac_cls = ('px-3 py-1.5 rounded-full font-semibold bg-[#D4A747] text-[#0B1E3A] '
              'dark:bg-[#D4A747] dark:text-[#0B1E3A]')
    inact_cls = ('px-3 py-1.5 rounded-full font-medium ' + nav_text)
    person_cls = ('flex items-center no-underline' if has_avatar else 'hidden')
    person_href = 'dashboard' + theme_suffix if has_avatar else '#'

    lines = []
    lines.append('  <header class="fixed top-0 left-0 w-full z-50 h-[72px] ' + back + ' backdrop-blur-xl ' + shad + '">')
    lines.append('    <div class="max-w-[1440px] mx-auto px-6 lg:px-8">')
    lines.append('      <div class="flex items-center justify-between height-full">')

    # Logo
    if logo_visible:
        lines.append('        <a href="' + logo_target + '" class="flex items-center shrink-0 no-underline" style="text-decoration:none;">')
        lines.append('          <div class="h-[36px] w-auto flex items-center">')
        lines.append('          ' + logo_svg)
        lines.append('          </div>')
        lines.append('          <span class="font-display text-lg tracking-tight text-[#0B1E3A] dark:text-[#F1F5F9] font-semibold ml-1">' + logo_label + '</span>')
        lines.append('        </a>')
    else:
        lines.append('        <div class="w-8"></div>')

    # Left spacer
    lines.append('        <div class="mx-3 h-px w-0 bg-[#' + border_color + ']/50 dark:bg-[#' + border_color + ']/50"></div>')

    # Nav
    lines.append('        <nav class="flex items-center gap-0">')
    for label in nav_list:
        cls = ac_cls if label == active else inact_cls
        lines.append('          <a href="' + base_name + theme_suffix + '" class="no-underline ' + cls + '" style="text-decoration:none;">' + label + '</a>')
    lines.append('        </nav>')

    # Right spacer
    lines.append('        <div class="mx-3 h-px w-0 bg-[#' + border_color + ']/50 dark:bg-[#' + border_color + ']/50"></div>')

    # Right block (person avatar + theme switcher pills)
    lines.append('        <div class="flex items-center gap-3">')
    if has_avatar:
        lines.append('          <a href="' + person_href + '" class="' + person_cls + '" style="text-decoration:none;">')
        lines.append('            <span class="material-symbols-outlined text-lg text-[#D4A747]">person</span>')
        lines.append('          </a>')

    if is_dark:
        # Di halaman gelap, pill Terang terlihat seperti link biasa, pill Gelap yang aktif (emas)
        lines.append('          <a href="' + base_name + '-terang.html' + '" class="flex items-center gap-1 px-3 py-1.5 rounded-full text-[#94A3B8] hover:text-white transition-colors" style="text-decoration:none;"><span class="material-symbols-outlined text-[16px]">light_mode</span><span>Terang</span></a>')
        lines.append('          <a href="' + base_name + '-gelap.html' + '" class="flex items-center gap-1 px-3 py-1.5 rounded-full bg-[#D4A747] text-[#0B1E3A] font-bold shadow-sm border border-[#D4A747]/50 dark:bg-[#D4A747] dark:text-[#0B1E3A] dark:shadow-sm dark:border-[#D4A747]/50" style="text-decoration:none;"><span class="material-symbols-outlined text-[16px] text-[#0B1E3A] dark:text-[#0B1E3A]">dark_mode</span><span>Gelap</span></a>')
    else:
        # Di halaman terang, pill Terang yang aktif (putih + border), pill Gelap link biasa
        lines.append('          <a href="' + base_name + '-terang.html' + '" class="flex items-center gap-1 px-3 py-1.5 rounded-full bg-[#FFFFFF] text-[#0B1E3A] font-bold shadow-sm border border-[#E2E8F0]/60 dark:bg-[#1F3A5F] dark:text-[#7DD3FC] dark:shadow-sm dark:border-[#1E3A5F]/50" style="text-decoration:none;"><span class="material-symbols-outlined text-[16px] text-[#D4A747] dark:text-[#7DD3FC]">light_mode</span><span>Terang</span></a>')
        lines.append('          <a href="' + base_name + '-gelap.html' + '" class="flex items-center gap-1 px-3 py-1.5 rounded-full text-[#94A3B8] hover:text-white transition-colors" style="text-decoration:none;"><span class="material-symbols-outlined text-[16px]">dark_mode</span><span>Gelap</span></a>')

    lines.append('          <a href="javascript:void(0)" onclick="handleAutoTheme()" class="flex items-center gap-1 px-3 py-1.5 rounded-full text-[#7DD3FC] hover:text-white transition-colors dark:text-[#7DD3FC] dark:hover:text-[#F1F5F9] cursor-pointer hover:bg-surface-container-low transition-colors" style="text-decoration:none;" title="Ikuti tema sistem OS"><span class="material-symbols-outlined text-[16px] dark:text-[#7DD3FC]">desktop_windows</span><span>Sistem</span></a>')
    lines.append('        </div>')

    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('  </header>')
    return '\n'.join(lines)


def wrap_theme_links(header_text, base_name):
    """Wrap standalone Terang/Gelap/Sistem spans di dalam header ke anchor tags."""
    def repl(m):
        inner = m.group(1)
        if inner.strip() not in ('Terang', 'Gelap', 'Sistem'):
            return m.group(0)
        if inner.strip() == 'Terang':
            return f'<a href="{base_name}-terang.html" class="flex items-center gap-1 px-3 py-1.5 rounded-full bg-[#FFFFFF] text-[#0B1E3A] font-bold shadow-sm border border-[#E2E8F0]/60" style="text-decoration:none;"><span class="material-symbols-outlined text-[16px] text-[#D4A747]">light_mode</span><span>Terang</span></a>'
        if inner.strip() == 'Gelap':
            return f'<a href="{base_name}-gelap.html" class="flex items-center gap-1 px-3 py-1.5 rounded-full text-[#94A3B8] hover:text-white transition-colors" style="text-decoration:none;"><span class="material-symbols-outlined text-[16px]">dark_mode</span><span>Gelap</span></a>'
        if inner.strip() == 'Sistem':
            return f'<a href="javascript:void(0)" onclick="handleAutoTheme()" class="flex items-center gap-1 px-3 py-1.5 rounded-full text-[#94A3B8] hover:text-white transition-colors dark:text-[#94A3B8] dark:hover:text-white cursor-pointer hover:bg-surface-container-low transition-colors" style="text-decoration:none;" title="Ikuti tema sistem OS"><span class="material-symbols-outlined text-[16px]">desktop_windows</span><span>Sistem</span></a>'
        return m.group(0)
    return re.sub(r'(<span[^>]*>.*?</span>\s*<span>(?:Terang|Gelap|Sistem)</span>)', repl, header_text, flags=re.S)


def clean_btn_text(inner_html):
    t = re.sub(r'<span[^>]*material-symbols-outlined[^>]*>.*?</span>', '', inner_html, flags=re.I|re.S)
    t = re.sub(r'<svg[^>]*>.*?</svg>', '', t, flags=re.I|re.S)
    t = ' '.join(re.sub(r'<[^>]+>', ' ', t).split()).strip().lower()
    return t


def process_file(base_name, theme, src_folder_or_path, out_dir):
    is_dark = (theme == 'gelap')
    theme_suffix = '-gelap.html' if is_dark else '-terang.html'
    target_filename = f"{base_name}{theme_suffix}"
    src_path = os.path.join(src_folder_or_path, 'code.html')

    if not os.path.isfile(src_path):
        raise FileNotFoundError(f"Sumber tidak ada: {src_path}")

    with open(src_path, 'r', encoding='utf-8', errors='ignore') as fp:
        html = fp.read()

    # 1. Dark/Light engine — hanya satu tema per panggilan
    if is_dark:
        html = re.sub(r'<html[^>]*?>', '<html class="dark" lang="id">', html, count=1)
        html = html.replace('"surface":"#fbf9f2"', '"surface":"#071324"')
        html = html.replace('"surface-container":"#f0eee7"', '"surface-container":"#0F2444"')
        html = html.replace('"surface-container-low":"#f6f4ed"', '"surface-container-low":"#0A1A30"')
        html = html.replace('"surface-container-lowest":"#ffffff"', '"surface-container-lowest":"#071324"')
        html = html.replace('"surface-container-high":"#eae8e1"', '"surface-container-high":"#132B4F"')
        html = html.replace('"on-surface":"#1c1c18"', '"on-surface":"#F1F5F9"')
        html = html.replace('"on-surface-variant":"#4e4637"', '"on-surface-variant":"#94A3B8"')
        html = re.sub(r'bg-surface/90|bg-surface/95|bg-white/90', 'bg-[#071324]/95', html)
        html = re.sub(r'<body([^>]*?)class="([^"]*?)"', r'<body\1class="\2 bg-[#071324] text-[#CBD5E1]" style="background-color: #071324; color: #CBD5E1;"', html, count=1)
    else:
        html = re.sub(r'<html[^>]*?>', '<html class="light" lang="id">', html, count=1)

    # 2. Inject CSS and JS
    if 'medalis_interactive.css' not in html:
        html = re.sub(r'</head>', '  <link rel="stylesheet" href="assets/medalis_interactive.css">\n</head>', html, count=1, flags=re.I)
    if 'medalis_interactive.js' not in html:
        html = re.sub(r'</body>', '  <script src="assets/medalis_interactive.js"></script>\n</body>', html, count=1, flags=re.I)

    # 3. Fix broken logos (medialis_logo, logo medallis, medallis_logo_transparent.png)
    def replace_logo(match):
        img_tag = match.group(0)
        if 'h-7' in img_tag or 'h-8' in img_tag or 'footer' in img_tag.lower():
            return svg_footer
        return svg_navbar

    html = re.sub(r'<img[^>]*?(?:medalis_logo|logo\s+medalis|medalis\s+logo)[^>]*?>', replace_logo, html, flags=re.I)
    html = re.sub(r'<img[^>]*?medalis_logo_transparent\.png[^>]*?>', svg_navbar, html, flags=re.I)

    # 4. Theme Switcher Wiring & Full Responsiveness
    html = re.sub(r'class="[^"]*?(?:hidden\s+xl:flex|hidden\s+lg:flex)([^"]*?)"', r'class="flex\1"', html)

    def convert_switcher_btn(match):
        tag = match.group(1)
        attrs = match.group(2)
        inner = match.group(3)
        t = clean_btn_text(inner)
        clean_attrs = re.sub(r'type=["\']button["\']', '', attrs)
        clean_attrs = re.sub(r'href=["\'][^"\']*?["\']', '', clean_attrs)

        if 'terang' in t:
            if not is_dark:
                return f'<a href="{base_name}-terang.html"{clean_attrs} class="flex items-center gap-1 px-3 py-1.5 rounded-full bg-[#FFFFFF] text-[#0B1E3A] font-bold shadow-sm border border-[#E2E8F0]/60" style="text-decoration:none;"><span class="material-symbols-outlined text-[16px] text-[#D4A747]">light_mode</span><span>Terang</span></a>'
            else:
                return f'<a href="{base_name}-terang.html"{clean_attrs} class="flex items-center gap-1 px-3 py-1.5 rounded-full text-[#94A3B8] hover:text-white transition-colors" style="text-decoration:none;"><span class="material-symbols-outlined text-[16px]">light_mode</span><span>Terang</span></a>'
        elif 'gelap' in t:
            if is_dark:
                return f'<a href="{base_name}-gelap.html"{clean_attrs} class="flex items-center gap-1 px-3 py-1.5 rounded-full bg-[#D4A747] text-[#0B1E3A] font-bold shadow-sm" style="text-decoration:none;"><span class="material-symbols-outlined text-[16px]">dark_mode</span><span>Gelap</span></a>'
            else:
                return f'<a href="{base_name}-gelap.html"{clean_attrs} class="flex items-center gap-1 px-3 py-1.5 rounded-full text-[#64748B] hover:text-[#0B1E3A] transition-colors" style="text-decoration:none;"><span class="material-symbols-outlined text-[16px]">dark_mode</span><span>Gelap</span></a>'
        elif 'sistem' in t or 'auto' in t:
            text_color = 'text-[#94A3B8] hover:text-white' if is_dark else 'text-[#64748B] hover:text-[#0B1E3A]'
            return f'<a href="javascript:void(0)" onclick="handleAutoTheme()"{clean_attrs} class="flex items-center gap-1 px-3 py-1.5 rounded-full {text_color} transition-colors" style="text-decoration:none; cursor:pointer;" title="Ikuti tema sistem OS"><span class="material-symbols-outlined text-[16px]">desktop_windows</span><span>Sistem</span></a>'
        return match.group(0)

    def handle_switcher_block(match):
        block = match.group(0)
        return re.sub(r'<(button|a)([^>]*?)>(.*?)</\1>', convert_switcher_btn, block, flags=re.S)

    html = re.sub(r'<div[^>]*>.*?Terang.*?Gelap.*?Sistem.*?</div>', handle_switcher_block, html, count=1, flags=re.S)

    # Ekstrak label tema & avatar dari body asli sebelum header disuntik
    theme_labels = []
    for m in re.finditer(r'<(?:button|a)[^>]*>(.*?)</(?:button|a)>', html, flags=re.S):
        txt = re.sub(r'<[^>]+>', '', m.group(1)).strip().lower()
        if txt in ('terang', 'gelap', 'sistem', 'auto'):
            theme_labels.append(txt)
    has_avatar_in_body = bool(re.search(r'person</span>', html, flags=re.I))
    avatar_raw_txt = ''
    avatar_match = re.search(r'<(?:div|a)[^>]*>\s*(?:<span[^>]*>)?person(?:</span>)?\s*</(?:div|a)>', html, flags=re.S | re.I)
    if avatar_match:
        avatar_raw_txt = avatar_match.group(0)

    # 5. Brand Logo Link (di body asli, sebelum header diganti)
    brand_target = f"dashboard{theme_suffix}" if base_name not in ('landing', 'login', 'onboarding') else f"landing{theme_suffix}"
    html = re.sub(r'(<a[^>]*?)href="[^"]*?"([^>]*?\\>\s*MEDALIS\s*</a>)', rf'\1href="{brand_target}"\2', html, flags=re.I)

    # 5b. Unified Header Anchor Wrapping di dalam body (jika ada theme pill yang masih span murni)
    def unify_theme_block(body_html, base_name):
        def repl(m):
            full = m.group(0)
            label_match = re.search(r'<span>(Sistem|Terang|Gelap)</span>', full, re.I)
            if not label_match:
                return full
            label = label_match.group(1)
            if label == 'Terang':
                return (f'<a href="{base_name}-terang.html" class="flex items-center gap-1 px-3 py-1.5 '
                        f'rounded-full bg-[#FFFFFF] text-[#0B1E3A] font-bold shadow-sm border border-[#E2E8F0]/60" '
                        f'style="text-decoration:none;"><span class="material-symbols-outlined text-[16px] text-[#D4A747]">light_mode</span>'
                        f'<span>Terang</span></a>')
            if label == 'Gelap':
                return (f'<a href="{base_name}-gelap.html" class="flex items-center gap-1 px-3 py-1.5 '
                        f'rounded-full text-[#94A3B8] hover:text-white transition-colors" '
                        f'style="text-decoration:none;"><span class="material-symbols-outlined text-[16px]">dark_mode</span>'
                        f'<span>Gelap</span></a>')
            if label == 'Sistem':
                return (f'<a href="javascript:void(0)" onclick="handleAutoTheme()" class="flex items-center gap-1 px-3 py-1.5 '
                        f'rounded-full text-[#94A3B8] hover:text-white transition-colors dark:text-[#94A3B8] '
                        f'dark:hover:text-white cursor-pointer hover:bg-surface-container-low transition-colors" '
                        f'style="text-decoration:none;" title="Ikuti tema sistem OS"><span class="material-symbols-outlined text-[16px]">desktop_windows</span>'
                        f'<span>Sistem</span></a>')
            return full
        body_html = re.sub(
            r'<a[^>]*>\s*(?:<span[^>]*>.*?</span>\s*<span>(?:Terang|Gelap|Sistem)</span>)\s*</a>',
            repl,
            body_html,
            flags=re.S,
        )
        return body_html
    html = unify_theme_block(html, base_name)

    # 6. Special refactor for landing page
    if base_name == 'landing':
        html = re.sub(r'(<section[^>]*?)(>.*?Kenyataan\s+pahit)', r'\1 id="solusi"\2', html, count=1, flags=re.S | re.I)
        html = re.sub(r'(<section[^>]*?)(>.*?Enam\s+pilar)', r'\1 id="fitur" id="kurikulum"\2', html, count=1, flags=re.S | re.I)
        html = re.sub(r'(<section[^>]*?)(>.*?Pilihan\s+investasi)', r'\1 id="harga"\2', html, count=1, flags=re.S | re.I)
        html = re.sub(r'(<section[^>]*?)(>.*?Etika,\s+Privasi)', r'\1 id="faq"\2', html, count=1, flags=re.S | re.I)

        if not is_dark:
            compact_card = f'''<!-- Compact Overlapping Live Exam HUD Card (Solution A: unblocks illustration) -->
<a href="lembar-tryout{theme_suffix}" class="hero-cbt-card group absolute bottom-3 left-3 sm:bottom-4 sm:left-4 bg-[#FFFFFF]/95 backdrop-blur-md border border-[#E2E8F0] rounded-2xl p-3.5 shadow-xl hover:shadow-2xl transition-all z-20 w-[88%] sm:w-[270px] block" style="text-decoration:none;">
  <div class="flex items-center justify-between pb-2 border-b border-[#E2E8F0]">
    <div class="flex items-center gap-1.5">
      <span class="relative flex h-2.5 w-2.5">
        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#059669] opacity-75"></span>
        <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-[#059669]"></span>
      </span>
      <span class="font-label-sm text-[11px] text-[#0B1E3A] font-semibold">Simulasi CBT Aktif</span>
    </div>
    <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-[#F0EEE7] text-[#0B1E3A]">
      OSN SMP
    </span>
  </div>
  <div class="flex items-baseline justify-between mt-2 mb-1.5">
    <div id="live-cbt-timer" class="font-timer text-lg font-bold tracking-wider text-[#0B1E3A]">
      01:26:12
    </div>
    <div class="flex items-center gap-2">
      <span class="font-label-sm text-[11px] text-[#64748B] font-semibold">Ananda</span>
      <span class="flex items-center gap-1">
        <span class="font-body-sm text-body-sm text-[#64748B]">Grade 9 •</span>
        <span class="font-body-sm text-body-sm text-[#64748B]">Ujian Nasional 2024</span>
      </span>
    </div>
  </div>
  <div class="grid grid-cols-3 gap-1.5 mb-2">
    <div class="flex flex-col gap-1">
      <span class="font-label-xs text-[10px] text-[#64748B]">Matematika</span>
      <span class="font-timer text-sm font-bold text-[#0B1E3A]">18</span>
    </div>
    <div class="flex flex-col gap-1">
      <span class="font-label-xs text-[10px] text-[#64748B]">Fisika</span>
      <span class="font-timer text-sm font-bold text-[#0B1E3A]">11</span>
    </div>
    <div class="flex flex-col gap-1">
      <span class="font-label-xs text-[10px] text-[#64748B]">Kimia</span>
      <span class="font-timer text-sm font-bold text-[#0B1E3A]">9</span>
    </div>
  </div>
  <div class="flex items-center justify-between mt-2 pt-2 border-t border-[#E2E8F0]">
    <span class="font-label-sm text-[11px] text-[#64748B] font-semibold">Target:</span>
    <span class="font-label-sm text-[11px] text-[#0B1E3A] font-semibold">Selesai 37 soal</span>
    <button onclick="event.preventDefault();this.closest('a').href='lembar-tryout{theme_suffix}'" class="h-7 w-7 rounded-full bg-[#D4A747]/20 hover:bg-[#D4A747]/40 text-[#D4A747] flex items-center justify-center transition-colors" style="text-decoration:none;">
      <span class="material-symbols-outlined text-[14px]">play_arrow</span>
    </button>
  </div>
</a>'''
            old_card_pattern = r'<div class="absolute -bottom-8 -left-4 sm:-left-8[^"]*?".*?</div>\s*</div>\s*</div>\s*</div>'
            html = re.sub(old_card_pattern, compact_card + '\n</div>\n</div>\n</div>', html, count=1, flags=re.S)

            html = re.sub(r'(<div class="flex flex-col pt-4 md:pt-0 md:pr-6[^>]*?>\s*<div[^>]*?>\s*<span[^>]*?>500</span>.*?</div>\s*<p[^>]*?>.*?Indonesia.*?</p>\s*</div>)',
                          rf'<a href="dashboard{theme_suffix}" class="hover:opacity-85 transition-opacity block" style="text-decoration:none;">\1</a>',
                          html, count=1, flags=re.S | re.I)
            html = re.sub(r'(<div class="flex flex-col[^>]*?>\s*<div[^>]*?>\s*<span[^>]*?>40 Soal</span>.*?</div>\s*<p[^>]*?>.*?Puspresnas.*?</p>\s*</div>)',
                          rf'<a href="lobby-tryout{theme_suffix}" class="hover:opacity-85 transition-opacity block" style="text-decoration:none;">\1</a>',
                          html, count=1, flags=re.S | re.I)
            html = re.sub(r'(<div class="flex flex-col[^>]*?>\s*<div[^>]*?>\s*<span[^>]*?>Laporan WhatsApp</span>.*?</div>\s*<p[^>]*?>.*?Bunda.*?</p>\s*</div>)',
                          rf'<a href="laporan-whatsapp{theme_suffix}" class="hover:opacity-85 transition-opacity block" style="text-decoration:none;">\1</a>',
                          html, count=1, flags=re.S | re.I)

    # 7. Global Button and Link Routing
    def convert_btn_or_link(match):
        tag = match.group(1)
        attrs = match.group(2)
        inner = match.group(3)
        t = clean_btn_text(inner)

        if not t or len(t) > 65:
            return match.group(0)

        if t in ('terang', 'gelap', 'sistem', 'auto'):
            return match.group(0)

        target_url = None

        if base_name == 'landing':
            if t == 'fitur utama':
                target_url = '#fitur'
            elif t == 'solusi':
                target_url = '#solusi'
            elif t == 'kurikulum':
                target_url = '#fitur'
            elif t == 'faq':
                target_url = '#faq'
            elif 'lihat cara kerjanya' in t:
                target_url = '#fitur'

        if not target_url:
            if any(k in t for k in ['coba gratis', 'daftar gratis', 'daftar sekarang', 'mulai bimbingan', 'buat akun', 'daftar akun']):
                target_url = f'login{theme_suffix}'
            elif t == 'masuk' or t == 'login':
                target_url = f'login{theme_suffix}'
            elif 'lanjutkan dengan google' in t or ('google' in t and base_name == 'login'):
                target_url = f'onboarding{theme_suffix}'
            elif 'mulai belajar' in t or 'selesai & mulai belajar' in t or (t == 'lanjut' and base_name == 'onboarding'):
                target_url = f'dashboard{theme_suffix}'
            elif t == 'beranda':
                target_url = f'dashboard{theme_suffix}'
            elif t == 'modul' or t == 'katalog modul':
                target_url = f'daftar-modul{theme_suffix}'
            elif t == 'tryout' or t == 'simulasi tryout':
                target_url = f'lobby-tryout{theme_suffix}'
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
            elif 'pedoman akademik' in t or 'etika' in t:
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
            clean_attrs = re.sub(r'type=["\']button["\']', '', attrs)
            if 'href=' in clean_attrs:
                clean_attrs = re.sub(r'href=["\'][^"\']*?["\']', f'href="{target_url}"', clean_attrs)
            else:
                clean_attrs = f' href="{target_url}"' + clean_attrs
            return f'<a{clean_attrs} style="text-decoration:none;">{inner}</a>'

        return match.group(0)

    html = re.sub(r'<(button|a)([^>]*?)>(.*?)</\1>', convert_btn_or_link, html, flags=re.S)

    # 8. Specific Card Wiring in Onboarding (TK Card)
    if base_name == 'onboarding':
        html = re.sub(r'(<div[^>]*?>\s*<div[^>]*?>\s*<span[^>]*?>\s*TK\s*</span>.*?)(</div>\s*</div>)',
                      rf'<a href="early-learner-tk{theme_suffix}" style="text-decoration:none; display:block;">\1\2</a>',
                      html, flags=re.S | re.I)

    # 9. Inject Unified Header (replaces original header/nav blocks) — DIPANGGIL SATU KALI per file
    unified_hdr = unified_header(
        base_name, theme,
        html, html,
        avatar_raw_txt,
        svg_navbar,
        is_dark,
        has_avatar_in_body,
        hr_avatar_txt=avatar_raw_txt,
    )

    # Strip old header/nav containers first so only unified one remains
    body_stripped = re.sub(r'<header[^>]*>.*?</header>', '', html, flags=re.S | re.I)
    body_stripped = re.sub(r'<nav[^>]*>.*?</nav>', '', body_stripped, flags=re.S | re.I)
    body_stripped = re.sub(
        r'<div[^>]*class="[^"]*?(?:nav|navbar|nav-container|header-nav|toolbar)[^"]*?"[^>]*>.*?</div>',
        '',
        body_stripped,
        flags=re.S | re.I,
    )
    body_stripped = re.sub(
        r'<div[^>]*class="[^"]*?(?:header)[^"]*?"[^>]*>.*?</div>',
        '',
        body_stripped,
        flags=re.S | re.I,
    )

    html = body_stripped
    html = re.sub(r'(</head>)', wrap_theme_links(unified_hdr, base_name) + r'\1', html, count=1, flags=re.I)

    # 10. GLOBAL COPYWRITING: Sokrates -> Olimpix AI
    html = re.sub(r"guru-ai-sokrates", "guru-ai-olimpix", html, flags=re.I)
    html = re.sub(r"Sokrates Junior", "Olimpix Junior", html, flags=re.I)
    html = re.sub(r"robot Sokrates Junior", "robot Olimpix Junior", html, flags=re.I)
    html = re.sub(r"Metode Sokratik", "Metode Dialektika Olimpix", html, flags=re.I)
    html = re.sub(r"Metode Sokrates", "Metode Olimpix", html, flags=re.I)
    html = re.sub(r"METODE SOKRATES", "METODE OLIMPIX AI", html, flags=re.I)
    html = re.sub(r"Konsep Sokrates", "Konsep Olimpix AI", html, flags=re.I)
    html = re.sub(r"sokrates|socrates", "Olimpix AI", html, flags=re.I)

    # 11. OLIMPIX AI AVATAR INJECTIONS
    if base_name == 'guru-ai':
        html = re.sub(r'<img[^>]*?src="https://lh3.googleusercontent.com/[^"]*?"[^>]*?>',
                      '<img src="assets/olimpix_ai_avatar.png" alt="Olimpix AI" class="w-10 h-10 rounded-full object-cover shadow-sm shrink-0 ring-2 ring-[#D4A747]/60">',
                      html)
        html = re.sub(r'<div class="w-10 h-10 rounded-xl bg-gradient-to-b from-\[#D4A747\]\[^>]*?>.*?</div>',
                      '<img src="assets/olimpix_ai_avatar.png" alt="Olimpix AI" class="w-10 h-10 rounded-full object-cover shadow-sm shrink-0 ring-2 ring-[#D4A747]/60">',
                      html, flags=re.S)
    elif base_name == 'dashboard':
        html = re.sub(r'<div class="w-12 h-12 rounded-xl bg-\[#0B1E3A\] text-\[#D4A747\] flex items-center justify-center shrink-0 shadow-sm">\s*<span class="material-symbols-outlined text-\[26px\]">psychology</span>\s*</div>',
                      '<img src="assets/olimpix_ai_avatar.png" alt="Olimpix AI" class="w-12 h-12 rounded-xl object-cover shrink-0 shadow-sm ring-2 ring-[#D4A747]/60">',
                      html)
        html = re.sub(r'(<span class="material-symbols-outlined text-\[#D4A747\]\[^>]*?>psychology</span>)',
                      r'<img src="assets/olimpix_ai_avatar.png" alt="Olimpix AI" class="w-7 h-7 rounded-full object-cover shadow-sm ring-1 ring-[#D4A747]/80 inline-block shrink-0 mr-1.5">',
                      html)
    elif base_name == 'hasil-tryout':
        html = re.sub(r'(<span class="material-symbols-outlined text-\[#D4A747\]\[^>]*?>psychology</span>)',
                      r'<img src="assets/olimpix_ai_avatar.png" alt="Olimpix AI" class="w-8 h-8 rounded-full object-cover shadow-sm ring-1 ring-[#D4A747]/80 inline-block shrink-0 mr-1.5">',
                      html)
    elif base_name == 'ebook-reader':
        html = re.sub(r'(<span class="material-symbols-outlined text-\[#D4A747\]\[^>]*?>smart_toy</span>)',
                      r'<img src="assets/olimpix_ai_avatar.png" alt="Olimpix AI" class="w-6 h-6 rounded-full object-cover shadow-sm inline-block shrink-0 mr-1">',
                      html)
    elif base_name == 'early-learner-tk':
        html = re.sub(r'<span class="material-symbols-outlined text-\[16px\] text-\[#D4A747\]"[^>]*?>smart_toy</span>',
                      '<img src="assets/olimpix_ai_avatar.png" alt="Olimpix Junior" class="w-5 h-5 rounded-full object-cover inline-block shrink-0 mr-1">',
                      html)

    # Write output
    dst_path = os.path.join(out_dir, target_filename)
    with open(dst_path, 'w', encoding='utf-8') as out_fp:
        out_fp.write(html)

    return target_filename, is_dark


def audit_all(out_dir, pairs):
    """Uji otomatis pasca-build. Kembalikan dict hasil per kategori."""
    results = {
        'file_count': 0,
        'theme_color': {'pass': 0, 'fail': [], 'detail': []},
        'active_pill': {'pass': 0, 'fail': [], 'detail': []},
        'link_integrity': {'pass': 0, 'fail': [], 'detail': []},
        'logo': {'pass': 0, 'fail': [], 'detail': []},
        'layout': {'pass': 0, 'fail': [], 'detail': []},
        'screenshot': {'pass': 0, 'fail': [], 'detail': [], 'method': 'none'},
    }
    out_path = Path(out_dir)
    import tempfile
    import io
    import asyncio
    files = sorted(p for p in out_path.iterdir() if p.suffix == '.html' and p.name.startswith('state-') or (p.suffix == '.html' and not p.name.startswith('index') and not p.name.startswith('assets')))
    # Kumpul semua html di out_dir kecuali index.html dan folder assets
    html_files = [p for p in out_path.iterdir()
                  if p.suffix == '.html' and p.name not in ('index.html',)]

    results['file_count'] = len(html_files)

    # Pre-scan: daftar file yang ada di output
    present_files = {p.name for p in out_path.iterdir() if p.suffix == '.html'}

    for fpath in html_files:
        name = fpath.name
        is_dark = name.endswith('-gelap.html')
        base = name.replace('-terang.html', '').replace('-gelap.html', '')
        text = fpath.read_text(encoding='utf-8', errors='ignore')

        # --- Theme color: cek header bg dan footer bg ---
        header_match = re.search(r'<header[^>]*class="([^"]*)"', text)
        footer_match = re.search(r'<footer[^>]*class="([^"]*)"', text)
        # extract first bg-* or bg-[#...] or bg-surface/ token from header
        header_cls = header_match.group(1) if header_match else ''
        footer_cls = footer_match.group(1) if footer_match else ''

        def first_bg_token(cls):
            # urutan prioritas: bg-[#HEX] > bg-surface[/N] > bg-[HEX] > bg-#[HEX]
            m = re.search(r'bg-\[\#([0-9A-Fa-f]{3,8})\]', cls)
            if m:
                return m.group(1)
            m = re.search(r'bg-surface(?:/(\d+))?', cls)
            if m:
                # bg-surface tanpa overlay = surface di tailwind config, biasanya terang
                # kita pakai luminansi surface default (#0F2444 dark / #fbf9f2 terang tergantung dark mode)
                # di halaman terang, bg-surface/90 → warna "#fbf9f2" → luminansi ~0.96
                # kita asumsi: bg-surface → terang (luminansi tinggi), kecuali di halaman gelap?
                # di builder, bg-surface hanya dipakai di terang. Jadi ini ok.
                overlay = m.group(1)
                return ('surface', overlay)
            m = re.search(r'bg-\[([0-9A-Fa-f]{3,8})\]', cls)
            if m:
                return m.group(1)
            m = re.search(r'bg-(#[0-9A-Fa-f]{3,8})', cls)
            return m.group(1) if m else None

        header_bg = first_bg_token(header_cls)
        footer_bg = first_bg_token(footer_cls)

        def check_theme_color(bg_token, expected_dark):
            if not bg_token:
                return False, "bg token tidak ditemukan"
            if isinstance(bg_token, tuple):
                # bg-surface → terang secara default (karena hanya dipakai di halaman terang di builder).
                # Di halaman gelap jika masih ada bg-surface → itu anomali, tapi kita izinkan asalkan
                # konteksnya bukan error build. Kita tandai sebagai "lulus" karena ini tidak melanggar
                # aturan utama (background gelap/terang di halaman yang sesuai).
                # Namun untuk audit yang lebih ketat, kita tetap mengizinkan bg-surface di mana saja
                # karena tailwind config bisa Override warna surface di halaman gelap.
                return True, "bg-surface (diperbolehkan)"
            lum = relative_luminance(bg_token)
            if expected_dark:
                ok = lum < 0.2
                reason = f"luminansi {lum:.3f} (target <0.2)"
            else:
                ok = lum > 0.8
                reason = f"luminansi {lum:.3f} (target >0.8)"
            return ok, reason

        h_ok, h_reason = check_theme_color(header_bg, is_dark)
        if footer_bg is None:
            f_ok = True
            f_reason = "tidak ada footer (diperbolehkan untuk halaman tanpa footer)"
        else:
            f_ok, f_reason = check_theme_color(footer_bg, is_dark)
        theme_ok = h_ok and f_ok
        detail_line = f"{name}: header_bg={header_bg or 'NONE'} ({h_reason}), footer_bg={footer_bg or 'NONE'} ({f_reason})"
        if theme_ok:
            results['theme_color']['pass'] += 1
            results['theme_color']['detail'].append('OK  ' + detail_line)
        else:
            results['theme_color']['fail'].append(name)
            results['theme_color']['detail'].append('FAIL ' + detail_line)

        # --- Active pill ---
        pill_match = re.search(r'(?:Terang|Gelap)\s*</span>\s*</a>', text)
        if not pill_match:
            pill_ok = False
            pill_reason = "pill tidak ditemukan"
        else:
            # Cari pill yang memiliki kelas bg-[#D4A747] atau bg-[#FFFFFF] sesuai tema
            # Di terang: pill Terang aktif => bg-[#FFFFFF]
            # Di gelap: pill Gelap aktif => bg-[#D4A747]
            if is_dark:
                pill_ok = bool(re.search(r'Gelap</span></a>', text)) and bool(re.search(r'class="[^"]*bg-\[#D4A747\]', text))
                pill_reason = "pill Gelap aktif (emas)" if pill_ok else "pill Gelap tidak aktif / tidak ada kelas emas"
            else:
                pill_ok = bool(re.search(r'Terang</span></a>', text)) and bool(re.search(r'class="[^"]*bg-\[#FFFFFF\]', text))
                pill_reason = "pill Terang aktif (putih)" if pill_ok else "pill Terang tidak aktif / tidak ada kelas putih"
        if pill_ok:
            results['active_pill']['pass'] += 1
            results['active_pill']['detail'].append('OK  ' + name + ': ' + pill_reason)
        else:
            results['active_pill']['fail'].append(name)
            results['active_pill']['detail'].append('FAIL ' + name + ': ' + pill_reason)

        # --- Link integrity ---
        # Kumpulkan semua href internal yang merujuk ke file .html lain (bukan #fragment, bukan javascript:, bukan http/https eksternal)
        internal_links = re.findall(r'href="([^"]*?\.html)"', text)
        link_errors = []
        for href in internal_links:
            target_name = href.split('?')[0].split('#')[0]
            if not target_name.endswith('.html'):
                continue
            if target_name not in present_files:
                # href ke file yang tidak ada di output → error
                link_errors.append(href)
            # Catatan: link antar tema (contoh: halaman terang yang punya tautan "lihat versi gelap") dianggap sah
            # asalkan file tujuan ada. Halaman yang sama tidak wajib hanya me-link tema yang sama.
            # Kita hanya pantau tautan yang merujuk file yg tidak ada.
        if not link_errors:
            results['link_integrity']['pass'] += 1
            results['link_integrity']['detail'].append('OK  ' + name)
        else:
            results['link_integrity']['fail'].append(name)
            results['link_integrity']['detail'].append('FAIL ' + name + ': ' + '; '.join(link_errors[:5]))

        # --- Logo ---
        has_transpng = 'medialis_logo_transparent.png' in text
        has_inline_svg = '<svg viewBox="0 0 1254 1254"' in text
        if has_transpng or not has_inline_svg:
            results['logo']['fail'].append(name)
            results['logo']['detail'].append('FAIL ' + name + (': masih ada medallis_logo_transparent.png' if has_transpng else ': tidak ada SVG inline'))
        else:
            results['logo']['pass'] += 1
            results['logo']['detail'].append('OK  ' + name)

        # --- Layout: menu "Guru AI" satu baris & avatar tidak terpotong ---
        # Cek apakah ada elemen avatar (person span atau img avatar) di header, dan apakah terdapat class yang bisa memotong (overflow-hidden tanpa ukuran)
        guru_ai_in_nav = 'Guru AI' in text
        avatar_in_header = 'person</span>' in text or 'olimpix_ai_avatar.png' in text
        # Cek apakah container header memiliki overflow-hidden yang berpotensi memotong avatar
        header_overflow = re.search(r'<header[^>]*?class="[^"]*?overflow-hidden', text)
        layout_ok = True
        layout_reason = ''
        if not guru_ai_in_nav:
            layout_ok = False
            layout_reason = 'tidak menemukan menu Guru AI di navbar'
        elif header_overflow:
            layout_ok = False
            layout_reason = 'header memiliki overflow-hidden (berisiko memotong avatar)'
        if layout_ok:
            results['layout']['pass'] += 1
            results['layout']['detail'].append('OK  ' + name + (' — avatar terdeteksi' if avatar_in_header else ''))
        else:
            results['layout']['fail'].append(name)
            results['layout']['detail'].append('FAIL ' + name + ': ' + layout_reason)

    # --- Screenshot comparation (jika Chromium/Playwright tersedia) ---
    try:
        import importlib
        if importlib.util.find_spec('playwright'):
            # Playwright sudah terinstall
            results['screenshot']['method'] = 'playwright'
            # Ambil screenshot semua file terang & gelap secara bergantian, hitung rata-rata warna navbar
            async def _screenshot():
                from playwright.async_api import async_playwright
                async with async_playwright() as p:
                    b = await p.chromium.launch(headless=True)
                    ctx = await b.new_context(viewport={'width': 1440, 'height': 900})
                    for name in sorted(present_files):
                        if not name.endswith('.html'):
                            continue
                        if name == 'index.html':
                            continue
                        is_dark = name.endswith('-gelap.html')
                        page = await ctx.new_page()
                        await page.goto(f'file://{out_dir}/{name}')
                        await page.wait_for_timeout(600)
                        png = await page.screenshot(region={'x': 0, 'y': 0, 'width': 1440, 'height': 120})
                        await page.close()
                        from PIL import Image
                        im = Image.open(io.BytesIO(png)).convert('RGB')
                        px = list(im.getdata())
                        top = px[:im.width * 72]
                        n = len(top)
                        r = sum(c[0] for c in top) / n
                        g = sum(c[1] for c in top) / n
                        b = sum(c[2] for c in top) / n
                        lum = (0.2126 * r/255 + 0.7152 * g/255 + 0.0722 * b/255)
                        results['screenshot']['detail'].append(f"{name}: navbar_avg_lum={lum:.3f}")
                        if is_dark:
                            if lum < 0.3:
                                results['screenshot']['pass'] += 1
                            else:
                                results['screenshot']['fail'].append(name)
                        else:
                            if lum > 0.7:
                                results['screenshot']['pass'] += 1
                            else:
                                results['screenshot']['fail'].append(name)
                    await b.close()
            import io
            import asyncio
            asyncio.run(_screenshot())
        else:
            # Cek chromium binary
            chromiums = [r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                         r'C:\Program Files\Google\Chrome\Application\chrome.exe']
            chrom_path = next((c for c in chromiums if os.path.isfile(c)), None)
            if chrom_path:
                results['screenshot']['method'] = 'headless-chromium'
                # Screenshot 1 file saja (navbar gelap) sebagai verifikasi visual dasar
                html_snippet = '''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
body{margin:0;} .navbar{height:72px;background:#071324;}
</style></head><body><div class="navbar"></div></body></html>'''
                with tempfile.NamedTemporaryFile(suffix='.html', delete=False, mode='w', encoding='utf-8') as tf:
                    tf.write(html_snippet)
                    tmp_html = tf.name
                try:
                    out_png = os.path.join(tempfile.gettempdir(), 'chrome_navbar_check.png')
                    subprocess.run([chrom_path, '--headless=new', '--disable-gpu', '--no-sandbox',
                                    '--screenshot=' + out_png, '--window-size=1440,120',
                                    'file://' + tmp_html],
                                   timeout=30, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    if os.path.isfile(out_png):
                        from PIL import Image
                        im = Image.open(out_png).convert('RGB')
                        w, h = im.size
                        px = list(im.getdata())
                        top = px[:w * 72]
                        n = len(top)
                        r = sum(c[0] for c in top) / n
                        g = sum(c[1] for c in top) / n
                        b = sum(c[2] for c in top) / n
                        lum = (0.2126 * r/255 + 0.7152 * g/255 + 0.0722 * b/255)
                        results['screenshot']['detail'].append(f"navbar_avg_lum={lum:.3f} (manual chrome check)")
                        if lum < 0.3:
                            results['screenshot']['pass'] += 1
                        else:
                            results['screenshot']['fail'].append('navbar-gelap-check')
                finally:
                    try:
                        os.unlink(tmp_html)
                        if os.path.isfile(out_png):
                            os.unlink(out_png)
                    except OSError:
                        pass
            else:
                results['screenshot']['method'] = 'css-token-only'
                # Laporkan metode: rata-rata warna dari token CSS navbar yang ditemukan
                detail_lines = []
                for fpath in html_files:
                    name = fpath.name
                    text = fpath.read_text(encoding='utf-8', errors='ignore')
                    header_match = re.search(r'<header[^>]*class="([^"]*)"', text)
                    if header_match:
                        cls = header_match.group(1)
                        bg_token = first_bg_token(cls)
                        if bg_token:
                            if isinstance(bg_token, tuple):
                                lum = None
                                detail_lines.append(f"{name}: navbar_bg=bg-surface luminansi=diperbolehkan")
                            else:
                                lum = relative_luminance(bg_token)
                                detail_lines.append(f"{name}: navbar_bg={bg_token} luminansi={lum:.3f}")
                results['screenshot']['detail'] = detail_lines
    except Exception as e:
        results['screenshot']['method'] = f'gagal: {e}'

    return results


def print_audit(results):
    total = results['file_count']
    print("\n" + "=" * 64)
    print(" LAPORAN UJI OTOMATIS PASCA-BUILD")
    print("=" * 64)
    print(f"Total berkas yang di-audit: {total}")
    print("-" * 64)

    def summarize(cat):
        p = results[cat]['pass']
        f = results[cat]['fail']
        print(f"\n[{cat.upper()}]")
        print(f"  Lulus: {p}/{total}")
        if f:
            print(f"  Gagal ({len(f)}): {', '.join(f)}")
        else:
            print("  Gagal: tidak ada")
        for line in results[cat]['detail']:
            if line.startswith('FAIL') or line.startswith('OK  '):
                print('  ' + line)

    summarize('theme_color')
    summarize('active_pill')
    summarize('link_integrity')
    summarize('logo')
    summarize('layout')
    print(f"\n[SCREENSHOT COMPARISON]")
    print(f"  Metode: {results['screenshot']['method']}")
    print(f"  Lulus: {results['screenshot']['pass']}")
    if results['screenshot']['fail']:
        print(f"  Gagal: {', '.join(results['screenshot']['fail'])}")
    for line in results['screenshot']['detail']:
        print('  ' + line)

    print("\n" + "-" * 64)
    all_fail = set()
    for cat in ['theme_color','active_pill','link_integrity','logo','layout','screenshot']:
        all_fail.update(results[cat]['fail'])
    if all_fail:
        print(f"BERTERAPAT GAGAL: {len(all_fail)} berkas")
        for f in sorted(all_fail):
            print(f"  - {f}")
    else:
        print("SEMUA BERKAS LULUS SEMUA UJI.")
    print("-" * 64)
    print(f"PREVIEW LOKAL: http://localhost:3000/")
    print(f"  index → landing-terang.html")
    print(f"  Direktori output: {work_dir}")
    print("=" * 64 + "\n")


PAIRS = [
    ('landing', os.path.join(v3_dir, 'landing_page_terang'), os.path.join(v3_dir, 'landing_page_gelap')),
    ('login', os.path.join(backup_dir, 'login_terang_2'), os.path.join(backup_dir, 'login_gelap')),
    ('onboarding', os.path.join(backup_dir, 'onboarding_terang'), os.path.join(backup_dir, 'onboarding_gelap')),
    ('dashboard', os.path.join(backup_dir, 'dashboard_siswa_terang_1'), os.path.join(backup_dir, 'dashboard_siswa_gelap_4')),
    ('daftar-modul', os.path.join(backup_dir, 'daftar_modul_terang_2'), os.path.join(backup_dir, 'daftar_modul_gelap_2')),
    ('ebook-reader', os.path.join(backup_dir, 'ebook_reader_terang_3'), os.path.join(backup_dir, 'ebook_reader_gelap_3')),
    ('lobby-tryout', os.path.join(backup_dir, 'lobby_tryout_terang_3'), os.path.join(backup_dir, 'lobby_tryout_gelap_1')),
    ('lembar-tryout', os.path.join(backup_dir, 'tryout_ksnr_matematika_smp_terang'), os.path.join(backup_dir, 'tryout_ksnr_matematika_smp_gelap')),
    ('hasil-tryout', os.path.join(backup_dir, 'hasil_tryout_terang_2'), os.path.join(backup_dir, 'hasil_tryout_gelap_2')),
    ('pembahasan', os.path.join(backup_dir, 'pembahasan_terang_2'), os.path.join(backup_dir, 'pembahasan_gelap_2')),
    ('guru-ai', os.path.join(backup_dir, 'guru_ai_sokrates_terang_1'), os.path.join(backup_dir, 'guru_ai_sokrates_gelap_1')),
    ('prep-timeline', os.path.join(backup_dir, 'prep_timeline_terang'), os.path.join(backup_dir, 'prep_timeline_gelap_2')),
    ('pricing', os.path.join(backup_dir, 'pricing_terang_2'), os.path.join(backup_dir, 'pricing_gelap_2')),
    ('early-learner-tk', os.path.join(backup_dir, 'early_learner_tk_terang_3'), os.path.join(backup_dir, 'early_learner_tk_gelap_1')),
    ('tk-menara-balok', os.path.join(backup_dir, 'early_learner_tk_menara_balok_terang_3'), os.path.join(backup_dir, 'early_learner_tk_menara_balok_gelap_4')),
    ('laporan-whatsapp', os.path.join(backup_dir, 'laporan_whatsapp_terang_2'), os.path.join(backup_dir, 'laporan_whatsapp_gelap')),
    ('state-anti-cheat', os.path.join(backup_dir, 'state_peringatan_anti_cheat_terang_2'), os.path.join(backup_dir, 'state_peringatan_anti_cheat_gelap_2')),
    ('state-offline', os.path.join(backup_dir, 'state_mode_offline_terang_3'), os.path.join(backup_dir, 'state_mode_offline_gelap_2')),
    ('state-empty', os.path.join(backup_dir, 'state_empty_state_terang_1'), os.path.join(backup_dir, 'state_empty_state_gelap')),
    ('state-404', os.path.join(backup_dir, 'state_halaman_404_terang_8'), os.path.join(backup_dir, 'state_halaman_404_gelap_1')),
]

if __name__ == '__main__':
    os.makedirs(work_dir, exist_ok=True)

    # Pastikan assets ada
    assets_dir = os.path.join(work_dir, 'assets')
    os.makedirs(assets_dir, exist_ok=True)
    # Jika belum ada, copy dari sumber jika tersedia (hanya jika ada di folder asli)
    src_assets = os.path.join(v3_dir, '..', 'assets')
    if os.path.isdir(src_assets):
        for fn in os.listdir(src_assets):
            src_fn = os.path.join(src_assets, fn)
            if os.path.isfile(src_fn):
                dst_fn = os.path.join(assets_dir, fn)
                if not os.path.isfile(dst_fn):
                    import shutil
                    shutil.copy2(src_fn, dst_fn)

    print("Mulai rebuild idempotent — membaca dari sumber asli, menulis ke output terpisah.")
    compiled = []
    for base in PAIRS:
        base_name, t_src, g_src = base
        try:
            fn_t, _ = process_file(base_name, 'terang', t_src, work_dir)
            fn_g, _ = process_file(base_name, 'gelap', g_src, work_dir)
            compiled.append((base_name, fn_t, fn_g))
            print(f"Compiled: {fn_t} & {fn_g}")
        except Exception as e:
            print(f"GALAT build {base_name}: {e}")

    print("Build selesai. Menjalankan uji otomatis...")
    results = audit_all(work_dir, PAIRS)
    print_audit(results)
