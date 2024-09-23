# Nama: Brainer Mundung
# Tanggal: 5 Maret 2024

# buat parent class
class Animal:
    type_food = ""
    time = ""
    duration = ""
    high = ""
    # Constructor untuk menginisialisasikan suatu objek
    def __init__(self,name,age, color):
        self.name = name
        self.age = age
        self.color = color
    
    # method 1
    def eat(self,type_food,time):
        self.type_food = type_food
        self.time = time
        print("Food type of animal is: ",self.type_food)
        print("Time to eat for animal is: ",self.time)
    
    # method 2
    def run(self,duration):
        self.duration = duration
        print("The animal's running duration is: ",self.duration)

    # method 3
    def fly(self, high):
        self.high = high
        print("Animal's fly height is: ",self.high)

    # method 4
    def sleep(self,time):
        self.time = time
        print("Animal's sleep time is: ",self.time)
    
    # method 5
    def sound(self):
        print("Animal's sound is: Depends on the animal")

    # method 6
    def show(self):
        print("Name = ",self.name);
        print("Age = ",self.age)
        print("Color = ",self.color);

# buat child class dan wariskan fungsi parent class
class cat(Animal):
    def fly(self):
        print("Cat can't fly")
    
    def sound(self):
        print("Meuw Meuw")
    
    def run(self, duration):
        return super().run(duration)
    
    def play(self):
        print("Cat likes to run")

# buat child class 2 dan wariskan fungsi parent class
class dog(Animal):

    def fly(self):
        print("Dog can't fly")
    
    def sound(self):
        print("Goug Goug")
    
    def run(self,duration):
        return super().run(duration)

    def play(self):
        print("Dog likes to run")

# buat child class 3 dan wariskan fungsi parent class
class bird(Animal):

    def fly(self):
        print("Bird can fly")
    
    def sound(self):
        print("Kiew Kiew")

    def run(self, duration):
        return super().run(duration)
    
    def play(self):
        print("Bird doesn't like to run")

# Menginstantiasikan class kedalam variabel
binatang = Animal('Boddy','18','red')
kucing = cat('kitty', '2', 'white')
anjing = dog('doggy', '3', 'brown')
burung = bird('birdy', '5', 'blue')

# user-defined function is called from object
binatang.eat("Anything", "15 minutes")
binatang.run("Unknown")
binatang.fly("Unknown")
binatang.sleep("8 hours maybe")
binatang.sound()
binatang.show()
print("=========================================")

kucing.fly()
kucing.sound()
kucing.run('15 Minutes')
kucing.play()
kucing.show()
print("==========================================")

anjing.fly()
anjing.sound()
anjing.run("30 Minutes")
anjing.play()
anjing.show()
print("===========================================")

burung.fly()
burung.sound()
burung.run('Unknown')
burung.play()
burung.show()