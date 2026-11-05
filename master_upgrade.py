#!/usr/bin/env python3
"""
master_upgrade.py — Skrip Eksekusi Komprehensif Medalis Live Preview
"""

import os
import re
import glob

WORK_DIR = "/root/medalis-live-preview"
os.chdir(WORK_DIR)

# ==============================================================================
# 1. TEMPLATE NAVBAR BAKU (3 TIPE) & MOBILE NAVIGATION
# ==============================================================================

def get_public_navbar(is_dark=False):
    theme_suffix = "-gelap.html" if is_dark else "-terang.html"
    bg_class = "bg-[#0B1E3A]/95 border-[#1E293B]" if is_dark else "bg-white/95 border-[#E2E8F0]"
    text_main = "text-white" if is_dark else "text-[#0B1E3A]"
    text_muted = "text-[#94A3B8] hover:text-white" if is_dark else "text-[#475569] hover:text-[#0B1E3A]"
    brand_sub = "text-[#D4A747]"
    light_btn_cls = "bg-white text-[#0B1E3A] shadow-sm font-semibold" if not is_dark else "text-[#94A3B8] hover:text-white"
    dark_btn_cls = "bg-[#0F2444] text-white shadow-sm font-semibold" if is_dark else "text-[#64748B] hover:text-[#0B1E3A]"
    
    return f'''<!-- NAVBAR PUBLIK TERSTANDARISASI (TIPE A) -->
<header class="fixed top-0 left-0 w-full z-50 {bg_class} backdrop-blur-md shadow-sm border-b">
  <div class="max-w-7xl mx-auto h-[72px] px-4 sm:px-6 lg:px-8 flex items-center justify-between gap-4">
    <!-- Logo -->
    <a href="landing{theme_suffix}" style="text-decoration:none;" class="flex items-center gap-3 shrink-0">
      <img alt="Medalis Logo" class="h-8 sm:h-9 w-auto object-contain" src="assets/medalis_logo.svg">
      <div class="flex flex-col">
        <span class="font-bold text-lg sm:text-xl tracking-wider {text_main} leading-none">MEDALIS</span>
        <span class="text-[10px] tracking-widest uppercase font-semibold {brand_sub}">Olympiad Academy</span>
      </div>
    </a>

    <!-- Menu Desktop (Bersih Tanpa Avatar) -->
    <nav class="hidden lg:flex items-center gap-1 xl:gap-2">
      <a href="landing{theme_suffix}#fitur" class="px-3 py-2 rounded-lg text-sm font-medium {text_muted} transition-colors">Fitur Unggulan</a>
      <a href="daftar-modul{theme_suffix}" class="px-3 py-2 rounded-lg text-sm font-medium {text_muted} transition-colors">Kurikulum & Past Papers</a>
      <a href="prep-timeline{theme_suffix}" class="px-3 py-2 rounded-lg text-sm font-medium {text_muted} transition-colors">Kalender Lomba</a>
      <a href="pricing{theme_suffix}" class="px-3 py-2 rounded-lg text-sm font-medium {text_muted} transition-colors">Biaya Bimbingan</a>
      <a href="landing{theme_suffix}#faq" class="px-3 py-2 rounded-lg text-sm font-medium {text_muted} transition-colors">FAQ</a>
    </nav>

    <!-- Right Actions -->
    <div class="flex items-center gap-2 sm:gap-3 shrink-0">
      <!-- Theme Switcher -->
      <div class="flex items-center bg-black/5 dark:bg-white/10 p-1 rounded-full text-xs font-medium">
        <a href="landing-terang.html" class="flex items-center gap-1 px-2.5 py-1 rounded-full {light_btn_cls}">
          <span class="material-symbols-outlined text-[15px]">light_mode</span>
          <span class="hidden sm:inline">Terang</span>
        </a>
        <a href="landing-gelap.html" class="flex items-center gap-1 px-2.5 py-1 rounded-full {dark_btn_cls}">
          <span class="material-symbols-outlined text-[15px]">dark_mode</span>
          <span class="hidden sm:inline">Gelap</span>
        </a>
      </div>

      <!-- Auth CTAs -->
      <a href="login{theme_suffix}" class="hidden sm:inline-flex items-center justify-center px-4 py-2 rounded-xl text-sm font-semibold border border-[#CBD5E1] dark:border-[#334155] {text_main} hover:bg-black/5 dark:hover:bg-white/5 transition-all">
        Masuk
      </a>
      <a href="login{theme_suffix}" class="inline-flex items-center justify-center px-4 py-2 rounded-xl text-sm font-semibold bg-[#D4A747] text-[#0B1E3A] hover:bg-[#c4973b] shadow-sm transition-all">
        Coba Gratis
      </a>

      <!-- Mobile Hamburger Button -->
      <button type="button" onclick="toggleMobileDrawer()" class="lg:hidden p-2 rounded-lg text-[#64748B] dark:text-[#94A3B8] hover:text-[#0B1E3A] dark:hover:text-white" aria-label="Buka Menu">
        <span class="material-symbols-outlined text-[26px]">menu</span>
      </button>
    </div>
  </div>

  <!-- Mobile Slide Drawer -->
  <div id="mobile-public-drawer" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden lg:hidden" onclick="toggleMobileDrawer()">
    <div class="fixed top-0 right-0 w-[280px] h-full {bg_class} shadow-2xl p-6 flex flex-col gap-6" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between pb-4 border-b border-black/10 dark:border-white/10">
        <span class="font-bold text-lg {text_main}">Menu Navigasi</span>
        <button type="button" onclick="toggleMobileDrawer()" class="p-1 rounded-lg text-gray-500 hover:text-gray-800 dark:hover:text-white">
          <span class="material-symbols-outlined text-[24px]">close</span>
        </button>
      </div>
      <nav class="flex flex-col gap-3 font-medium text-base">
        <a href="landing{theme_suffix}#fitur" onclick="toggleMobileDrawer()" class="{text_muted} py-2">Fitur Unggulan</a>
        <a href="daftar-modul{theme_suffix}" class="{text_muted} py-2">Kurikulum & Past Papers</a>
        <a href="prep-timeline{theme_suffix}" class="{text_muted} py-2">Kalender Lomba</a>
        <a href="pricing{theme_suffix}" class="{text_muted} py-2">Biaya Bimbingan</a>
        <a href="landing{theme_suffix}#faq" onclick="toggleMobileDrawer()" class="{text_muted} py-2">FAQ</a>
      </nav>
      <div class="mt-auto flex flex-col gap-3 pt-6 border-t border-black/10 dark:border-white/10">
        <a href="login{theme_suffix}" class="w-full py-2.5 text-center rounded-xl font-semibold border border-[#CBD5E1] dark:border-[#334155] {text_main}">Masuk</a>
        <a href="login{theme_suffix}" class="w-full py-2.5 text-center rounded-xl font-semibold bg-[#D4A747] text-[#0B1E3A]">Daftar Akun Gratis</a>
      </div>
    </div>
  </div>
</header>
<script>
function toggleMobileDrawer() {
  var d = document.getElementById('mobile-public-drawer');
  if (d) d.classList.toggle('hidden');
}
</script>
'''

