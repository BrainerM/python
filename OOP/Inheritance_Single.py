# Nama : Mundung, Brainer Keneth
# Tanggal : 29 Februari 2024

# Pertama trg bking dpe kelas ortu yaitu "Oto"
class Oto:
    #  abisu npa dpe Konstruktor for mo inisialisasi dpe objek dg jenis dg jumlah roda
    def __init__(self, jenis, ban):
        self.jenis = jenis  # for mo simpang dpe jenis oto oto
        self.ban = ban # for mo simpang ada brp bnyk dpe ban di oto

    # Ini dpe fungsi for mo kse tunjung tu info-info tentang ni oto oto
    def info_oto(self):
        print(f"Jenis: {self.jenis}, Dpe ban da: {self.ban}")

# Kg definisikan dpe kelas anak 'Mobil' yang se waris dari dpe kelas ortu 'Kendaraan'
class Oto_oto(Oto):
    # Npa dpe Konstruktor for inisialisasi objek dg dpe jenis, dpe bnyk ban, dg dpe merek
    def __init__(self, jenis, ban, merek):
        super().__init__(jenis, ban)  # Pangge dpe sebe pe Konsruktor
        self.merek = merek  # Simpang dpe merek oto

    # Haaa npa dpe jurus(metode) for mo kse tunjung info dri oto
    def info_otooto(self):
        print(f"Jenis: {self.jenis}, Dpe ban da: {self.ban}, Merek: {self.merek}")

# Bking objek oto1 dari dpe kelas yang 'Oto_oto' isi jo dg dpe spek trg pe mau iotoh
oto1 = Oto("Sedan", 2, "Bendi")
# Nah ini pangge dpe metode info_mobil() for mo kse tunjung info dri ni objek oto1
oto1.info_oto()
# kurang lbh sma dg di atas mar ini pngge info_kendaraan() dari dpe ortu pe kelas for mo kse tunjung informasi
oto1.info_oto()  # Ini noh tu dpngge metode dri dpe kelas ortu