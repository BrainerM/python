#Nama: Brainer Mundung
#Tanggal: Kamis 1 februari 2024

class teacher:
    #Tambahkan variabel
    status = ""
    
    #instace creator (new empty object)
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of class teacher")
        return super().__new__(cls)
    
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("2. Initialize the new instance of class teacher.")
        print("My name is {0} ({1} years old).".format(self.name, self.age));

    #string representator
    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, age={self.age})"
    
    # destructor (object is deleted or destroyed)
    def __del__(self):
        print('3. Object destroyed.')

    # Method 1
    def set_status(self, status):
        self.status = status

    # Method 2
    def get_status(self):
        return str(self.status)

#create object using constructor
t1 = teacher('George Tangka', 20)
t2 = teacher('Green sandaag', 21)

#set status using set_status method
t1.set_status("Mengajar")
t2.set_status("Istirahat")

# Display status using get_status method
print("Status of teacher 1:", t1.get_status())
print("Status of teacher 2:", t2.get_status())

#delete object
del t1