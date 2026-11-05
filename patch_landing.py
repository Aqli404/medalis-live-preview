import re

def update_landing_content(html, is_dark=False):
    # 1. Kicker & Tagline Universal
    # Ganti Kicker
    html = re.sub(
        r'PLATFORM\s+PERSIAPAN\s+OLIMPIADE\s+NASIONAL\s*\([^)]*\)',
        'AKADEMI PERSIAPAN OLIMPIADE SAINS DAN MATEMATIKA',
        html, flags=re.I
    )
    # Ganti Headline
    html = re.sub(
        r'<h1[^>]*?>\s*TEMPAT\s+PARA\s*&nbsp;\s*JUARA\s+BERTUMBUH\s*</h1>',
        '<h1 class="font-headline-xl text-headline-xl text-[#0B1E3A] dark:text-white font-extrabold tracking-tight leading-[1.15]">BIMBINGAN INTENSIF & SIMULASI CBT<br><span class="text-[#D4A747]">MENUJU PODIUM EMAS OLIMPIADE</span></h1>',
        html, flags=re.I
    )
    # Ganti Sub-headline
    html = re.sub(
        r'Bimbingan\s+Olimpiade\s+&\s+simulasi\s+ujian\s+CBT\s+berstandar\s+Puspresnas[^<]*',
        'Kurikulum penalaran adaptif berstandar kompetisi sains nasional hingga internasional (OSN, SASMO, AMO, hingga KSNR) untuk mengantarkan ananda meraih medali kejuaraan dari jenjang usia dini hingga lanjutan.',
        html, flags=re.I
    )
    
    # 2. Hapus total frasa "Bukan Mentor Manusia" & bersihkan kata "AI"
    html = re.sub(r'Olimpix\s+AI\s*\(Bukan\s+Mentor\s+Manusia\)', 'Tutor Penalaran Interaktif (Olimpix Engine)', html, flags=re.I)
    html = re.sub(r'Bukan\s+Mentor\s+Manusia', 'Tutor Penalaran Interaktif', html, flags=re.I)
    html = re.sub(r'Guru\s+AI:', 'Tutor Nalar:', html, flags=re.I)
    html = re.sub(r'Olimpix\s+AI', 'Olimpix Engine', html)
    html = re.sub(r'Guru\s+Olimpix\s+AI', 'Tutor Olimpix', html)

    # 3. FAQ: Bersihkan pertanyaan kaku ketiadaan mentor manusia
    faq_old = r'Apakah\s+ada\s+mentor\s+manusia\s+di\s+platform\s+ini\?'
    faq_new = 'Bagaimana metode pendampingan belajar di Medalis?'
    html = re.sub(faq_old, faq_new, html, flags=re.I)
    
    faq_ans_old = r'Tidak\s+ada\.\s+Pendampingan\s+di\s+Medalis\s+sepenuhnya\s+digerakkan\s+oleh[^<]*'
    faq_ans_new = 'Ananda didampingi oleh Tutor Penalaran Interaktif (Olimpix Engine) yang dirancang khusus membimbing logika berpikir secara bertahap tanpa membocorkan jawaban instan. Siswa bebas berlatih mandiri 24 jam dengan ritme belajarnya sendiri, didukung diagnosis penguasaan konsep yang dilaporkan otomatis ke WhatsApp orang tua setiap pekan.'
    html = re.sub(faq_ans_old, faq_ans_new, html, flags=re.I)

    # 4. Ganti Puspresnas RI di trust badge dengan cakupan global
    html = re.sub(r'✓\s*Standar\s+Puspresnas\s+RI', '✓ Standar OSN & Kompetisi Internasional (SASMO/AMO)', html)
    html = re.sub(r'✓\s*AI\s+Olimpix\s+AI\s+Tanpa\s+Webcam', '✓ Simulasi CBT Anti-Cemas Tanpa Webcam', html)
    html = re.sub(r'Bank\s+soal\s+terstandarisasi\s+Puspresnas\s+RI,\s*KSNR,\s*SASMO,\s*hingga\s*FISO', 'Bank soal resmi OSN Nasional, SASMO, AMO, KSNR, hingga FISO Internasional', html)

    return html

print("Landing content transformer ready.")
