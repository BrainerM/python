## NAMA : Kapal, David Mathew Daniel
## Tanggal : 29 Februari 2024


#MULTIPLE INHERITANCE

# Pertama trg bking dpe sebe pe kelas itu "OtoOto"
class Oto_oto:
    #  kg npa dpe Konstruktor for mo inisialisasi dpe objek dg jenis dg jumlah roda
    def _init_(self, jenis, ban):
        self.jenis = jenis  # for mo simpang dpe jenis oto oto
        self.ban = ban    # for mo simpang ada brp bnyk dpe ban di oto

    # Ini dpe fungsi for mo kse tunjung tu info-info tentang ni oto oto
    def info_otooto(self):
        print(f"Jenis: {self.jenis}, Dpe bnyk ban: {self.ban}")

# Bking kelas baru for mo se tunjung dpe info dg spek spek mesin baityuu.
class Mesin:
    # Konstruktor for mo inisialisasi objek dg dpe jenis mesin
    def _init_(self, jenis_mesin):
        self.jenis_mesin = jenis_mesin  # For mo simpang dpe jenis mesin

    # npa dpe fungsi ato metode for mo kas tunjung dpe informasi mesin bgtu.
    def info_mesin(self):
        print(f"Jenis Mesin: {self.jenis_mesin}")

# nah ini ko bikin kelas Oto for mo warisi de pu pace 'OtoOto' dg mace 'Mesin' pu kelas
class Oto(Oto_oto, Mesin):
    # Konstruktor for mo inisialisasi objek ulang dg dpe jenis, dpe banyak ban, jenis mesin, deng merek
    def __init__(self, jenis, ban, jenis_mesin, merek):
        # Npa dia pngge dpe konstruktor dri dpe sebe dg ajus pe kelas 'OtoOto dg 'Mesin'
        Oto_oto._init_(self, jenis, ban)
        Mesin._init_(self, jenis_mesin)
        self.merek = merek  # Simpang dpe merek oto

    # npa dpe metode khusus kata gpt blg for mo kse tunjung dpe informasi informasi dri dpe jenis, dbrp dpe ban, dg merek.
    def info_oto(self):
        print(f"Jenis: {self.jenis}, Dpe bnyk ban: {self.ban}, Merek: {self.merek}")

# bkeng objek 'oto1' dari kelas 'Mobil' kg isi jo dpe spek sesuai trg pe selera baityuu.
oto1 = Oto("Sedan", 4, "Bensin", "Toyota")
# trg ba pngge metode pke info_mobil() for mse tunjung info dri oto1
oto1.info_oto()
# kg pngge metode info_kendaraan() dari dpe sebe pe kelas 'OtoOto' for mse tunjung informasi dri ni oto (oto1)
oto1.info_otooto()
# npa le dia bpngge ulng dpe metode info_mesin() dari dpe ajus pe kelas 'Mesin' for mse tunjung dpe jenis mesin dri ni oto1
oto1.info_mesin()
