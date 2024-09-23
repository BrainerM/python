#Nama: Brainer Mundung
#Tanggal: Kamis 1 februari 2024

class Student:
    # Class variable
    status = ""

    def __init__(self, name):
        print('Inside constructor')
        self.name = name
        print('All variables initialized')

    # Destructor
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')

    # Instance method
    def show(self):
        print('Ni hao ma, nama saya', self.name)

    # Method 1
    def set_status(self, status):
        print("Setting status")
        self.status = status

    # Method 2
    def get_status(self):
        return str(self.status)

# Create objects using constructor
s1 = Student('Hikari jones')
s2 = Student('David kapal')
s3 = Student('Jarel kandou')

# Call methods
s1.show()
# Set status using set_status method
s1.set_status("ke wc")
# Display status using get_status method
print("Status of s1:", s1.get_status())
# Delete object
del s1

#call method
s2.show()
#set status using set_status method
s2.set_status("Beking tugas")
# Display status using get_status method 
print("Status of s2:", s2.get_status())
# Delete object
del s2

#call method
s3.show()
#set status using set_status method
s3.set_status("Main hp")
# Display status using get_status method
print("Status of s3:", s3.get_status())
# Delete object
del s3