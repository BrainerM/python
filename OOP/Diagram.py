# Nama: Brainer Mundung
# Tanggal: 20 Februari 2024

# parent class
class Vehicle:
    def speed(self):
        print("max speed 150")

    def change_gear(self):
        print("5 gear")

    def show(self):
        print("display vehicle")
        print("----------------")

#child class 1
class Car(Vehicle):

    def speed(self):
        print("max speed 240")

    def change_gear(self):
        print("6 gear")

    def show(self):
        print("Car")
        print("----------------")

#child class 2
class Truck(Vehicle):

    def speed(self):
        print("max speed 200")

    def change_gear(self):
        print("8 gear")

    def show(self):
        print("Truck")
        print("----------------")


# object dari parent class dan child class
kendaraan = Vehicle() # <- Parent Class
mobil = Car() # <- Child Class 1
truk = Truck() # <- Child Class 2 

# user-defined-function called from kendaraan (parent class)
kendaraan.speed() 
kendaraan.change_gear() 
kendaraan.show() 

# user-defined-function called from mobil (child class)
mobil.speed()
mobil.change_gear()
mobil.show()

# user-defined-function called from truk (child class)
truk.speed()
truk.change_gear()
truk.show()