class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print("Node ->", current.data)
            current = current.next

    def add_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Fungsi untuk menampilkan menu
def display_menu():
    print("\nPilihan Menu:")
    print("1. Tampilkan isi linked list")
    print("2. Tambahkan node baru di awal")
    print("3. Keluar")

# Membuat linked list dengan 3 node
days_list = LinkedList()
days_list.head = Node("minggu")
node2 = Node("senin")
node3 = Node("selasa")

# Menghubungkan node
days_list.head.next = node2
node2.next = node3

# Loop untuk menu
while True:
    display_menu()
    choice = input("Masukkan pilihan Anda: ")

    if choice == '1':
        print("\nIsi linked list:")
        days_list.print_list()
    elif choice == '2':
        new_day = input("Masukkan nama hari baru: ")
        days_list.add_node_at_beginning(new_day)
        print("Node baru berhasil ditambahkan di awal linked list.")
    elif choice == '3':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
