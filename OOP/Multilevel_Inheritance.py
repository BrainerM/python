# Nama: Brainer Mundung
# Tanggal: 5 Maret 2024

# Buat parent class (level 1)
# Buat parent class (level 1)
class GrandFather:
    # Buat variabel
    nama = "Robert Toda"
    __max_umur = '60'
    #Inisialisasi constructor
    def __init__(self, input_nama, input_umur):
        self.nama = input_nama
        self.__max_umur = input_umur

    # Buat metode menulis
    def menulis(self):
        print("Skill grandfather adalah menulis")

    # Buat metode info private
    def __info(self):
        print("Grand Father:",self.nama,"dan umur:",self.__max_umur,",")

# Buat parent class (level 2)
class Father(GrandFather):
    # Buat metode membaca
    def membaca(self):
        print("Skill father adalah membaca buku")
    
    # Buat metode menulis
    def menulis(self):
        print("Skill father adalah menulis jurnal international")

    # Buat metode programmer
    def programmer(self):
        print("Skill father adalah membuat program computer")

# Buat child class 1
class Semmy(Father):
    # Buat metode berenang
    def berenang(self):
        print("Skill Semmy adalah berenang")

    def programmer(self):
        print("Skill Semmy adalah programmer Java")


# Buat child class 2
class Buddy(Father):
    # Buat metode pidato
    def pidato(self):
        print('skill buddy adalah pidato')

    def menulis(self):
        print("Skill buddy adalah menulis buku")


# Create objects from child classes
obj_sem = Semmy("Hendra Bayu", "58")
# Tidak mengakses obj_sem.__info karena private
obj_sem.menulis()
obj_sem.membaca()
obj_sem.berenang()
obj_sem.programmer()
print("============================")

obj_bud = Buddy("John Tambayun", "89")
# Tidak mengakses obj_bud.__info kafena private
obj_bud.membaca()
obj_bud.programmer()
obj_bud.pidato()
obj_bud.menulis()