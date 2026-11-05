def get_calendar_section(is_dark=False):
    card_bg = "bg-[#0F2444] border-[#1E3A5F]" if is_dark else "bg-white border-[#E2E8F0]"
    text_main = "text-white" if is_dark else "text-[#0B1E3A]"
    text_muted = "text-[#94A3B8]" if is_dark else "text-[#64748B]"
    sub_bg = "bg-white/5" if is_dark else "bg-[#F8FAFC]"
    theme_suffix = "-gelap.html" if is_dark else "-terang.html"

    return f'''
<!-- SEKSI BARU: PUSAT KALENDER AGENDA LOMBA & NOTIFIKASI WHATSAPP BUNDA -->
<div class="flex flex-col gap-8 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">

  <!-- Header Kalender Lomba -->
  <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-6 pb-6 border-b border-black/10 dark:border-white/10">
    <div>
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#D4A747]/15 border border-[#D4A747]/30 text-[#D4A747] text-xs font-bold tracking-wide uppercase mb-3">
        <span class="material-symbols-outlined text-[16px]">calendar_month</span>
        Kalender Agenda Resmi Olimpiade 2026
      </div>
      <h1 class="text-2xl sm:text-3xl font-extrabold {text_main} tracking-tight">Pusat Jadwal Kompetisi Sains & Panduan Pendaftaran</h1>
      <p class="text-sm sm:text-base {text_muted} mt-2 max-w-3xl">Pantau seluruh tanggal penting seleksi nasional & internasional (OSN, SASMO, AMO, KSNR). Unduh juknis resmi dan aktifkan bot pengingat WhatsApp agar tidak terlewat berkas.</p>
    </div>

    <!-- Banner Sinkronisasi WhatsApp -->
    <div class="{card_bg} rounded-2xl border p-4 shadow-sm flex items-center gap-4 shrink-0">
      <div class="w-12 h-12 rounded-xl bg-emerald-500/10 text-[#059669] flex items-center justify-center shrink-0">
        <span class="material-symbols-outlined text-[28px]">chat</span>
      </div>
      <div class="flex flex-col">
        <div class="flex items-center gap-2">
          <span class="text-xs font-bold text-[#059669] flex items-center gap-1">
            <span class="w-2 h-2 rounded-full bg-[#059669] animate-pulse"></span> BOT WA AKTIF
          </span>
        </div>
        <span class="font-bold text-sm {text_main}">Pengingat WhatsApp Bunda</span>
        <span class="text-xs {text_muted}">Nomor: +62 812-••••-8819</span>
      </div>
    </div>
  </div>

  <!-- Daftar Event Lomba Utama -->
  <div class="flex flex-col gap-6">

    <!-- EVENT 1: OSN-K 2026 (Penyisihan Kabupaten/Kota) -->
    <div class="{card_bg} rounded-2xl border p-6 shadow-sm flex flex-col gap-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-black/5 dark:border-white/5">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-blue-500/10 text-blue-600 dark:text-blue-400 font-bold flex items-center justify-center text-sm">
            01
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded text-[10px] font-bold uppercase bg-blue-500/10 text-blue-600 dark:text-blue-400 border border-blue-500/20">Seleksi Nasional</span>
              <span class="text-xs font-bold text-emerald-600 dark:text-emerald-400">Pendaftaran Dibuka</span>
            </div>
            <h2 class="text-lg sm:text-xl font-bold {text_main}">OSN-K 2026 (Olimpiade Sains Nasional Tingkat Kota/Kabupaten)</h2>
          </div>
        </div>

        <!-- Toggle Switch WhatsApp Reminder -->
        <label class="flex items-center gap-3 cursor-pointer select-none bg-black/5 dark:bg-white/5 px-4 py-2 rounded-xl">
          <div class="flex flex-col text-right">
            <span class="text-xs font-bold {text_main}">Ingatkan via WhatsApp</span>
            <span class="text-[10px] {text_muted}">Kirim notif H-7 & H-1</span>
          </div>
          <input type="checkbox" checked class="w-5 h-5 accent-[#059669] rounded cursor-pointer">
        </label>
      </div>

      <!-- Milestone Timeline Card -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
        <div class="p-4 rounded-xl {sub_bg} border border-black/5 dark:border-white/5">
          <span class="font-bold text-[#D4A747] uppercase tracking-wider block mb-1">Tahap 1: Registrasi</span>
          <span class="font-bold text-sm {text_main} block">1 - 25 Maret 2026</span>
          <span class="{text_muted} block mt-1">Unggah berkas fakta integritas & surat rekomendasi kepsek.</span>
        </div>

        <div class="p-4 rounded-xl {sub_bg} border border-black/5 dark:border-white/5">
          <span class="font-bold text-[#D4A747] uppercase tracking-wider block mb-1">Tahap 2: Simulasi CBT</span>
          <span class="font-bold text-sm {text_main} block">10 - 12 April 2026</span>
          <span class="{text_muted} block mt-1">Uji coba aplikasi ujian daring resmi nasional.</span>
        </div>

        <div class="p-4 rounded-xl {sub_bg} border border-emerald-500/30 bg-emerald-500/5">
          <span class="font-bold text-[#059669] uppercase tracking-wider block mb-1">Tahap 3: Hari-H Lomba</span>
          <span class="font-bold text-sm text-[#059669] block">14 Mei 2026</span>
          <span class="{text_muted} block mt-1">Babak penyisihan serentak sesi pagi (08:30 WIB).</span>
        </div>

        <div class="p-4 rounded-xl {sub_bg} border border-black/5 dark:border-white/5">
          <span class="font-bold text-[#D4A747] uppercase tracking-wider block mb-1">Tahap 4: Pengumuman</span>
          <span class="font-bold text-sm {text_main} block">28 Mei 2026</span>
          <span class="{text_muted} block mt-1">Rilis SK lolos ke tingkat provinsi (OSN-P).</span>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex flex-wrap items-center justify-between gap-3 pt-3 border-t border-black/5 dark:border-white/5">
        <div class="flex flex-wrap items-center gap-2">
          <a href="https://pusatprestasinasional.kemdikbud.go.id" target="_blank" class="px-3.5 py-2 rounded-xl text-xs font-semibold border border-black/10 dark:border-white/10 {text_main} hover:bg-black/5 dark:hover:bg-white/5 flex items-center gap-1.5 transition-colors">
            <span class="material-symbols-outlined text-[16px]">open_in_new</span>
            <span>Portal Registrasi Resmi</span>
          </a>
          <a href="daftar-modul{theme_suffix}" class="px-3.5 py-2 rounded-xl text-xs font-semibold border border-[#D4A747]/30 text-[#D4A747] bg-[#D4A747]/10 hover:bg-[#D4A747]/20 flex items-center gap-1.5 transition-colors">
            <span class="material-symbols-outlined text-[16px]">download</span>
            <span>Unduh Juknis & Silabus PDF</span>
          </a>
        </div>

        <a href="lobby-tryout{theme_suffix}" class="px-4 py-2 rounded-xl text-xs font-bold bg-[#D4A747] text-[#0B1E3A] hover:bg-[#c4973b] shadow-sm flex items-center gap-1.5 transition-all">
          <span>Latihan Sesuai Silabus Ini</span>
          <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
        </a>
      </div>
    </div>

    <!-- EVENT 2: SASMO 2026 (Kompetisi Internasional) -->
    <div class="{card_bg} rounded-2xl border p-6 shadow-sm flex flex-col gap-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-black/5 dark:border-white/5">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400 font-bold flex items-center justify-center text-sm">
            02
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded text-[10px] font-bold uppercase bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20">Kompetisi Asia & Global</span>
              <span class="text-xs font-bold text-[#D4A747]">Segera Dimulai</span>
            </div>
            <h2 class="text-lg sm:text-xl font-bold {text_main}">SASMO 2026 (Singapore and Asian Schools Math Olympiad)</h2>
          </div>
        </div>

        <label class="flex items-center gap-3 cursor-pointer select-none bg-black/5 dark:bg-white/5 px-4 py-2 rounded-xl">
          <div class="flex flex-col text-right">
            <span class="text-xs font-bold {text_main}">Ingatkan via WhatsApp</span>
            <span class="text-[10px] {text_muted}">Kirim notif H-7 & H-1</span>
          </div>
          <input type="checkbox" checked class="w-5 h-5 accent-[#059669] rounded cursor-pointer">
        </label>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
        <div class="p-4 rounded-xl {sub_bg} border border-black/5 dark:border-white/5">
          <span class="font-bold text-[#D4A747] uppercase tracking-wider block mb-1">Tahap 1: Batas Akhir Daftar</span>
          <span class="font-bold text-sm {text_main} block">20 Maret 2026</span>
          <span class="{text_muted} block mt-1">Registrasi individu / kolektif sekolah via SIMCC.</span>
        </div>

        <div class="p-4 rounded-xl {sub_bg} border border-black/5 dark:border-white/5">
          <span class="font-bold text-[#D4A747] uppercase tracking-wider block mb-1">Tahap 2: Uji Coba Platform</span>
          <span class="font-bold text-sm {text_main} block">28 Maret 2026</span>
          <span class="{text_muted} block mt-1">Simulasi portal daring ujian berbasis iPad / Laptop.</span>
        </div>

        <div class="p-4 rounded-xl {sub_bg} border border-emerald-500/30 bg-emerald-500/5">
          <span class="font-bold text-[#059669] uppercase tracking-wider block mb-1">Tahap 3: Hari-H Ujian</span>
          <span class="font-bold text-sm text-[#059669] block">11 April 2026</span>
          <span class="{text_muted} block mt-1">Pengerjaan 25 soal penalaran berdurasi 90 menit.</span>
        </div>

        <div class="p-4 rounded-xl {sub_bg} border border-black/5 dark:border-white/5">
          <span class="font-bold text-[#D4A747] uppercase tracking-wider block mb-1">Tahap 4: Hasil & Medali</span>
          <span class="font-bold text-sm {text_main} block">Mei 2026</span>
          <span class="{text_muted} block mt-1">Kualifikasi menuju IJMO & SIMOC Singapura.</span>
        </div>
      </div>

      <div class="flex flex-wrap items-center justify-between gap-3 pt-3 border-t border-black/5 dark:border-white/5">
        <div class="flex flex-wrap items-center gap-2">
          <a href="https://sasmo.sg" target="_blank" class="px-3.5 py-2 rounded-xl text-xs font-semibold border border-black/10 dark:border-white/10 {text_main} hover:bg-black/5 dark:hover:bg-white/5 flex items-center gap-1.5 transition-colors">
            <span class="material-symbols-outlined text-[16px]">open_in_new</span>
            <span>Website Resmi SASMO</span>
          </a>
          <a href="daftar-modul{theme_suffix}" class="px-3.5 py-2 rounded-xl text-xs font-semibold border border-[#D4A747]/30 text-[#D4A747] bg-[#D4A747]/10 hover:bg-[#D4A747]/20 flex items-center gap-1.5 transition-colors">
            <span class="material-symbols-outlined text-[16px]">download</span>
            <span>Silabus & Contoh Soal PDF</span>
          </a>
        </div>

        <a href="lobby-tryout{theme_suffix}" class="px-4 py-2 rounded-xl text-xs font-bold bg-[#D4A747] text-[#0B1E3A] hover:bg-[#c4973b] shadow-sm flex items-center gap-1.5 transition-all">
          <span>Latihan Soal SASMO</span>
          <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
        </a>
      </div>
    </div>

  </div>
</div>
'''

print("Calendar section component ready.")
