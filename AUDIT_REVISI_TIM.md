# AUDIT REVISI TIM PROTOTYPE STATIS MEDALIS
**Tanggal Audit:** 09 November 2026  
**Status:** FASE 0 SELESAI — STOP-GATE (Menunggu Persetujuan Sebelum Edit)

---

## 1. Pemetaan Alur & Masalah Navigasi (Guest vs Portal)

### A. Temuan Header & Avatar Siswa "Aisyah"
Saat ini terdapat inkonsistensi header antara halaman publik dan halaman fitur:
1. **Landing Page (`landing-terang.html` & `landing-gelap.html`):**
   - **Status:** SUDAH TIPE A GUEST MURNI.
   - Sisi kanan: Tombol *Masuk* dan *Coba Gratis*, tanpa avatar atau nama siswa (baris 52-60).
2. **Daftar Modul (`daftar-modul-terang.html` & `daftar-modul-gelap.html`):**
   - **Status:** SAAT INI MEMAKAI HEADER TIPE B (PORTAL SISWA).
   - Menampilkan chip profil personal: `AP - Aisyah | Kelas 8 SMP • OSN Madya` (baris 53-61).
   - Jika pengguna umum / guest membuka tautan "Modul Belajar" langsung dari landing page, mereka bingung karena seolah-olah sudah login sebagai Aisyah.
3. **Kalender Lomba (`prep-timeline-terang.html` & `prep-timeline-gelap.html`):**
   - **Status:** MEMAKAI HEADER TIPE B (PORTAL SISWA).
   - Menampilkan chip profil personal Aisyah dan nomor WhatsApp pribadi `+62 812-••••-8819` di banner pengingat.

### B. Solusi Arsitektur Header
- Sediakan mode/kondisi **Guest View** untuk katalog modul publik dan kalender kompetisi publik:
  - Menu kanan menampilkan tombol `Masuk` & `Daftar Gratis` (Pola Ruangguru).
  - Chip avatar Aisyah hanya aktif jika diakses dari dalam dashboard siswa (`dashboard-terang.html`).

---

## 2. Inventaris Customer Service (WhatsApp Admin Langsung)

### A. Nomor WhatsApp yang Ditemukan di Proyek
1. `landing-terang.html` & `landing-gelap.html` (Seksi Konsultan Pendidikan & Share Paket):
   - `https://wa.me/6281234567890?text=Halo%20Medalis,%20saya%20ingin%20konsultasi%20bimbingan%20olimpiade%20anak`
2. `pricing-gelap.html` (Konsultasi Paket):
   - `https://wa.me/6281288888821`

### B. Tindakan Perapian CS
- Standarisasi **1 Nomor Utama Admin Resmi** menggunakan `wa.me/6281234567890` (atau nomor resmi yang Mas tentukan).
- Pasang **Floating Action Button (FAB) WhatsApp CS** di pojok kanan bawah (`bottom-6 right-6 z-40`) yang ramah pengguna mobile & desktop di seluruh halaman publik/katalog.

---

## 3. Audit UI Modul Eksisting & Aturan "2 Modul Gratis per Paket"

### A. Kondisi UI Modul Saat Ini (`daftar-modul-terang.html` & `daftar-modul-gelap.html`)
- **Struktur Saat Ini:**
  - Menampilkan 6 kartu bab dalam 1 grid flat:
    - Bab 01: Aljabar (Label: `GRATIS`, Akses: Buka Ebook)
    - Bab 02: Teori Bilangan (Label: `GRATIS`, Akses: Buka Ebook)
    - Bab 03: Geometri (Label: `PREMIUM`, Akses: Kunci / Arahkan ke Biaya)
    - Bab 04: Kombinatorika (Label: `PREMIUM`, Akses: Kunci / Arahkan ke Biaya)
    - Bab 05: Pertidaksamaan (Label: `PREMIUM`, Akses: Kunci / Arahkan ke Biaya)
    - Bab 06: Fungsi Polinomial (Label: `PREMIUM`, Akses: Kunci / Arahkan ke Biaya)
  - Di bawahnya ada seksi arsip *Past Papers* (OSN-K SMP, SASMO, dll).
