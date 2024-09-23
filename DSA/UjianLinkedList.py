#Nama: Mundung, Brainer Mundung
#Tanggal: 28 Februari 2024
#Linked list

class Node: #definisikan kelas Node
    def __init__(self, data): #inisialisasi data dan referensi ke simpul berikutnya
        self.data = data #beri nilai ke atribut data
        self.next = None #beri nilai kosong ke atribut next

class LinkedList: #definisikan kelas LinkedList
    def __init__(self): #inisialisasi kepala linked list
        self.head = None #beri nilai kosong ke kepala linked list

    def print_list(self): #definisikan fungsi print
        current = self.head #mulai dari kepala linked list.
        while current: #lakukan iterasi hingga mencapai akhir linked list
            print("Node ->", current.data) #cetak data dari simpul saat ini
            current = current.next #pindah ke simpul berikutnya
        print () #cetak baris baru

    def add_node_at_beginning(self, data):
        new_node = Node(data) #buat node baru dari data yang diberikan
        new_node.next = self.head
        self.head = new_node

    def add_node_at_middle(self, data, position):
        if position < 0:
            print("Posisi harus bernilai positif.")
            return
        if position == 0:
            self.add_node_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while current:
            if count == position - 1:
                new_node.next = current.next
                current.next = new_node
                print("Node baru berhasil ditambahkan di posisi tengah linked list.")
                return
        current = current.next
        count += 1

        print("Posisi melebihi panjang linked list. Node tidak ditambahkan.")


# Fungsi untuk menampilkan menu
def display_menu():
    print("\nPilihan Menu:")
    print("1. Tampilkan isi linked list")
    print("2. Tambahkan node baru di awal")
    print("3. Tambahkan node baru di tengah")
    print("4. Keluar")


# Membuat linked list dengan 3 node
days_list = LinkedList()
days_list.head = Node("Sapi")
node2 = Node("Ayam")
node3 = Node("Babi")
node4 = Node("Bebek")
Node5 = Node("Kuda")

# Menghubungkan node
days_list.head.next = node2
node2.next = node3
node3.next = node4
node4.next = Node5

# Loop untuk menu
while True:
    display_menu()
    choice = input("Masukkan pilihan Anda: ")

    if choice == '1':
        print("\nView Linked List:")
        days_list.print_list()
    elif choice == '2':     
        objek = input("Masukkan objek baru: ")
        days_list.add_node_at_beginning(objek)
        print("Node baru berhasil ditambahkan di awal linked list.")
    elif choice == '3':
        objek = input("Masukkan objek baru: ")
        posisi = int(input("Masukkan posisi node: "))
        days_list.add_node_at_middle(objek, posisi)
    elif choice == '4':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
