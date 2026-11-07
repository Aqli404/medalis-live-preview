# PROMPT PERBAIKAN MEDALIS — REVISI KLIEN (WhatsApp, 5 Poin)

Bahan: rekaman chat klien (video 24 detik, tanpa audio) + audit langsung 20 halaman di `https://aqli404.github.io/medalis-live-preview` (repo: `Aqli404/medalis-live-preview`, folder lokal `/root/medalis-live-preview`).

---

## RINGKASAN REVISI KLIEN (kutipan asli)

| # | Kutipan klien | Lokasi di preview | Tingkat |
|---|---|---|---|
| R1 | "bahasanya terlalu tinggi buat emak emak" | landing-terang/gelap, lobby-tryout, lembar-tryout, state-offline | Kritis |
| R2 | "dipersingkat misal: Tutor Onlinemu / Guru Onlinemu / Tutor Interaktif" | semua halaman (86 kemunculan "Olimpix Engine") | Tinggi |
| R3 | "kalimatnya kak sulit: mendingan Cara cepat untuk..." | landing, guru-ai, pembahasan (24 kemunculan "Speed-Hack") | Tinggi |
| R4 | "aplikasi kita kebanyakan full tulisan" + "di awal" + screenshot "Pilih Kelas" 1–12 | seluruh situs (8.183 kata, 50 gambar) | Kritis |
| R5 | "Tampilannya kita sesuaikan lagi dengan referensi ruang guru ka" | seluruh situs | Tinggi |

Yang klien SUKAI dan wajib dipertahankan: kartu **Pengingat WhatsApp Bunda** (komentar "ini oke banget").

---

## BATASAN YANG TIDAK BOLEH DILANGGAR

1. **Dilarang meniru Ruangguru secara harfiah.** Ambil struktur dan pola visualnya, bukan identitasnya. Medalis tetap memakai palet resmi: Navy `#0F172A`, Emas `#D97706`, Cream `#F8FAFC`, Emerald, Amber.
2. **Dilarang menambahkan video pembelajaran.** Prinsip bisnis Medalis 100% bebas video streaming. Kalau merujuk Ruangguru, ambil grid ikon dan kartu kelas, bukan player video.
3. **Dilarang menghapus atau melemahkan fitur** yang sudah ada: CBT anti-putus, laporan WhatsApp mingguan, Speed-Hack, Past Papers.
4. **Dilarang memakai label "AI" di etalase publik** sesuai keputusan sebelumnya. Tapi juga dilarang menyembunyikan bahwa tutor bukan manusia. Penjelasan jujur ditaruh di FAQ dan onboarding.
5. **Wajib patuh DESIGN.md:** font Poppins (UI) + JetBrains Mono (angka timer), touch target minimal 48px (TK: 64px), dark mode via `next-themes`, `overflow-x: hidden` di root.
6. **Wajib mobile-first.** Semua perubahan harus enak dilihat di lebar 360px sebelum diuji di 1440px.
7. **Dilarang simbol LaTeX mentah** ($, \rightarrow, \frac) tampil di teks UI. Formula wajib lewat KaTeX.

---

## R1 — TURUNKAN BAHASA KE LEVEL ORANG TUA

### Temuan konkret
Teks paling parah ada di landing page, blok "Ketahanan CBT":

> "Didukung arsitektur toleransi IndexedDB lokal dengan penyimpanan otomatis setiap 3 detik. Jawaban tetap tersimpan utuh kendati jaringan mati total, disertai deteksi ketat batas tab-switch (maksimal 3x) guna menjamin integritas olimpiade."

Selain itu, istilah teknis bocor di halaman publik:
- `IndexedDB` — 3 halaman (landing, lobby-tryout, lembar-tryout)
- `tab-switch` — 3 halaman
- `toleransi` (arti teknis) — 3 halaman
- `arsitektur`, `infrastruktur`, `sinkronisasi`, `protokol`, `autosave`, `cache` — tersebar di 8 halaman
- `Metode Dialektika` — 7 kali

