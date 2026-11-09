# T-Prototype-A: Penyempurnaan UI revisi tim — Kompetisi visual, modul tenang, akses guest & CS

## Scope
- `prep-timeline-terang.html` & `prep-timeline-gelap.html`: kartu lomba katalog visual poster Medalis Preview + aksi nyata, label timeline contoh bukan pendaftaran aktif.
- `daftar-modul-terang.html` & `daftar-modul-gelap.html`: label gratis/locked konsisten, kurangi elemen berisik, perbaikan link modul self-target, target sentuh >=48px.
- Halaman publik terkait: WhatsApp admin sementara punya Rosif diganti persis 6285792945213.

## Di Luar Scope
- Backend/auth/payment/batasan VIP enforcement selain UI prototype.
- Halaman artikel SEO, ads, n8n, subscription OPEX, real pengingat.
- Modifikasi onboarding existing ke luar kompatibilitas.
- Brand ganti to POSI/Ruangguru, klaim pendaftaran official atau afiliasi.
- Jadwal lomba fiktif sebagai berita resmi; materi demo diberi label contoh.

## Verifikasi
- Image thumbnail memiliki alt bukan sumber gambar resmi penyelenggara; teks tanggal juga HTML.
- Kartu kompetisi punya CTA working ke detail/material existing jika ada.
- Semua label CTA sama dengan tujuannya, nomor admin format E.164.
- HTML & JS valid; browser test, no zero-layout fail pada navigasi; 360px no overflow; light/dark toggle tidak mengacak identity.
