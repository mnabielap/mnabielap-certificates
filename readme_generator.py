import os
import urllib.parse

ORGANIZED_DIR = r"F:\!All About Coding\mnabielap-certificates"
OUTPUT_FILE = "README.md"

def generate_readme_with_links():
    """
    Fungsi utama untuk men-scan folder dan menghasilkan file README.md
    dengan link ke setiap file sertifikat.
    """
    print(f"Memulai pembuatan file README.md dengan link...")
    print(f"Membaca dari folder: {ORGANIZED_DIR}\n")

    if not os.path.isdir(ORGANIZED_DIR):
        print(f"ERROR: Folder '{ORGANIZED_DIR}' tidak ditemukan!")
        print("Pastikan Anda sudah menjalankan skrip 'atur_sertifikat.py' terlebih dahulu.")
        return

    readme_content = []
    readme_content.append("# My Programming & Technology Certificates Collection 🎓\n\n")
    readme_content.append("Here is a list of certificates I have obtained, sorted by category. Each certificate title is a link to its PDF file.\n\n")

    try:
        category_folders = sorted([d for d in os.listdir(ORGANIZED_DIR) if os.path.isdir(os.path.join(ORGANIZED_DIR, d))])
    except FileNotFoundError:
        print(f"ERROR: Gagal mengakses direktori '{ORGANIZED_DIR}'.")
        return

    for folder_name in category_folders:
        clean_title = folder_name.split('. ', 1)[-1]
        readme_content.append(f"## {clean_title}\n\n")

        category_path = os.path.join(ORGANIZED_DIR, folder_name)
        
        try:
            certificates = sorted([f for f in os.listdir(category_path) if f.lower().endswith('.pdf')])
            
            if not certificates:
                readme_content.append("- Belum ada sertifikat di kategori ini.\n")
            else:
                for cert_file in certificates:
                    cert_name = os.path.splitext(cert_file)[0]
                    
                    encoded_folder = urllib.parse.quote(folder_name)
                    encoded_file = urllib.parse.quote(cert_file)
                    
                    markdown_link = f"- [{cert_name}](./{encoded_folder}/{encoded_file})\n"
                    readme_content.append(markdown_link)

            readme_content.append("\n")
        except FileNotFoundError:
            print(f"WARNING: Gagal mengakses sub-folder '{category_path}'.")
            continue

    output_path = os.path.join(ORGANIZED_DIR, OUTPUT_FILE)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(readme_content)
        print("--- Proses Selesai ---")
        print(f"✔️  File README.md dengan link berhasil dibuat/diperbarui di:\n{output_path}")
    except IOError as e:
        print(f"❌  Gagal menulis file README.md. Error: {e}")

if __name__ == "__main__":
    generate_readme_with_links()