import os
import shutil

SOURCE_DIR = r"F:\!All About Coding\Cerificate"
DEST_DIR = r"F:\!All About Coding\mnabielap-certificates"

CATEGORIES = {
    "3. Mobile Development": ['flutter', 'android', 'kotlin', 'react native', 'swift', 'ios'],
    "2. Data Science - AI - ML": ['data science', 'machine learning', 'deep learning', 'ai', 'artificial intelligence', 'neural network', 'nlp', 'pytorch', 'tensorflow', 'pandas', 'numpy', 'data analyst', 'data analysis', 'sql for data', 'bigquery', 'big data'],
    "4. DevOps & Cloud": ['devops', 'docker', 'kubernetes', 'aws', 'gcp', 'azure', 'cloud'],
    "1. Web Development - Backend": ['backend', 'node.js', 'express', 'django', 'flask', 'java spring', 'spring boot', 'hibernate', 'php', 'laravel', 'golang', 'ruby on rails', 'asp.net', '.net', 'microservices', 'rest api'],
    "1. Web Development - Frontend": ['frontend', 'javascript', 'typescript', 'react', 'vue', 'angular', 'next.js', 'html', 'css', 'bootstrap', 'tailwind', 'figma', 'web design'],
    "6. Database": ['sql', 'mysql', 'postgresql', 'mongodb', 'database'],
    "7. Cybersecurity": ['ethical hacking', 'cyber security', 'penetration testing'],
    "5. Core Programming & CS Fundamentals": ['java', 'python', 'c++', ' c ', 'c#', 'rust', 'ruby', ' go ', 'golang', 'algorithms', 'data structures', 'clean code', 'design patterns', 'solid principles', 'oop', 'testing'],
    "8. Tools & Others": ['git', 'excel', 'postman', 'figma', 'wordpress']
}

UNCATEGORIZED_DIR_NAME = "9. Others (Uncategorized)"

def organize_certificates():
    """
    Fungsi utama untuk membaca file dari SOURCE_DIR, mencocokkannya dengan
    kategori, dan memindahkannya ke DEST_DIR.
    """
    print(f"Memulai proses organisasi sertifikat...")
    print(f"Folder Sumber: {SOURCE_DIR}")
    print(f"Folder Tujuan: {DEST_DIR}\n")

    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
        print(f"Folder tujuan '{DEST_DIR}' berhasil dibuat.")

    moved_count = 0
    error_count = 0

    if not os.path.isdir(SOURCE_DIR):
        print(f"ERROR: Folder sumber '{SOURCE_DIR}' tidak ditemukan!")
        return

    for filename in os.listdir(SOURCE_DIR):
        if not filename.lower().endswith('.pdf'):
            continue

        src_path = os.path.join(SOURCE_DIR, filename)
        
        if not os.path.isfile(src_path):
            continue

        found_category = False
        
        for category_name, keywords in CATEGORIES.items():
            for keyword in keywords:
                if keyword.lower() in filename.lower():
                    
                    category_dir = os.path.join(DEST_DIR, category_name)
                    if not os.path.exists(category_dir):
                        os.makedirs(category_dir)
                    
                    dest_path = os.path.join(category_dir, filename)

                    try:
                        shutil.move(src_path, dest_path)
                        print(f"✔️  '{filename}' -> dipindahkan ke '{category_name}'")
                        moved_count += 1
                        found_category = True
                    except Exception as e:
                        print(f"❌  Gagal memindahkan '{filename}'. Error: {e}")
                        error_count += 1
                    
                    break
            if found_category:
                break

        if not found_category:
            uncategorized_dir = os.path.join(DEST_DIR, UNCATEGORIZED_DIR_NAME)
            if not os.path.exists(uncategorized_dir):
                os.makedirs(uncategorized_dir)
            
            dest_path = os.path.join(uncategorized_dir, filename)
            try:
                shutil.move(src_path, dest_path)
                print(f"❔  '{filename}' -> tidak ada kategori, dipindahkan ke '{UNCATEGORIZED_DIR_NAME}'")
                moved_count += 1
            except Exception as e:
                print(f"❌  Gagal memindahkan '{filename}'. Error: {e}")
                error_count += 1
                
    print("\n--- Proses Selesai ---")
    print(f"Total file berhasil dipindahkan: {moved_count}")
    print(f"Total file gagal dipindahkan: {error_count}")
    print(f"Sertifikat Anda sekarang terorganisir di: {DEST_DIR}")

# Jalankan fungsi utama
if __name__ == "__main__":
    organize_certificates()