### Perbaikan yang diminta

**Ganti semua istilah teknis dengan bahasa sehari-hari. Tabel wajib dipakai:**

| Istilah sekarang | Ganti jadi |
|---|---|
| IndexedDB lokal | simpanan di HP/laptop ananda |
| arsitektur toleransi | sistem yang tahan gangguan |
| tab-switch | pindah ke aplikasi lain |
| autosave / penyimpanan otomatis 3 detik | tersimpan sendiri tiap 3 detik |
| sinkronisasi | penyesuaian data |
| protokol | aturan |
| cache | simpanan sementara |
| infrastruktur ujian | sistem ujian |
| integritas olimpiade | kejujuran ujian |
| deteksi ketat | pengawasan |
| Metode Dialektika | cara belajar tanya-jawab |
| Tutor Penalaran Interaktif | lihat R2 |

**Contoh penulisan ulang — kalimat yang dikeluhkan klien:**

Sebelum:
> "Didukung arsitektur toleransi IndexedDB lokal dengan penyimpanan otomatis setiap 3 detik. Jawaban tetap tersimpan utuh kendati jaringan mati total, disertai deteksi ketat batas tab-switch (maksimal 3x) guna menjamin integritas olimpiade."

Sesudah:
> **"Jawaban ananda tidak akan hilang, walau internet mati."**
> Setiap jawaban langsung tersimpan di perangkat, jadi kalau koneksi terputus di tengah ujian, pekerjaan ananda tetap utuh dan bisa dilanjutkan. Sistem juga mencatat bila ananda berpindah ke aplikasi lain saat ujian berlangsung.

**Aturan gaya bahasa untuk seluruh situs:**
- Satu paragraf maksimal **2 kalimat**. Kalau lebih, pecah.
- Kalimat maksimal **20 kata**.
- Dilarang memakai kata serapan teknis yang tidak dipakai orang tua sehari-hari.
- Sebut anak sebagai **"ananda"** atau **"anak Bunda"**, bukan "siswa" di halaman publik (siswa boleh dipakai di area portal).
- Dilarang total: "arsitektur", "infrastruktur", "toleransi", "integritas", "deterministik", "enumerasi", "payload", "render", "endpoint".

### Bug teks yang wajib diperbaiki sekalian
Di `landing-terang.html` dan `landing-gelap.html` ada judul rusak:
```
Ketahanan CBT Server dns Tryout Anti-Putus
```
Kata **"dns"** adalah sisa dari "Serverless dan" yang terpotong. Perbaiki jadi:
```
Tryout Anti-Putus — Ujian Tetap Jalan Walau Internet Mati
```

### File yang disentuh
`landing-terang.html`, `landing-gelap.html`, `lobby-tryout-*.html`, `lembar-tryout-*.html`, `state-offline-*.html`, `state-anti-cheat-*.html`, `dashboard-*.html`, `login-*.html`, `onboarding-*.html`, `hasil-tryout-*.html`

### Cara verifikasi
Jalankan pencarian di seluruh file. Hasil harus nol:
```
grep -ri "IndexedDB\|tab-switch\|tab switch\|arsitektur\|infrastruktur\|protokol\|sinkronisasi\|deterministik\|Metode Dialektika\|Server dns" *.html
```

---

## R2 — PERSINGKAT NAMA TUTOR

### Temuan
Istilah `Olimpix Engine` muncul **86 kali** di seluruh halaman, plus `Tutor Penalaran Interaktif` 4 kali.

### Perbaikan yang diminta

**Nama resmi baru di semua antarmuka: `Tutor Interaktif`**

Dengan varian kontekstual:

| Konteks | Sebutan |
|---|---|
| Menu navbar dan judul halaman | **Tutor Interaktif** |
| Tombol aksi ("Tanya Tutor Interaktif") | **Tutor Interaktif** |
| Kartu landing page | **Tutor Interaktif** + satu baris penjelas |
| Avatar di ruang chat | **Tutor Interaktif** (hilangkan "Olimpix Engine") |
| Nama file (kalau menyentuh navigasi) | boleh tetap `guru-ai-*.html` untuk menghindari broken link |

