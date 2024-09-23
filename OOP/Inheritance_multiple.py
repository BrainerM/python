# Nama : Mundung, Brainer Keneth
# Tanggal : 29 Februari 2024

# Pertama trg bking dpe orang tua pe kelas ato biasa dibilang parent class yaitu "OtoOto"
class Oto_oto:
    #  abistu npa dpe Konstruktor for mo inisialisasi dpe objek dg jenis dg jumlah roda
    def __init__(self, jenis, ban):
        self.jenis = jenis  # for mo simpang dpe jenis oto oto
        self.ban = ban    # for mo simpang ada brp bnyk dpe ban di oto

    # Ini dpe fungsi for mo kse tunjung tu info-info tentang ni oto oto
    def info_otooto(self):
        print(f"Jenis: {self.jenis}, Dpe bnyk ban: {self.ban}")

# Bking kelas baru for mo se tunjung dpe info dg spek spek mesin iotohh.
class Mesin:
    # Konstruktor for mo inisialisasi objek dg dpe jenis mesin
    def _init_(self, jenis_mesin):
        self.jenis_mesin = jenis_mesin  # For mo simpang dpe jenis mesin

    # npa dpe fungsi ato metode for mo kas tunjung dpe informasi mesin bgtu.
    def info_mesin(self):
        print(f"Jenis Mesin: {self.jenis_mesin}")

# nah ini beking kelas Oto for mo warisi depe 'Oto_oto' dg 'Mesin' pe kelas
class Oto(Oto_oto, Mesin):
    # Konstruktor for mo inisialisasi ulang objek, dpe jenis, dpe banyak ban, jenis mesin, deng merek
    def __init__(self, jenis, ban, jenis_mesin, merek):
        # trus dia pngge dpe konstruktor dri 'Oto_oto dg 'Mesin' pe kelas
        Oto_oto.__init__(self, jenis, ban)
        Mesin._init_(self, jenis_mesin)
        self.merek = merek  # Simpang dpe merek oto

    # npa dpe metode khusus kata gpt blg mo kse tunjung dpe informasi informasi dri dpe jenis, brp dpe ban, dg merek.
    def info_oto(self):
        print(f"Jenis: {self.jenis}, Dpe bnyk ban: {self.ban}, Merek: {self.merek}")

# bkeng objek 'oto1' dari kelas 'Mobil' kg isi jo dpe spek sesuai kamo pe selera.
oto1 = Oto("Sedan", 4, "Bensin", "Honda")
# trg ba pngge metode pke info_mobil() for mse tunjung info dri oto1
oto1.info_oto()
# kg pngge metode info_kendaraan() dari dpe ortu pe kelas 'Oto_oto' for mse tunjung informasi dri ni oto (oto1)
oto1.info_otooto()
# dia bpngge ulng dpe metode info_mesin() dari dpe ortu 2 pe kelas 'Mesin' for mse tunjung dpe jenis mesin dri ni oto1
oto1.info_mesin()
