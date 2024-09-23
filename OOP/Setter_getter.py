# Name : Mundung, Brainer Keneth
# Date : Thursday, 28th March

# Class
class Perpustakaan:
    def __init__(self):  # constructor untuk inisialisasi atribut-atribut
        self.__nama = ""
        self.__alamat = ""
        self.__jumlah_koleksi_buku = 0
        self.__jumlah_buku_terpinjam = 0
        self.__denda_per_hari = 0

    # Setter
    def set_nama(self, nama):  # setter untuk mengatur nama perpustakaan
        self.__nama = nama

    def set_alamat(self, alamat):  # setter untuk mengatur alamat perpustakaan
        self.__alamat = alamat

    def set_jumlah_koleksi_buku(self, jumlah_koleksi_buku):  # setter untuk mengatur jumlah koleksi buku
        self.__jumlah_koleksi_buku = jumlah_koleksi_buku

    def set_jumlah_buku_terpinjam(self, jumlah_buku_terpinjam):  # setter untuk mengatur jumlah buku yang dipinjam
        self.__jumlah_buku_terpinjam = jumlah_buku_terpinjam

    def set_denda_per_hari(self, denda_per_hari):  # setter untuk mengatur denda per hari
        self.__denda_per_hari = denda_per_hari

    # Getter
    def get_nama(self):  # getter untuk mendapatkan nama perpustakaan
        return self.__nama

    def get_alamat(self):  # getter untuk mendapatkan alamat perpustakaan
        return self.__alamat

    def get_jumlah_koleksi_buku(self):  # getter untuk mendapatkan jumlah koleksi buku
        return self.__jumlah_koleksi_buku

    def get_jumlah_buku_terpinjam(self):  # getter untuk mendapatkan jumlah buku yang dipinjam
        return self.__jumlah_buku_terpinjam

    def get_denda_per_hari(self):  # getter untuk mendapatkan denda per hari
        return self.__denda_per_hari

    # Method
    def informasi(self):  # method untuk mendapatkan informasi tentang perpustakaan
        return f"Perpustakaan {self.__nama}, Alamat: {self.__alamat}, Total Koleksi: {self.__jumlah_koleksi_buku} buku, Buku Terpinjam: {self.__jumlah_buku_terpinjam}, Denda Per Hari: Rp. {self.__denda_per_hari}"

    def tambah_buku_ke_koleksi(self, jumlah):  # method untuk menambah buku ke koleksi
        self.__jumlah_koleksi_buku += jumlah

    def meminjam_buku(self, jumlah):  # method untuk meminjam buku
        if self.__jumlah_koleksi_buku - self.__jumlah_buku_terpinjam >= jumlah:
            self.__jumlah_buku_terpinjam += jumlah
        else:
            print("Jumlah buku yang tersedia tidak mencukupi!")

    def mengembalikan_buku(self, jumlah):  # method untuk mengembalikan buku
        if self.__jumlah_buku_terpinjam >= jumlah:
            self.__jumlah_buku_terpinjam -= jumlah
        else:
            print("Jumlah buku yang akan dikembalikan melebihi jumlah buku yang sedang dipinjam!")

    def jumlah_buku_tersedia(self):  # method untuk mendapatkan jumlah buku yang tersedia
        return self.__jumlah_koleksi_buku - self.__jumlah_buku_terpinjam

    def jumlah_buku_dipinjam(self):  # method untuk mendapatkan jumlah buku yang dipinjam
        return self.__jumlah_buku_terpinjam

# Membuat objek perpustakaan1
perpustakaan1 = Perpustakaan()
perpustakaan1.set_nama("Perpustakaan Universitas Klabat")
perpustakaan1.set_alamat("Jl. Arnold Mononutu No. 123")
perpustakaan1.set_jumlah_koleksi_buku(1000)
perpustakaan1.set_jumlah_buku_terpinjam(400)
perpustakaan1.set_denda_per_hari(1000)

# Menampilkan informasi perpustakaan1
print(perpustakaan1.informasi())

# Melakukan beberapa operasi pada perpustakaan1
perpustakaan1.tambah_buku_ke_koleksi(500)
perpustakaan1.meminjam_buku(200)
perpustakaan1.mengembalikan_buku(100)

# Menampilkan jumlah buku tersedia dan jumlah buku yang dipinjam pada perpustakaan1
print("jumlah buku tersedia:",perpustakaan1.jumlah_buku_tersedia())
print("Jumlah buku yang dipinjam:", perpustakaan1.jumlah_buku_dipinjam())

# Menampilkan informasi perpustakaan1 setelah operasi
print(perpustakaan1.informasi())
print("-------------------------------------")

# Membuat objek perpustakaan2
perpustakaan2 = Perpustakaan()
perpustakaan2.set_nama("Perpustakaan Universitas Manado")
perpustakaan2.set_alamat("Jl. Tikala No. 345")
perpustakaan2.set_jumlah_koleksi_buku(2000)
perpustakaan2.set_jumlah_buku_terpinjam(300)
perpustakaan2.set_denda_per_hari(2000)

# Menampilkan informasi perpustakaan2
print(perpustakaan2.informasi())

# Melakukan beberapa operasi pada perpustakaan2
perpustakaan2.tambah_buku_ke_koleksi(200)
perpustakaan2.meminjam_buku(300)
perpustakaan2.mengembalikan_buku(100)

# Menampilkan jumlah buku tersedia dan jumlah buku yang dipinjam pada perpustakaan2
print("jumlah buku tersedia:",perpustakaan2.jumlah_buku_tersedia())
print("Jumlah buku yang dipinjam:", perpustakaan2.jumlah_buku_dipinjam())

# Menampilkan informasi perpustakaan1 setelah operasi
print(perpustakaan1.informasi())
print("--------------------------------------")

# Membuat objek perpustakaan3
perpustakaan3 = Perpustakaan()
perpustakaan3.set_nama("Perpustakaan Universitas Bitung")
perpustakaan3.set_alamat("Jl. Mahesa No. 654")
perpustakaan3.set_jumlah_koleksi_buku(6000)
perpustakaan3.set_jumlah_buku_terpinjam(500)
perpustakaan3.set_denda_per_hari(3000)

# Menampilkan informasi perpustakaan3
print(perpustakaan3.informasi())

# Melakukan beberapa operasi pada perpustakaan3
perpustakaan3.tambah_buku_ke_koleksi(600)
perpustakaan3.meminjam_buku(350)
perpustakaan3.mengembalikan_buku(200)

# Menampilkan jumlah buku tersedia dan jumlah buku yang dipinjam pada perpustakaan3
print("jumlah buku tersedia:",perpustakaan3.jumlah_buku_tersedia())
print("Jumlah buku yang dipinjam:", perpustakaan3.jumlah_buku_dipinjam())

# Menampilkan informasi perpustakaan3 setelah operasi
print(perpustakaan3.informasi())