`Olimpix Engine` dan `Tutor Penalaran Interaktif` **dihapus dari seluruh teks yang dilihat pengguna**. Boleh tetap dipakai di komentar kode internal.

**Penjelas di bawah nama (wajib ada, satu baris):**
> "Pendamping belajar yang membimbing lewat pertanyaan, bukan memberi jawaban langsung."

**Di FAQ landing page, tambahkan satu pertanyaan jujur:**
> **"Tutornya manusia atau sistem?"**
> "Tutor Interaktif adalah sistem pendamping belajar berbasis kecerdasan buatan, bukan guru manusia. Ia membimbing ananda lewat pertanyaan agar menemukan jawaban sendiri. Naskah soal dan pembahasannya disusun tim akademik Medalis."

Kalimat terakhir hanya boleh dipakai **jika benar** tim akademik memang menyusun dan memeriksa soal. Kalau belum, hapus bagian itu.

**Aturan bahasa di ruang chat:** hilangkan kata "Dialektika" di semua tempat. Ganti chip "Metode Dialektika Olimpix" menjadi **"Belajar Bertahap"**.

### File yang disentuh
Semua 41 file HTML (20 pasang terang/gelap + index), kecuali `tk-*` yang teksnya minim.

### Cara verifikasi
```
grep -ri "Olimpix Engine\|Tutor Penalaran Interaktif\|Metode Dialektika\|dialektika" *.html
```
Harus nol di area teks tampil.

---

## R3 — SEDERHANAKAN KALIMAT SPEED-HACK

### Temuan
Kalimat yang dikeluhkan klien:
> "Pintas kalkulasi tanpa kalkulator untuk menghemat alokasi waktu babak penyisihan kompetisi sains."

### Perbaikan yang diminta

**Judul kartu:** tetap `⚡ Cara Cepat 10 Detik` (ganti dari `OLYMPIAD SPEED-HACK 10 Detik`).

Struktur kartu baru — tiga baris saja, tidak lebih:

```
⚡ CARA CEPAT 10 DETIK
[Nama metode, misal: Akar Cepat Newton]

Untuk apa: [satu kalimat, maksimal 12 kata]
Caranya:   [rumus KaTeX, satu baris]
```

**Contoh penulisan ulang untuk kartu Newton-Raphson:**

Sebelum:
> Judul: Aproksimasi Akar Newton-Raphson
> Deskripsi: Pintas kalkulasi tanpa kalkulator untuk menghemat alokasi waktu babak penyisihan kompetisi sains.
> Catatan: Selesai dalam 10 detik tanpa kertas buram

Sesudah:
> Judul: **Akar Cepat Newton**
> Untuk apa: **Menebak akar kuadrat dalam 10 detik, tanpa kalkulator.**
> Caranya: rumus KaTeX
> Contoh: **Akar dari 40 kira-kira 6,3.**
> Penutup: **Cukup 10 detik, tanpa kertas buram.**

**Aturan penulisan semua kartu:**
- Dilarang memakai kata "aproksimasi", "kalkulasi", "alokasi", "penyisihan" di halaman publik.
- Pakai: "kira-kira", "hitung cepat", "waktu ujian", "babak pertama".
- Setiap kartu wajib punya **satu contoh angka nyata**, bukan cuma rumus.
- Deskripsi maksimal **12 kata**.

### File yang disentuh
`landing-*.html`, `guru-ai-*.html`, `pembahasan-*.html`, `daftar-modul-*.html`

### Cara verifikasi
```
grep -ri "Speed-Hack\|SPEED-HACK\|Aproksimasi\|Pintas kalkulasi" *.html
```
Harus nol di teks tampil.

---

## R4 — KURANGI TULISAN, TAMBAH VISUAL, PILIH KELAS DI AWAL

