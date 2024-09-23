print("1. Tambah data (push data)")
print("2. Hapus data (pop data)")
print("3. View Data")
print("4. Informasi Stack")
print("5. Keluar")
pilihan = int(input("Masukan pilihan anda: "))
stack = []

def TambahData():
    push = int(input("Masukan data yang ingin ditambahkan: "))
    stack.append(push)
    print("Data berhasil ditambahkan")

def HapusData():
    if len(stack) > 0:
        stack.pop()
        print("Data berhasil dihapus")
    else:
        print("Stack sudah kosong, tidak ada data yang bisa dihapus.")

def ViewData():
    if len(stack) > 0:
        print("\nTampilan Stack:")
        for data in reversed(stack):
            print(data)
    else:
        print("Stack kosong.")

def Informasi():
    print("\nJumlah data pada stack:", len(stack))
    if len(stack) > 0:
        print("Data teratas (top):", stack[-1])
    else:
        print("Stack kosong.")

while pilihan != 5:
    if pilihan == 1:
        TambahData()
    elif pilihan == 2:
        HapusData()
    elif pilihan == 3:
        ViewData()
    elif pilihan == 4:
        Informasi()
    
    print("\n1. Tambah data (push data)")
    print("2. Hapus data (pop data)")
    print("3. View Data")
    print("4. Informasi Stack")
    print("5. Keluar")
    pilihan = int(input("Masukan pilihan anda: "))
