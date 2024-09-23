class Animal:
    # data members of class
    color = "black"     # atribute 1
    species = "Dog"     # atribute 2
    Gender = ""     # atribute 3
    nickname = ""      # atribute 4
    size = ""     # atribute 5

    # constructor
    def __init__(self, species, color):
        self.species = species
        self.color = color

    def func(self):
        print("-----------------------------")
        print("After calling func() method.")
        print("Species type is", self.species)
        print("Its color is", self.color)
        print("its gender is", self.gender)
        print("its nickname is", self.nickname)
        print("its size is", self.size)
        print("-----------------------------")

    def get_gender(self, Gender):
        self.gender = Gender

    def get_nickname(self, nickname):
        self.nickname = nickname

    def get_size(self, size):
        self.size = size

    #destructor method
    def __del__(self):
        print("")

# objects are created and the parameterized constructor is called
obj_cat = Animal('Cat', 'white')    # object 1
obj_dog = Animal('dog', 'black')    # object 2
obj_bird = Animal('bird', 'red')    # object 3
obj_horse = Animal('horse', 'brown')    # object 4
obj_fish = Animal('fish', 'gold')    # object 5
obj_bear = Animal('Bear', 'brown')    # object 6
obj_bee = Animal('bee', 'yellow')    # object 7
obj_wasp = Animal('wasp', 'red')    # object 8
obj_ant = Animal('ant', 'red')    # object 9
obj_crocodile = Animal('Crocodile', 'green')    # object 10

#obj 1
obj_cat.get_gender("male")
obj_cat.get_nickname("Joy")
obj_cat.get_size("small")

#obj 2
obj_dog.get_gender("male")
obj_dog.get_nickname("heli")
obj_dog.get_size("medium")

#obj 3
obj_bird.get_gender("female")
obj_bird.get_nickname("papilo")
obj_bird.get_size("big")

#obj 4
obj_horse.get_gender("male")
obj_horse.get_nickname("owo")
obj_horse.get_size("big")

#obj 5
obj_fish.get_gender("male")
obj_fish.get_nickname("nemo")
obj_fish.get_size("small")

#obj 6
obj_bear.get_gender("male")
obj_bear.get_nickname("princess")
obj_bear.get_size("big")

#obj 7
obj_bee.get_gender("female")
obj_bee.get_nickname("jihyo")
obj_bee.get_size("small")

#obj 8
obj_wasp.get_gender("male")
obj_wasp.get_nickname("Ofu")
obj_wasp.get_size("small")

#obj 9
obj_ant.get_gender("male")
obj_ant.get_nickname("rio")
obj_ant.get_size("small")

#obj 10
obj_crocodile.get_gender("male")
obj_crocodile.get_nickname("Jones Hikari")
obj_crocodile.get_size("big")

del obj_crocodile

# useridefined function is called from object 1
obj_cat.func()
obj_dog.func()
obj_bird.func()
obj_horse.func()
obj_fish.func()
obj_bear.func()
obj_bee.func()
obj_wasp.func()
obj_ant.func()
obj_crocodile.func()

# access the atribute
print("\nDirect acess of attributes using object..")
print(obj_cat.species)
print(obj_dog.species)
print(obj_bird.species)
print(obj_horse.species)
print(obj_fish.species)
print(obj_bear.species)
print(obj_bee.species)
print(obj_ant.species)
print(obj_wasp.species)
print(obj_crocodile.species)