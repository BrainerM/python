# Nama: Brainer Mundung
# Tanggal: 20 Februari 2024

#Parent class
class Employee:

    Name = "George Tangka"
    Age = 26
    def show(self):
        self.Name
        self.Age
        print("Name:",self.Name)
        print("Age:",self.Age)
        print("------------------")    
    
# Child class 1
class PermanentEmployee(Employee):
    
    def show(self):
        self.Name = 'Edwin Padu'
        self.Age = 26
        print("Name:",self.Name)
        print("Age:",self.Age)   

    def Salary(self): 
        print("Salary. Rp. 3000")
        print("------------------")        

# Child class 2
class ContractEmployee(Employee):

    def show(self):
        self.Name = 'Reza Haeres'
        self.Age = '35'
        print("Name:",self.Name)
        print("Age:",self.Age)
        
    def HourlyPay(self):        
        print("Hourly pay. Rp. 5000")
        print("------------------")

# object dari parent class dan child class
Pekerja = Employee() # <- Parent Class
Pekerja_tetap = PermanentEmployee() # <- Child Class 1
Kontrak_pekerja = ContractEmployee() # <- Child Class 2

#user-defined function is called Pekerja(Parent class)
Pekerja.show()

#user-defined function is called Pekerja_tetap(child class)
Pekerja_tetap.show()
Pekerja_tetap.Salary()

#user-defined function is called Kontrak_pekerja(pekerja class)
Kontrak_pekerja.show()
Kontrak_pekerja.HourlyPay()
