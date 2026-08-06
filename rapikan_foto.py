import os
import shutil

BASE_DIR = "images"

# 1. Peta Perubahan Nama (Galeri & Kegiatan)
RENAME_MAP = {
    "KKN-PPM-UGM_Periode2_2026-ArtefakGua1.jpg": "galeri/ArtefakGua1.jpg",
    "KKN-PPM-UGM_Periode2_2026-ArtefakGua2.jpg": "galeri/ArtefakGua2.jpg",
    "KKN-PPM-UGM_Periode2_2026-ArtefakGua3.jpg": "galeri/ArtefakGua3.jpg",
    "KKN-PPM-UGM_Periode2_2026-ArtefakGua4.jpg": "galeri/ArtefakGua4.jpg",
    "KKN-PPM-UGM_Periode2_2026-DanauTerbesarDiPulauFam.jpg": "galeri/DanauPulauFam.jpg",
    "KKN-PPM-UGM_Periode2_2026-DockKapalPiaynemo.jpg": "galeri/DockPiaynemo.jpg",
    "KKN-PPM-UGM_Periode2_2026-LandscapePemandanganPiaynemo.jpg": "galeri/PemandanganPiaynemo.jpg",
    
    "KKN-PPM-UGM_Periode2_2026-KoordinasiPemetaanDanPemasanganPetaSaukabuAtauPulauFam.jpg": "kegiatan/KoordinasiPemetaan.jpg",
    "KKN-PPM-UGM_Periode2_2026-KunjunganTimKKNKePiaynemo1.jpg": "kegiatan/KunjunganPiaynemo1.jpg",
    "KKN-PPM-UGM_Periode2_2026-KunjunganTimKKNKePiaynemo2.jpg": "kegiatan/KunjunganPiaynemo2.jpg",
    "KKN-PPM-UGM_Periode2_2026-PenyambutanDiDesaPam.jpg": "kegiatan/PenyambutanDesaPam.jpg",
    "KKN-PPM-UGM_Periode2_2026-PenyerahanMahasiswaDariDosenPembimbingLapanganKeDesaSaukabu.jpg": "kegiatan/PenyerahanMahasiswa.jpg",
    "KKN-PPM-UGM_Periode2_2026-PerayaanUlangTahunSaukabuKe26-1.jpg": "kegiatan/PerayaanHUT26.jpg",
}

# 2. Rename Folders
FOLDER_RENAMES = {
    "BukuAlbumSaukabu_FIXED": "buku_album",
    "InventarisBurung": "fauna",
    "Flora": "flora"
}

print("Memulai proses perapian folder images...")

# Buat folder baru jika belum ada
for folder in ["galeri", "kegiatan", "fauna", "flora", "buku_album"]:
    os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

# Pindahkan dan ubah nama file foto utama
for old_name, new_name in RENAME_MAP.items():
    old_path = os.path.join(BASE_DIR, old_name)
    new_path = os.path.join(BASE_DIR, new_name)
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"✅ Dipindahkan: {old_name} -> {new_name}")

# Pindahkan folder / ubah nama folder lama ke folder baru
for old_folder, new_folder in FOLDER_RENAMES.items():
    old_folder_path = os.path.join(BASE_DIR, old_folder)
    new_folder_path = os.path.join(BASE_DIR, new_folder)
    
    if os.path.exists(old_folder_path):
        # Jika itu folder, pindahkan isinya
        for item in os.listdir(old_folder_path):
            s = os.path.join(old_folder_path, item)
            d = os.path.join(new_folder_path, item)
            if not os.path.exists(d):
                shutil.move(s, d)
        
        # Hapus folder lama yang sudah kosong
        try:
            os.rmdir(old_folder_path)
            print(f"✅ Folder diganti nama: {old_folder} -> {new_folder}")
        except OSError:
            pass

# Bersihkan prefix "KKN-PPM-UGM_Periode2_2026-" pada fauna (burung)
fauna_dir = os.path.join(BASE_DIR, "fauna")
if os.path.exists(fauna_dir):
    for f in os.listdir(fauna_dir):
        if f.startswith("KKN-PPM-UGM_Periode2_2026-"):
            new_f = f.replace("KKN-PPM-UGM_Periode2_2026-", "")
            if new_f.startswith("PtilinopusRivoli-WalikDadaPutih"):
                new_f = "Ptilinopus_rivoli.jpeg"
            elif new_f.startswith("EclectusRoratus"):
                new_f = "Eclectus_roratus.jpeg"
            elif new_f.startswith("GeoffroyusGeoffroyi"):
                new_f = "Geoffroyus_geoffroyi.jpeg"
            elif new_f.startswith("RhipiduraLeucophrys"):
                new_f = "Rhipidura_leucophrys.jpeg"
                
            old_path = os.path.join(fauna_dir, f)
            new_path = os.path.join(fauna_dir, new_f)
            shutil.move(old_path, new_path)
            print(f"✅ File burung diganti nama menjadi: {new_f}")

print("\n🎉 Selesai! Semua file gambar telah dirapikan.")
