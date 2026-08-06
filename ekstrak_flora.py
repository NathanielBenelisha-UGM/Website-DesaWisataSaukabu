"""
Skrip untuk mengekstrak gambar dari PDF Ensiklopedia Flora Saukabu
Cara pakai:
1. Pastikan Python sudah terinstall
2. Buka terminal/command prompt di folder ini
3. Jalankan: pip install PyMuPDF
4. Jalankan: python ekstrak_flora.py
"""

import os

try:
    import fitz  # PyMuPDF
except ImportError:
    print("❌ Library PyMuPDF belum terinstall.")
    print("Silakan jalankan perintah ini di terminal:")
    print("pip install PyMuPDF")
    exit(1)

PDF_FILE = "Ensiklopedia_Flora_Saukabu (1).pdf"
OUTPUT_DIR = "images/Flora"

if not os.path.exists(PDF_FILE):
    print(f"❌ File {PDF_FILE} tidak ditemukan!")
    exit(1)

os.makedirs(OUTPUT_DIR, exist_ok=True)
print(f"Membaca file PDF: {PDF_FILE}...")

doc = fitz.open(PDF_FILE)
image_count = 0

for page_index in range(len(doc)):
    page = doc[page_index]
    image_list = page.get_images(full=True)
    
    if image_list:
        print(f"  Halaman {page_index + 1}: Ditemukan {len(image_list)} gambar")
    
    for img_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        # Penamaan: flora_halamanX_gambarY.ext
        image_name = f"flora_hal{page_index + 1}_{img_index}.{image_ext}"
        image_path = os.path.join(OUTPUT_DIR, image_name)
        
        with open(image_path, "wb") as image_file:
            image_file.write(image_bytes)
            
        image_count += 1
        print(f"    -> Disimpan: {image_name}")

print("\n✅ Ekstraksi selesai!")
print(f"Total {image_count} gambar berhasil diekstrak ke folder '{OUTPUT_DIR}'")
print("\nSekarang Anda bisa memilih foto-foto terbaik dan menampilkannya di website.")