def get_student_navbar(current_path, is_dark=False):
    theme_suffix = "-gelap.html" if is_dark else "-terang.html"
    bg_class = "bg-[#0B1E3A]/95 border-[#1E293B]" if is_dark else "bg-white/95 border-[#E2E8F0]"
    text_main = "text-white" if is_dark else "text-[#0B1E3A]"
    brand_sub = "text-[#D4A747]"
    light_btn_cls = "bg-white text-[#0B1E3A] shadow-sm font-semibold" if not is_dark else "text-[#94A3B8] hover:text-white"
    dark_btn_cls = "bg-[#0F2444] text-white shadow-sm font-semibold" if is_dark else "text-[#64748B] hover:text-[#0B1E3A]"

    # 5 standard links
    links = [
        ("dashboard", "Beranda", f"dashboard{theme_suffix}"),
        ("daftar-modul", "Modul & Past Papers", f"daftar-modul{theme_suffix}"),
        ("lobby-tryout", "Simulasi Tryout", f"lobby-tryout{theme_suffix}"),
        ("guru-ai", "Tutor Olimpix", f"guru-ai{theme_suffix}"),
        ("prep-timeline", "Kalender Lomba", f"prep-timeline{theme_suffix}"),
    ]
    
    desktop_nav_items = []
    for key, label, href in links:
        is_active = (key == current_path)
        if is_active:
            active_cls = "bg-[#D4A747] text-[#0B1E3A] font-bold shadow-sm"
        else:
            active_cls = "text-[#94A3B8] hover:text-white hover:bg-white/5" if is_dark else "text-[#475569] hover:text-[#0B1E3A] hover:bg-slate-100"
        desktop_nav_items.append(f'<a href="{href}" class="px-3.5 py-1.5 rounded-xl text-sm transition-all {active_cls}">{label}</a>')
    
    desktop_nav_html = "\n      ".join(desktop_nav_items)
    
    # Bottom Nav Items for Mobile
    bottom_nav_items = []
    icon_map = {
        "dashboard": "home",
        "daftar-modul": "menu_book",
        "lobby-tryout": "timer",
        "guru-ai": "psychology",
        "prep-timeline": "calendar_month"
    }
    for key, label, href in links:
        is_active = (key == current_path)
        icon = icon_map.get(key, "circle")
        act_color = "text-[#D4A747] font-bold" if is_active else ("text-[#94A3B8]" if is_dark else "text-[#64748B]")
        short_label = "Modul" if key == "daftar-modul" else ("Tutor" if key == "guru-ai" else ("Kalender" if key == "prep-timeline" else label))
        bottom_nav_items.append(f'''
    <a href="{href}" class="flex flex-col items-center justify-center flex-1 py-1.5 {act_color}">
      <span class="material-symbols-outlined text-[22px]">{icon}</span>
      <span class="text-[11px] tracking-tight">{short_label}</span>
    </a>''')
    bottom_nav_html = "".join(bottom_nav_items)

    return f'''<!-- NAVBAR PORTAL SISWA TERSTANDARISASI (TIPE B) -->
<header class="fixed top-0 left-0 w-full z-50 {bg_class} backdrop-blur-md shadow-sm border-b">
  <div class="max-w-7xl mx-auto h-[72px] px-4 sm:px-6 lg:px-8 flex items-center justify-between gap-4">
    <!-- Logo -->
    <a href="dashboard{theme_suffix}" style="text-decoration:none;" class="flex items-center gap-3 shrink-0">
      <img alt="Medalis Logo" class="h-8 sm:h-9 w-auto object-contain" src="assets/medalis_logo.svg">
      <div class="flex flex-col">
        <span class="font-bold text-lg sm:text-xl tracking-wider {text_main} leading-none">MEDALIS</span>
        <span class="text-[10px] tracking-widest uppercase font-semibold {brand_sub}">Portal Belajar Siswa</span>
      </div>
    </a>

    <!-- Navigasi Tengah Desktop (Seragam 5 Menu Teks Bersih) -->
    <nav class="hidden lg:flex items-center gap-1.5 bg-black/5 dark:bg-white/5 p-1 rounded-2xl border border-black/5 dark:border-white/5">
      {desktop_nav_html}
    </nav>

    <!-- Right Profile & Theme Switcher -->
    <div class="flex items-center gap-2 sm:gap-3 shrink-0">
      <!-- Theme Switcher -->
      <div class="flex items-center bg-black/5 dark:bg-white/10 p-1 rounded-full text-xs font-medium">
        <a href="{current_path}-terang.html" class="flex items-center gap-1 px-2.5 py-1 rounded-full {light_btn_cls}">
          <span class="material-symbols-outlined text-[15px]">light_mode</span>
          <span class="hidden xl:inline">Terang</span>
        </a>
        <a href="{current_path}-gelap.html" class="flex items-center gap-1 px-2.5 py-1 rounded-full {dark_btn_cls}">
          <span class="material-symbols-outlined text-[15px]">dark_mode</span>
          <span class="hidden xl:inline">Gelap</span>
        </a>
      </div>

      <!-- Single Standard Student Chip -->
      <div class="flex items-center gap-2 pl-2 sm:pl-3 border-l border-black/10 dark:border-white/10">
        <div class="w-9 h-9 rounded-full bg-[#0B1E3A] dark:bg-[#D4A747] text-[#D4A747] dark:text-[#0B1E3A] flex items-center justify-center font-bold text-xs select-none shadow-sm">
          AP
        </div>
        <div class="hidden sm:flex flex-col text-left">
          <span class="font-bold text-xs sm:text-sm {text_main} leading-tight">Aisyah</span>
          <span class="text-[11px] text-[#64748B] dark:text-[#94A3B8] leading-tight">Kelas 8 SMP • OSN Madya</span>
        </div>
      </div>
    </div>
  </div>
</header>

<!-- MOBILE BOTTOM NAVIGATION BAR (PORTAL SISWA) -->
<nav class="lg:hidden fixed bottom-0 left-0 right-0 z-50 {bg_class} border-t shadow-[0_-2px_10px_rgba(0,0,0,0.05)] flex items-center justify-around px-2 py-1 safe-area-pb">
  {bottom_nav_html}
</nav>
'''

