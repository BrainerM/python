class penulis:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def tulis_buku(self, judul):
        print(F" {self.nama} menulis buku dengan judul {judul}")

class buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def cetak_info(self):
        print(f"Buku '{self.judul}' ditulis oleh {self.penulis.nama} dari {self.penulis.asal}")

# create objects dari class Penulis dan class Buku
penulis1 = penulis("Brainer Mundung", "Manado" )
bukul = buku("Java Programming", penulis1)

# info buku
bukul.cetak_info()

# info penulis
penulis1. tulis_buku ("Java Programming")