Ini revisi terbesar dan yang paling berpengaruh ke persepsi orang tua.

### Bukti angka kenapa klien benar

| Halaman | Jumlah kata | Gambar raster |
|---|---|---|
| landing-terang | 1.223 | 4 |
| ebook-reader-terang | 762 | 2 |
| daftar-modul-terang | 680 | 2 |
| pricing-terang | 678 | 2 |
| pembahasan-terang | 603 | 2 |
| dashboard-terang | 462 | 3 |
| **TOTAL 20 halaman** | **8.183** | **50** |

Rata-rata **2,5 gambar per halaman**, dan 2 di antaranya adalah logo dan favicon. Artinya nyaris **tidak ada visual penjelas** sama sekali. Rata-rata **409 kata per halaman**.

### Perbaikan 4A — Pecah teks landing page jadi kartu visual

**Target:** landing page turun dari **1.223 kata jadi maksimal 450 kata**, tanpa kehilangan satu pun informasi penting.

Caranya:
1. Bagian "REALITA PERSIAPAN KOMPETISI" (3 paragraf panjang) menjadi **3 kartu ikon besar** bersusun, masing-masing **maksimal 15 kata**.
2. Bagian "ARSITEKTUR BIMBINGAN MEDALIS" (6 pilar) sudah kartu tapi teksnya padat. Potong tiap pilar jadi **judul 3 kata + penjelas 12 kata**.
3. Setiap bagian wajib punya **satu elemen visual**: ilustrasi, tangkapan layar mini, atau diagram sederhana. Bukan ikon Material kecil.

Struktur kartu baku:
```
[Ikon besar 64x64]
[Judul, 3-5 kata]
[Penjelas, maksimal 15 kata]
```

### Perbaikan 4B — Tambah pemilihan kelas di awal (permintaan langsung dari screenshot klien)

**Fakta sekarang:** di `onboarding-terang.html`, jenjang hanya 4 pilihan (TK, SD Kelas 1–6, SMP, SMA Kelas 10–12). Tidak ada pemilihan kelas 1 sampai 12 satu per satu.

**Yang diminta:** grid pemilihan kelas seperti yang dikirim klien di screenshot.

Rancangan:
1. Di langkah 1 onboarding, setelah jenjang dipilih, muncul **grid kelas**.
2. Isi grid mengikuti jenjang:
   - TK → TK A, TK B
   - SD → Kelas 1 sampai Kelas 6
   - SMP → Kelas 7, 8, 9
   - SMA/SMK → Kelas 10, 11, 12
3. Tiap tombol kelas minimal **72 x 72 px** (lebih besar dari 48px karena dipakai anak dan orang tua di HP).
4. Kelas yang dipilih langsung mengubah isi bank soal dan modul.
5. Setelah kelas dipilih, baru masuk langkah 2 (nomor WhatsApp Bunda).

Tambahkan juga jalan pintas: **"Lewati dulu, pilih nanti"** yang mengarah ke dashboard dengan kelas default.

### Perbaikan 4C — Tambah visual di halaman yang paling banyak teksnya

**`ebook-reader-*.html` (762 kata, 2 gambar):**
- Tambah panel sampul modul dengan thumbnail di sisi kiri (atau atas di mobile)
- Tambah progress bar visual
- Tambah daftar isi bergambar, bukan daftar teks

**`daftar-modul-*.html` (680 kata, 2 gambar):**
- Setiap modul jadi kartu dengan **thumbnail cover** (bukan hanya teks judul)
- Tambah badge jumlah soal dan estimasi waktu sebagai ikon, bukan kalimat panjang

**`pricing-*.html` (678 kata, 2 gambar):**
- Tambah ikon besar di tiap paket
- Tambah tabel perbandingan visual (centang/silang) menggantikan paragraf penjelas
- Kurangi teks di bawah harga

### Perbaikan 4D — Tambah ilustrasi di landing page

