Menu =int(input("1. Masukkan Nilai \n2. Cari nilai \npilih menu yang ingin anda pakai:"))

if Menu == 1:
    nilaiUjian = []
    i = 1
    while i <= 3:
        nilai = int(input("Masukkan nilai ujian ke-" + str(i) + ": "))
        nilaiUjian.append(nilai)
        i += 1

    def Linear(nilaiUjian, x, nilai):
        for i in range (len(nilaiUjian)):
            if nilaiUjian[i] == x :
                return i
        return -1

x = int(input("Masukkan nilai yang ingin dicari: "))
nilai = 0
nilai = Linear(nilaiUjian, x, nilai)
if nilai!=-1:
    print("data ditemukan di index: ", nilai)
else:
    print("data tidak ditemukan") 