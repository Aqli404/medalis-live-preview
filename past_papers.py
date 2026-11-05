def get_past_papers_section(is_dark=False):
    card_bg = "bg-[#0F2444] border-[#1E3A5F]" if is_dark else "bg-white border-[#E2E8F0]"
    text_main = "text-white" if is_dark else "text-[#0B1E3A]"
    text_muted = "text-[#94A3B8]" if is_dark else "text-[#64748B]"
    sub_bg = "bg-white/5" if is_dark else "bg-[#F8FAFC]"
    
    return f'''
<!-- SEKSI BARU: BANK ARSIP SOAL ASLI (PAST PAPERS) DENGAN STRUKTUR BERJENJANG (ALA JAGOTPA) -->
<section class="flex flex-col gap-6 mt-4">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-2 border-b border-black/10 dark:border-white/10">
    <div>
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#D4A747]/15 border border-[#D4A747]/30 text-[#D4A747] text-xs font-bold tracking-wide uppercase mb-2">
        <span class="material-symbols-outlined text-[15px]">lock_open</span>
        Arsip Soal Resmi & Pembahasan 3 Lapis
      </div>
      <h2 class="text-xl sm:text-2xl font-bold {text_main} tracking-tight">Koleksi Past Papers Olimpiade (Tahun 2018–2025)</h2>
      <p class="text-sm {text_muted} mt-1">Bedah analitis soal asli OSN-K, OSN-P, SASMO, AMO, hingga KSNR dengan metode pembuktian formal & trik cepat 10 detik.</p>
    </div>
    
    <div class="flex items-center gap-2">
      <span class="px-3 py-1.5 rounded-xl text-xs font-bold bg-[#D4A747] text-[#0B1E3A] flex items-center gap-1 shadow-sm">
        <span class="material-symbols-outlined text-[16px]">workspace_premium</span>
        FITUR PREMIUM
      </span>
    </div>
  </div>

  <!-- Grid Card Past Papers -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
    
    <!-- Item 1: OSN-K SMP Matematika -->
    <div class="{card_bg} rounded-2xl border p-5 shadow-sm hover:shadow-md transition-all flex flex-col justify-between">
      <div>
        <div class="flex items-center justify-between gap-2 mb-3">
          <span class="px-2.5 py-1 rounded-lg text-xs font-bold bg-blue-500/10 text-blue-600 dark:text-blue-400 border border-blue-500/20">OSN-K (Kabupaten/Kota)</span>
          <span class="text-xs font-bold text-[#D4A747] flex items-center gap-1">
            <span class="material-symbols-outlined text-[15px]">verified</span> 2018–2025
          </span>
        </div>
        <h3 class="text-base font-bold {text_main} leading-snug">Matematika SMP: Aljabar, Modulo & Kombinatorika</h3>
        <p class="text-xs {text_muted} mt-2 line-clamp-2">40 butir soal seleksi asli per tahun disertai penguraian teorema bilangan, kongruensi modulo, dan segitiga pascal.</p>
        
        <div class="mt-4 p-3 rounded-xl {sub_bg} border border-black/5 dark:border-white/5 flex flex-col gap-1.5 text-xs">
          <div class="flex justify-between {text_muted}">
            <span>Cakupan Arsip:</span>
            <span class="font-bold {text_main}">8 Tahun Lengkap</span>
          </div>
          <div class="flex justify-between {text_muted}">
            <span>Siswa Belajar:</span>
            <span class="font-bold text-[#059669]">1.420 Pejuang OSN</span>
          </div>
          <div class="flex justify-between {text_muted}">
            <span>Format Bahasan:</span>
            <span class="font-bold {text_main}">3 Lapis (Konsep, Solusi, Speed-Hack)</span>
          </div>
        </div>
      </div>

      <div class="mt-5 pt-4 border-t border-black/5 dark:border-white/5 flex items-center justify-between">
        <span class="text-xs font-bold text-[#059669] flex items-center gap-1">
          <span class="material-symbols-outlined text-[16px]">task_alt</span> Siap Akses
        </span>
        <a href="ebook-reader{'-gelap.html' if is_dark else '-terang.html'}" class="px-4 py-2 rounded-xl text-xs font-bold bg-[#0B1E3A] dark:bg-[#D4A747] text-white dark:text-[#0B1E3A] hover:opacity-90 transition-all flex items-center gap-1">
          <span>Buka Past Paper</span>
          <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
        </a>
      </div>
    </div>

    <!-- Item 2: SASMO & AMO Internasional -->
    <div class="{card_bg} rounded-2xl border p-5 shadow-sm hover:shadow-md transition-all flex flex-col justify-between">
      <div>
        <div class="flex items-center justify-between gap-2 mb-3">
          <span class="px-2.5 py-1 rounded-lg text-xs font-bold bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20">SASMO & AMO Internasional</span>
          <span class="text-xs font-bold text-[#D4A747] flex items-center gap-1">
            <span class="material-symbols-outlined text-[15px]">verified</span> 2020–2025
          </span>
        </div>
        <h3 class="text-base font-bold {text_main} leading-snug">Singapore & Asian Schools Math Olympiad</h3>
        <p class="text-xs {text_muted} mt-2 line-clamp-2">Arsip bilingual (English-Indonesia) soal penalaran kreatif Section A (Multiple Choice) dan Section B (Non-routine problems).</p>
        
        <div class="mt-4 p-3 rounded-xl {sub_bg} border border-black/5 dark:border-white/5 flex flex-col gap-1.5 text-xs">
          <div class="flex justify-between {text_muted}">
            <span>Cakupan Arsip:</span>
            <span class="font-bold {text_main}">6 Seri Kompetisi</span>
          </div>
          <div class="flex justify-between {text_muted}">
            <span>Siswa Belajar:</span>
            <span class="font-bold text-[#059669]">980 Siswa</span>
          </div>
          <div class="flex justify-between {text_muted}">
            <span>Format Bahasan:</span>
            <span class="font-bold {text_main}">Analisis Soal Tidak Rutin</span>
          </div>
        </div>
      </div>

      <div class="mt-5 pt-4 border-t border-black/5 dark:border-white/5 flex items-center justify-between">
        <span class="text-xs font-bold text-[#059669] flex items-center gap-1">
          <span class="material-symbols-outlined text-[16px]">task_alt</span> Siap Akses
        </span>
        <a href="ebook-reader{'-gelap.html' if is_dark else '-terang.html'}" class="px-4 py-2 rounded-xl text-xs font-bold bg-[#0B1E3A] dark:bg-[#D4A747] text-white dark:text-[#0B1E3A] hover:opacity-90 transition-all flex items-center gap-1">
          <span>Buka Past Paper</span>
          <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
        </a>
      </div>
    </div>

    <!-- Item 3: OSN-P Tingkat Provinsi -->
    <div class="{card_bg} rounded-2xl border p-5 shadow-sm hover:shadow-md transition-all flex flex-col justify-between">
      <div>
        <div class="flex items-center justify-between gap-2 mb-3">
          <span class="px-2.5 py-1 rounded-lg text-xs font-bold bg-purple-500/10 text-purple-600 dark:text-purple-400 border border-purple-500/20">OSN-P (Tingkat Provinsi)</span>
          <span class="text-xs font-bold text-[#D4A747] flex items-center gap-1">
            <span class="material-symbols-outlined text-[15px]">verified</span> Isian & Uraian
          </span>
        </div>
        <h3 class="text-base font-bold {text_main} leading-snug">Geometri Lanjutan & Teori Graf Provinsi</h3>
        <p class="text-xs {text_muted} mt-2 line-clamp-2">Latihan pembuktian analitis teorema Menelaus, Ceva, dan keterbagian aljabar untuk merebut tiket ke babak Nasional.</p>
        
        <div class="mt-4 p-3 rounded-xl {sub_bg} border border-black/5 dark:border-white/5 flex flex-col gap-1.5 text-xs">
          <div class="flex justify-between {text_muted}">
            <span>Cakupan Arsip:</span>
            <span class="font-bold {text_main}">Uraian 2019–2025</span>
          </div>
          <div class="flex justify-between {text_muted}">
            <span>Siswa Belajar:</span>
            <span class="font-bold text-[#059669]">620 Kandidat Provinsi</span>
          </div>
          <div class="flex justify-between {text_muted}">
            <span>Format Bahasan:</span>
            <span class="font-bold {text_main}">Rubrik Penilaian Esai Puspresnas</span>
          </div>
        </div>
      </div>

      <div class="mt-5 pt-4 border-t border-black/5 dark:border-white/5 flex items-center justify-between">
        <span class="text-xs font-bold text-[#D4A747] flex items-center gap-1">
          <span class="material-symbols-outlined text-[16px]">lock</span> Khusus Member
        </span>
        <a href="pricing{'-gelap.html' if is_dark else '-terang.html'}" class="px-4 py-2 rounded-xl text-xs font-bold bg-[#D4A747] text-[#0B1E3A] hover:bg-[#c4973b] transition-all flex items-center gap-1">
          <span>Buka Akses Premium</span>
          <span class="material-symbols-outlined text-[15px]">lock_open</span>
        </a>
      </div>
    </div>

  </div>
</section>
'''

print("Past papers component compiled successfully.")
