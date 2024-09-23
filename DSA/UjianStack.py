print("--------------------------------")
print("SELAMAT DATANG DI BUS MANADO BITUNG")
print("--------------------------------")
print("1. Silahkan masukkan nama anda")
print("2. hapus nama anda(pilih menu ini jika anda sudah keluar bus)")
print("3. tampilkan jumlah penumpang saat ini")
print("4. keluar")
pilihan = int(input("1/2/3/4: "))
pelanggan = []

def tambah():
    nama_pelanggan = str(input("tambahkan nama: "))
    pelanggan.append(nama_pelanggan)
    print("penumpang berhasil di tambahkan")
    print("--------------------------------")

def hapus():
    pelanggan.pop()
    print("penumpang Sudah keluar bus")
    print("Terima kasih")
    print("--------------------------------")

def remaining():
    if len(pelanggan) >= 0 :
        for data in reversed(pelanggan):
            print("sisa penumpang:",data)
        print("---------------------")

while pilihan != 4:
    if pilihan == 1:
        tambah()
    elif pilihan == 2:
        hapus()
    elif pilihan == 3:
        remaining()
    print("1. Silahkan masukkan nama anda")
    print("2. hapus nama anda(pilih menu ini jika anda sudah keluar bus)")
    print("3. tampilkan jumlah penumpang saat ini")
    print("4. keluar")
    pilihan = int(input("1/2/3/4: "))