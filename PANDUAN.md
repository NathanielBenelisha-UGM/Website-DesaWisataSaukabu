# 📘 PANDUAN UPDATE WEBSITE SAUKABU
**Kampung Wisata Saukabu — Waigeo Barat Kepulauan, Raja Ampat**
*Dibuat oleh KKN PPN UGM 2026*

---

## 🗂️ Struktur File Website

```
📁 [KKN] WEBSITE SAUKABU/
│
├── index.html          ← File utama website (ini yang perlu diedit)
├── style.css           ← Tampilan/desain (tidak perlu diedit)
├── PANDUAN.md          ← File panduan ini
│
└── 📁 images/          ← Simpan semua foto di sini
    ├── pantai1.jpg
    ├── piaynemo.jpg
    └── ... (foto lainnya)
```

---

## 📸 1. MENAMBAH FOTO KE GALERI

### Langkah-langkah:
1. Simpan foto ke dalam folder `images/`
2. Buka file `index.html` dengan Notepad
3. Tekan `Ctrl+F`, cari kata: `GALERI`
4. Ganti kotak placeholder dengan foto asli

### Sebelum (placeholder):
```html
<div class="gal-slot"><span>Pasir putih Saukabu</span></div>
```

### Sesudah (foto asli):
```html
<div class="gal-slot"><img src="images/pantai1.jpg" alt="Pantai Saukabu"></div>
```

### Tambah foto baru:
Salin dan tempel setelah foto terakhir di galeri:
```html
<div class="gal-slot"><img src="images/nama-foto.jpg" alt="Keterangan foto"></div>
```

---

## 📰 2. MENAMBAH BERITA / UPDATE

1. Buka `index.html`
2. Tekan `Ctrl+F`, cari: `news-grid`
3. Tempel berita BARU di PALING ATAS (sebelum berita pertama)

### Template:
```html
<article class="news-card">
  <div class="news-date">Agustus 2026</div>
  <h3 class="news-title">Judul Berita Di Sini</h3>
  <p class="news-body">Isi berita di sini.</p>
</article>
```

---

## 🎯 3. MENAMBAH ATRAKSI WISATA

Cari `CARA TAMBAH ATRAKSI`, lalu salin dan tempel:
```html
<div class="card">
  <div class="tag">Kategori</div>
  <h3>Nama Atraksi</h3>
  <p>Deskripsi singkat.</p>
</div>
```

---

## 🛒 4. MENAMBAH PRODUK

Cari `CARA TAMBAH PRODUK`, lalu salin dan tempel:
```html
<div class="prod-item">
  <div class="name">Nama Produk</div>
  <div class="desc">deskripsi singkat</div>
</div>
```

---

## 📞 5. UPDATE NOMOR WHATSAPP

1. Cari teks `wa.me/6281234567890`
2. Ganti angkanya dengan nomor WA yang benar
3. Format: `62` + nomor tanpa 0 depan
   - Contoh: `0812-3456-7890` → `6281234567890`
4. Juga ganti teks `+62 812-XXXX-XXXX` dengan nomor yang benar

---

## 🌐 6. CARA UPLOAD KE INTERNET (Gratis)

**Cara termudah — Netlify:**
1. Buka https://netlify.com dan daftar gratis
2. Drag-and-drop seluruh folder website ke Netlify
3. Website langsung online!

**Atau gunakan GitHub Pages:**
1. Buat akun di https://github.com
2. Upload semua file ke repository baru
3. Aktifkan GitHub Pages di Settings
4. Website tersedia di `https://username.github.io/saukabu`

---

## ✅ CHECKLIST UPDATE RUTIN

- [ ] Edit `index.html` sesuai kebutuhan
- [ ] Simpan file (`Ctrl+S`)
- [ ] Cek di browser (klik dua kali `index.html`)
- [ ] Upload ke hosting jika sudah oke

---

*Juli 2026 — KKN PPN UGM*
