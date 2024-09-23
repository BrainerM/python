class Buku:
    #ini adalah constructor
    def __init__(self, judul, penulis, ISBN):
        self.judul = judul
        self.penulis = penulis
        self.ISBN = ISBN
        self.harga_per_tahun = {}

    #method pertama
    def set_harga_tahun(self, tahun, harga):
        self.harga_per_tahun[tahun] = harga

    #method kedua
    def tampilkan_detail_buku(self):
        print(f"Judul Buku: {self.judul}")
        print(f"penulis: {self.penulis}")
        print(f"ISBN: {self.ISBN}")
        print("Harga per tahun: ")
        for tahun, harga in self.harga_per_tahun.items():
            print(f"- Tahun {tahun}: Rp{harga:,.2f}")

#objek dari buku dibuat
obj_buku = Buku (" Machine learning Algoritma", "George Tangka", "231849246")

# Pengaturan harga buku per tahun
obj_buku.set_harga_tahun(2020, 50000)
obj_buku.set_harga_tahun(2021, 70000)
obj_buku.set_harga_tahun(2022, 90000)
obj_buku.set_harga_tahun(2023, 95000)