Minimal **6 ilustrasi baru** di landing page:
1. Hero — ilustrasi siswa di podium atau sedang mengerjakan soal
2. Kartu "Tryout Anti-Putus" — ilustrasi HP dengan ikon sinyal terputus tapi centang tersimpan
3. Kartu "Tutor Interaktif" — ilustrasi percakapan tanya-jawab
4. Kartu "Cara Cepat 10 Detik" — ilustrasi stopwatch + rumus
5. Kartu "Laporan WhatsApp" — **wajib dipertahankan**, klien menyukainya. Perbesar jadi visual penuh.
6. Grid mata pelajaran — 6 ikon bidang (Matematika, Fisika, Biologi, Kimia, Astronomi, Informatika)

Gaya ilustrasi: garis solid, dua warna (Navy + Emas), latar transparan. Bukan ilustrasi 3D, bukan gradien mewah.

### Perbaikan 4E — Ambil struktur Ruangguru tanpa meniru identitasnya

Yang **boleh** diambil:
- Grid kelas 1–12 dengan kartu besar
- Ikon mata pelajaran berwarna
- Pemilihan jenjang/kelas di awal sebelum masuk aplikasi
- Kartu fitur unggulan bergambar
- Navigasi bawah di mobile dengan 4–5 tab

Yang **dilarang** diambil:
- Palet warna biru-dominan Ruangguru (Medalis tetap Navy-Emas-Cream)
- Video player atau preview video pembelajaran
- Gaya ilustrasi maskot Ruangguru
- Layout landing page yang identik

### File yang disentuh
`landing-*.html`, `onboarding-*.html`, `dashboard-*.html`, `daftar-modul-*.html`, `pricing-*.html`, `ebook-reader-*.html`

### Cara verifikasi
1. Hitung kata landing page baru — harus di bawah 450.
2. Setiap bagian landing page punya minimal satu gambar atau ilustrasi (cek `grep -c "<img\|<svg"` per section).
3. Buka di lebar 360px — tidak boleh ada scroll horizontal.
4. Grid kelas muncul setelah memilih jenjang, dan tombolnya minimal 72px.
5. Uji klik: pilih Kelas 8 → bank soal berubah ke materi Kelas 8.

---

## R5 — SELARASKAN DENGAN REFERENSI, TAPI JAGA IDENTITAS

### Aturan penyelarasan

**Yang wajib diseragamkan ke seluruh 41 halaman:**
1. **Navbar tiga tipe** sesuai keputusan sebelumnya:
   - Tipe A (publik): menu anchor + Masuk + Coba Gratis. Tanpa avatar siswa.
   - Tipe B (portal siswa): 5 menu teks + chip profil `AP | Aisyah`.
   - Tipe C (ruang ujian): hanya logo, nama ujian, progres, timer, tombol Selesai. Tanpa link keluar.
2. **Bottom navigation di mobile** untuk Tipe B, 5 tab dengan ikon + label.
3. **Toggle tema** konsisten tiga pilihan: Terang, Gelap, Sistem.

**Yang ditambahkan dari pola Ruangguru:**
1. **Halaman "Pilih Kelas"** sebagai layar pembuka setelah login pertama.
2. **Grid mata pelajaran** di dashboard dengan ikon berwarna, bukan daftar teks.
3. **Kartu progres** dengan cincin persentase, bukan angka telanjang.
4. **Banner ajakan** di atas dashboard, maksimal satu, bisa ditutup.

**Yang dilarang:**
1. Jangan mengubah palet, font, atau bentuk tombol Medalis.
2. Jangan menambah video pembelajaran dalam bentuk apa pun.
3. Jangan menyalin teks pemasaran Ruangguru.

---

## URUTAN PENGERJAAN YANG DISARANKAN

Kerjakan berurutan, satu batch per sesi. Jangan lompat.