- **Kekurangan Sesuai Feedback Tim ("Dirapiin Ae UI-nya & Per Paket"):**
  - Modul saat ini belum dikelompokkan secara tegas **per paket kurikulum** (misal: *Paket OSN Matematika SMP*, *Paket SASMO Internasional*, *Paket IPA Terpadu*).
  - Aturan *"Modul 1-2 free sisanya VIP"* harus diterapkan konsisten pada setiap paket/kategori modul, bukan hanya 2 bab pertama di bab 1.

---

## 4. Analisis Referensi Kompetisi `posi.id/competitions`

### A. Struktur Nyata yang Diekstrak dari `posi.id/competitions`
Dari hasil inspeksi live DOM halaman POSI, struktur kartu kompetisi yang efektif terdiri dari:
1. **Banner visual/thumbnail lomba** dengan rasio 16:9 atau kartu vertikal rapi.
2. **Badge Status & Biaya (Pojok/Atas):** `GRATIS • Rp 50.000` atau `Pendaftaran Dibuka` + Badge Mode (`Online` / `Offline`).
3. **Badge Jenjang & Bidang:** Pill jenjang terpisah yang jelas (`SD`, `SMP`, `SMA`) + jumlah mata lomba/bidang (misal: `Matematika`, `Fisika`, `IPA`).
4. **Informasi Tanggal & Waktu:** Tanggal pelaksanaan kompetisi dan batas akhir pendaftaran.
5. **Aksi Ganda (Action Buttons):**
   - Tombol Sekunder: `Juknis` (Unduh Panduan/Silabus).
   - Tombol Bantuan: `Hubungi Admin` (WhatsApp).
   - Tombol Utama: `Lihat Detail` / `Daftar Sekarang`.

### B. Adaptasi ke Desain Medalis
- **Yang Diadopsi:** Hierarki informasi di atas (Badge Status, Pill Jenjang, Tanggal Penting, Tombol Juknis + Daftar).
- **Yang Tetap Mengikuti Brand Medalis:**
  - Token warna resmi: Navy `#0B1E3A`, Gold `#D4A747`, Cream `#F7F5EE` (Bukan biru langit POSI).
  - Tipografi: Poppins & sans-serif bersih Medalis.
  - Kartu beradius `rounded-2xl` dengan border subtle `#E2E8F0` / dark `#1E293B`.

---

## 5. Usulan Task Baru di TASKS.md

Sesuai aturan urutan proyek, dibuat 1 task atomik terkonsolidasi baru untuk fase prototype:
* **`T-23: Refinement UI/UX Prototype Statis (Guest Header, Floating CS WA, Grid Modul Per-Paket, & Kalender Lomba Pola POSI)`**
  - **Scope:**
    1. Update header `daftar-modul` dan `prep-timeline` agar ramah guest (tombol Masuk/Daftar) jika dibuka dari publik.
    2. Tambahkan Floating Button WhatsApp CS resmi (`wa.me/6281234567890`) di halaman publik prototype.
    3. Rapikan layout `daftar-modul` menjadi tata letak **Per-Paket** dengan aturan tegas: Modul 1 & 2 Gratis, Modul 3+ VIP Berlangganan.
    4. Perbarui seksi kompetisi di `prep-timeline` mengadopsi hierarki POSI (Badge Jenjang, Tanggal Penting, Tombol Juknis & Daftar) dalam tema Medalis.
  - **Di Luar Scope:**
    - Tidak mengubah backend Next.js / Supabase / Redis.
    - Tidak membuat halaman artikel berita.
    - Tidak membuat integrasi payment gateway palsu atau alur n8n.
  - **Validasi:** Pengujian visual desktop (1280px) & mobile (375px) di tema terang dan gelap.

---

**STOP GATE:** Dokumen audit ini siap direview. Approval diminta sebelum melanjutkan ke eksekusi edit file HTML.
