# 🚀 Panduan Lengkap Website & CMS Desa Wisata Saukabu

Website ini kini telah dilengkapi dengan **Sistem Admin (CMS)** sehingga perangkat desa dapat dengan mudah menambah/mengedit Berita dan Fauna tanpa perlu menyentuh kode HTML.

---

## 1. MENGAKTIFKAN SISTEM ADMIN (CMS) DI NETLIFY

Agar halaman admin bisa digunakan, Anda **wajib** mengaktifkan fitur Identity di Netlify:

### Langkah A: Aktifkan Netlify Identity
1. Buka dashboard **Netlify** Anda, pilih website Saukabu.
2. Di menu atas, pilih **"Site configuration"** > **"Identity"**.
3. Klik tombol **"Enable Identity"**.
4. Masih di halaman Identity, cari menu **"Registration"** > Ubah **Registration preferences** menjadi **Invite only** (agar tidak sembarang orang bisa daftar).

### Langkah B: Aktifkan Git Gateway
1. Di menu atas, pilih **"Site configuration"** > **"Identity"** > geser ke bawah cari **"Services"**.
2. Di bagian **Git Gateway**, klik **"Enable Git Gateway"**.
3. Ini akan meminta izin untuk menyambungkan Netlify dengan repositori GitHub Anda. Klik izinkan.

### Langkah C: Undang Admin (Diri Anda Sendiri)
1. Di menu atas, klik tab **"Identity"** (di sebelah "Site configuration").
2. Klik tombol **"Invite users"**.
3. Masukkan alamat email Anda, lalu kirim.
4. Buka email Anda, klik link konfirmasi yang diberikan.
5. Anda akan dibawa ke website Anda (desawisatasaukabu.netlify.app) dengan popup untuk membuat password. Buat password Anda.

### Cara Menggunakan CMS
1. Buka: `https://desawisatasaukabu.netlify.app/admin/`
2. Login menggunakan email dan password yang baru Anda buat.
3. Anda kini bisa menambah, mengedit, atau menghapus Berita dan Fauna! Setiap perubahan akan otomatis tersimpan ke GitHub dan Netlify akan memperbarui website secara otomatis.

---

## 2. CARA BELI DOMAIN (DesaWisataSaukabu.com)

Untuk membuat website terlihat profesional, Anda butuh domain.

### Opsi Mudah & Bahasa Indonesia (Niagahoster)
1. Buka **https://www.niagahoster.co.id/**.
2. Ketik `desawisatasaukabu.com` di kolom pencarian.
3. Klik "Cek Domain" lalu "Tambah ke Keranjang".
4. Pilih paket **"Hanya Domain"** (tidak perlu beli hosting, karena hosting sudah pakai Netlify yang jauh lebih cepat dan gratis).
5. Lanjutkan ke pembayaran (Transfer Bank / QRIS). Biaya sekitar Rp150.000 - Rp200.000 per tahun.

### Cara Menghubungkan Domain ke Netlify
Setelah domain aktif di Niagahoster:
1. Buka dashboard Netlify > **"Domain management"**.
2. Klik **"Add a domain"** > ketik `desawisatasaukabu.com` > Klik Verify.
3. Netlify akan memberikan 2 atau 4 "Nameserver" (misalnya: `dns1.p01.nsone.net`).
4. Buka dashboard **Niagahoster**, masuk ke menu pengaturan Domain Anda.
5. Cari pengaturan **"Nameserver"** atau **"DNS"**.
6. Ganti Nameserver bawaan Niagahoster dengan Nameserver dari Netlify.
7. Tunggu beberapa jam (maksimal 24 jam) hingga domain terhubung. Selesai!

---

## 3. CARA UPDATE WEBSITE MANUAL (Bagi Developer/Mahasiswa KKN)

Jika Anda ingin mengubah tampilan, warna, atau layout, Anda tetap bisa mengedit file `index.html` dan `style.css`.

- Lakukan edit file di komputer.
- Jika sudah selesai, jalankan perintah ini di Terminal (berada di folder `KKN-WEBSITE_SAUKABU`):

```powershell
git add .
git commit -m "Update tampilan"
git push -u origin main
```

Netlify akan otomatis memperbarui website dalam 1-2 menit setelah perintah `git push` selesai.

---
**Dibuat oleh Tim KKN-PPM UGM Periode 2 "Amai Pulau Pam" (2026)**
