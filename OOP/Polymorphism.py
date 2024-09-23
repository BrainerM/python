#name: Brainer Mundung
#subject: Object oriented programming
#date: 15 February 2024

# Buat parent class
class Animal:
    def intro(self):
        print("There are many species of Animal")
    
    def speak(self):
        print("Animal have different sound.")

# Buat child class 1
class Cat(Animal):

    def speak(self):
        print("cat speaks meow meow.")

# create child class 2
class Dog(Animal):

    def speak(self):
        print("dog speaks Gukk Gukk Gukk.")

# object of parent class & child class created
obj_binatang = Animal()
obj_kucing = Cat()
obj_anjing = Dog()

# user-defined function is called from obj_binatang (parent class)
obj_binatang.intro()
obj_binatang.speak()

#user-defined function is called from obj_kucing (child class)
obj_kucing.intro()
obj_kucing.speak()

#user-defined function is called from obj_anjing (child class)
obj_anjing.intro()
obj_anjing.speak()