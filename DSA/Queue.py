print("--------------------------------")
print("SELAMAT DATANG DI PLN")
print("silahkan mengambil nomor antrian")
print("--------------------------------")
print("silahkan pilih menu berikut")
print("--------------------------------")
print("1. Silahkan masukkan nomor antrian anda")
print("2. hapus nomor antrian(pilih menu ini jika antrian anda sudah selesai)")
print("3. banyaknya nomor antrian")
print("4. keluar")
pilihan = int(input("1/2/3/4: "))
pelanggan = []

def tambah():
    nomor_antri = int(input("tambahkan nomor antrian: "))
    pelanggan.append(nomor_antri)
    print("nomor antrian berhasil di tambahkan")
    print("informasi antrian:",pelanggan)
    print("--------------------------------")

def hapus():
    pelanggan.pop(0)
    print("antrian berhasil di hapus:")
    print(pelanggan)
    print("--------------------------------")

def remaining():
    print("nomor antrian tersisa:",pelanggan)
    print("--------------------------------")

while pilihan != 4:
    if pilihan == 1:
        tambah()
    elif pilihan == 2:
        hapus()
    elif pilihan == 3:
        remaining()
    print("1. Silahkan masukkan nomor antrian anda")
    print("2. hapus nomor antrian(pilih menu ini jika antrian anda sudah selesai)")
    print("3. banyaknya antrian")
    print("4. Keluar")
    pilihan = int(input("1/2/3/4: "))