**Batch 1 — Perbaikan teks (paling cepat, paling kelihatan)**
1. Bug "Server dns" di landing
2. Ganti semua istilah teknis sesuai tabel R1
3. Ganti nama tutor jadi "Tutor Interaktif" (R2)
4. Sederhanakan kartu Speed-Hack jadi "Cara Cepat 10 Detik" (R3)
5. Tambah FAQ kejujuran tutor

**Batch 2 — Pemilihan kelas**
1. Grid kelas TK A/B, 1–12 di onboarding
2. Tombol minimal 72px
3. Jalan pintas "lewati dulu"
4. Simpan pilihan ke profil siswa

**Batch 3 — Kurangi tulisan di landing**
1. Landing turun ke maksimal 450 kata
2. Pecah jadi kartu ikon besar
3. Tambah 6 ilustrasi
4. Perbesar kartu WhatsApp Bunda

**Batch 4 — Visual di halaman dalam**
1. Thumbnail cover di daftar modul
2. Panel sampul di ebook reader
3. Ikon besar + tabel banding di pricing
4. Cincin progres di dashboard

**Batch 5 — Penyelarasan navbar dan mobile**
1. Tiga tipe navbar di semua halaman
2. Bottom nav di mobile
3. Uji 360px tanpa scroll horizontal

---

## DEFINITION OF DONE

Sebelum menyatakan selesai, semua ini wajib terpenuhi:

**Teks**
- [ ] `grep -ri "IndexedDB\|tab-switch\|arsitektur\|infrastruktur\|toleransi\|protokol\|sinkronisasi\|deterministik" *.html` → nol
- [ ] `grep -ri "Olimpix Engine\|Tutor Penalaran Interaktif\|Metode Dialektika" *.html` → nol
- [ ] `grep -ri "Speed-Hack\|SPEED-HACK\|Aproksimasi\|Pintas kalkulasi" *.html` → nol
- [ ] `grep -ri "Server dns" *.html` → nol
- [ ] Tidak ada simbol LaTeX mentah tampil di UI

**Visual**
- [ ] Landing page maksimal 450 kata
- [ ] Minimal 6 ilustrasi baru di landing
- [ ] Setiap bagian landing punya satu elemen visual
- [ ] Kartu WhatsApp Bunda tetap ada dan lebih besar

**Fungsi**
- [ ] Grid kelas muncul setelah jenjang dipilih
- [ ] Pilih kelas mengubah isi bank soal
- [ ] Tiga tipe navbar konsisten di 41 halaman
- [ ] Bottom nav muncul di lebar di bawah 768px

**Aksesibilitas**
- [ ] Semua tombol minimal 48px (TK 64px, grid kelas 72px)
- [ ] Kontras teks minimal 4.5:1 di mode terang dan gelap
- [ ] Tidak ada scroll horizontal di 360px
- [ ] Layar terbaca dengan keyboard

**Build**
- [ ] `npm run lint` → nol error
- [ ] `npm run typecheck` → nol error
- [ ] `npm run build` → berhasil
- [ ] Commit: `feat(T-XX): revisi klien - bahasa awam, tutor interaktif, grid kelas, kurangi teks`

---

## CATATAN UNTUK MAS ROSIF (bukan untuk klien)

Tiga hal yang saya tidak eksekusi tanpa keputusan Mas:

1. **Arah "sesuaikan dengan Ruangguru"** — kalau dituruti harfiah, identitas akademi olimpiade bisa luntur jadi bimbel umum. Prompt di atas sudah saya batasi ke struktur saja.

2. **Klaim "disusun tim akademik Medalis"** di FAQ tutor — jangan dipakai sebelum tim akademiknya benar-benar ada dan memeriksa soal. Klaim ini masuk kategori informasi menyesatkan kalau dipakai tanpa dasar.

3. **Klaim "Standar Puspresnas RI"** — muncul di landing dan pricing. Ini menyiratkan afiliasi resmi. Kalau Medalis tidak punya izin tertulis dari Puspresnas, sebaiknya diganti jadi "mengacu pada silabus OSN" yang faktual dan tidak berisiko.