def get_exam_navbar(is_dark=False):
    theme_suffix = "-gelap.html" if is_dark else "-terang.html"
    bg_class = "bg-[#071324] border-[#1E293B] text-white" if is_dark else "bg-white border-[#E2E8F0] text-[#0B1E3A]"
    
    return f'''<!-- NAVBAR UJIAN CBT TERSTANDARISASI (TIPE C) -->
<header class="sticky top-0 z-50 h-[72px] {bg_class} border-b shadow-sm px-4 sm:px-8 flex items-center justify-between">
  <!-- Sisi Kiri: Logo & Info Mata Uji -->
  <div class="flex items-center gap-4">
    <div class="flex items-center gap-2.5 pr-4 border-r border-black/10 dark:border-white/10">
      <img alt="Medalis Logo" class="h-8 w-auto object-contain" src="assets/medalis_logo.svg">
      <span class="font-bold text-lg tracking-wider hidden sm:inline">MEDALIS</span>
    </div>
    <div class="flex flex-col">
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider bg-[#D4A747]/20 text-[#D4A747] border border-[#D4A747]/30">CBT RESMI</span>
        <span class="font-bold text-xs sm:text-sm tracking-tight">KSNR Matematika SMP</span>
      </div>
      <span class="text-[11px] text-[#64748B] dark:text-[#94A3B8] hidden sm:inline">Simulasi Babak Penyisihan Nasional</span>
    </div>
  </div>

  <!-- Sisi Tengah: Progres & Timer Monospace -->
  <div class="flex items-center gap-3 sm:gap-6">
    <div class="hidden md:flex flex-col items-center">
      <span class="text-[11px] font-medium text-[#64748B] dark:text-[#94A3B8]">Progres Soal</span>
      <span class="font-bold text-xs sm:text-sm text-[#059669]">14 / 40 Terjawab</span>
    </div>
    
    <div class="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-black/5 dark:bg-white/10 border border-black/10 dark:border-white/10">
      <span class="material-symbols-outlined text-[18px] text-[#D4A747]">timer</span>
      <span class="font-mono font-bold text-sm sm:text-base tracking-wider text-red-600 dark:text-red-400" id="live-timer-cbt">01:25:40</span>
    </div>
  </div>

  <!-- Sisi Kanan: Autosave & Tombol Selesai Ujian -->
  <div class="flex items-center gap-2 sm:gap-3">
    <!-- Autosave Local Indicator -->
    <div class="hidden sm:flex items-center gap-1.5 text-xs text-[#059669] font-medium px-2.5 py-1 rounded-lg bg-emerald-500/10">
      <span class="material-symbols-outlined text-[16px]">cloud_done</span>
      <span>Tersimpan di Lokal</span>
    </div>

    <!-- Tombol Selesai Ujian (Marun Berwibawa) -->
    <a href="hasil-tryout{theme_suffix}" class="px-3.5 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-[#881337] text-white hover:bg-[#9f1239] transition-all shadow-sm flex items-center gap-1.5">
      <span>Selesai Ujian</span>
      <span class="material-symbols-outlined text-[16px]">flag</span>
    </a>
  </div>
</header>
'''

print("Navbar templates compiled successfully.")
