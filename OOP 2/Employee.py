#Nama: Brainer Mundung
#Tanggal: Kamis 1 februari 2024

# create class
class Employee:

    #variabel
    status = ""

    # Parameterized constructor with default parameter values
    def __init__(self, name= "Bryan Dadidu", age="25", salary=8000000):
        self.name = name
        self.age = age
        self.salary = salary

    # display data employee
    def showInfo(self):
        print("Name: {0}.".format(self.name));
        print("Age: {0} years old.".format(self.age));
        print("Salary; Rp. {0}".format(self.salary))

     # method 1
    def set_status(self,status):
        self.status = status

    # method 2
    def get_status(self):
        return str(self.status)

# create multiple objects of the same class
test1 = Employee()
# Call methods
test1.showInfo()
#set status using set status method
test1.set_status('bobo dap')
#Display output of get status method
print("Status Bryan Dadidu adalah: ", test1.get_status())
print("----------------------------------------------------")

test2 = Employee('Semmy Taju', 20, 10000000)
# Call methods
test2.showInfo()
#set status using set status method
test2.set_status('mengajar')
#Display output of get status method
print("Status Semmy Raju adalah: ", test2.get_status())
print("----------------------------------------------------")

test3 = Employee('Hikari Jones', 18, 550000)
# Call methods
test3.showInfo()
#set status using set status method
test3.set_status('pusing')
#Display output of get status method
print("Status Juan Walelang adalah: ", test3.get_status())
print("----------------------------------------------------")

test4 = Employee('David Kapal', 40, 650000)
# Call methods
test4.showInfo()
#set status using set status method
test4.set_status('Stres')
#Display output of get status method
print("Status Patricia Mokodompit adalah: ", test4.get_status())
print("----------------------------------------------------")