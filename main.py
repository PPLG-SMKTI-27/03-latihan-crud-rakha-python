# data buku

from tabulate import tabulate

books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""},
]

def tampilkan_data():
     print(tabulate(books, headers="keys" , tablefmt="grid"))

def tambah_data():
     print("Menambahkan data buku")
     isbn = input("Masukkan kode ISBN buku: ")
     judul = input("Masukkan judul buku: ")
     pengarang = input("Masukkan Pengarang buku: ")
     jumlah = int(input("Masukkan jumlah stok buku:"))
     terpinjam = 0
     books.append({"isbn":isbn, "judul":judul, "pengarang":pengarang, "jumlah":jumlah, "terpinjam":terpinjam})
     print("Data buku berhasil di tambah.")
     tampilkan_data()
     

def edit_data():
    print("=== Edit Data Buku ===")
    isbn = input("Masukkan nomor ISBN yang ingin di edit:")
    for book in books:
        if book['isbn'] == isbn:
            book['judul'] = input("Masukkan judul buku baru: ")
            book['pengarang'] = input("Masukkan nama pengarang buku baru: ")
            book['jumlah'] = int(input("Masukkan jumlah buku baru: "))
            print("Data buku sudah di ubah.")
            tampilkan_data()
            
        

def hapus_data():
    print("=== Hapus Data ===")
    isbn = input("Masukkan nomor ISBN yang akan di hapus: ")
    for book in books:
        if book['isbn'] == isbn:
            books.remove(book)
            print("Data buku sudah terhapus.")
            tampilkan_data()

def tampilkan_peminjaman():
    print("=== Data Peminjam buku ===")
    print(tabulate(records, headers="keys", tablefmt="grid"))
    print("------------------------------")

def tampilkan_belum():
    print("=== Peminjaman belum dikembalikan ===")
    print(tabulate([record for record in records if record['tanggal_kembali']is None], headers="keys", tablefmt="grid"))

def peminjaman():
    print("=== Pinjaman buku ===")
    tampilkan_data()
    isbn = input("Masukkan nomor ISBN yang ingin di pinjam: ")
    nama = input("Masukkan nama peminjam: ")
    tanggal_pinjam = input("Masukkan tanggal peminjaman (YYYY-MM-DD): ")
    for book in books:
        if book['jumlah'] > book['terpinjam']:
            book['jumlah'] -= 1
            book['terpinjam'] += 1
            records.append({"isbn": isbn, "nama": nama, "status": "belum", "tanggal_pinjam": tanggal_pinjam, "tanggal_kembali": None})
            tampilkan_peminjaman()
            return
        else:
            print("Buku tidak ada untuk dipinjam.")

        

def pengembalian():
    print("=== Pengembalian Buku ===")
    isbn = input("Masukkan Nomor ISBN yang ingin dikembalikan: ")
    for book in books:
        if book['isbn'] == isbn:
            for record in records:
                if record['isbn'] == isbn and record['tanggal_kembali'] is None:
                    book['terpinjam'] -= 1
                    book['jumlah'] += 1
                    record['tanggal_kembali'] = input("masukkan tanggal kembali (YYYY-MM-DD): ")
                    record['status'] = "selesai"
                    print("Buku telah dikembalikan")
                    tampilkan_data()



while ...:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")

    if menu == "1" :
        tampilkan_data()
        input("Enter Untuk Melanjutkan")
    

    elif menu == "2" :
        tambah_data()
        input("Enter untuk melanjutkan")

    elif menu == "3" :
        edit_data()
        input("Enter untuk melanjutkan")

    elif menu == "4" :
        hapus_data()
        input("Enter untuk melanjutkan")

    elif menu == "5" :
        tampilkan_peminjaman()
        input("Enter untuk melanjutkan")

    elif menu == "6" :
        tampilkan_belum()
        input("Enter untuk melanjutkan")

    elif menu == "7" :
        peminjaman()
        input("Enter untuk melanjutkan")

    elif menu == "8" :
        pengembalian()
        input("Enter untuk melanjutkan")

    elif menu.lower() == "x":
        print("Terima kasih telah menggunakan perpustakaan ini.")
        break
        

    else:
        print("Nomor menu tidak valid")
