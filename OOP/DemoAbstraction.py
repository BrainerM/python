#Nama: Mundung, Brainer keneth
#Subject: Object oriented programming(OOP)

from abc import ABC, abstractmethod

# class abstract
class Animal(ABC):
    def __init__(self,species, color, gender):
        self.species = species
        self.color = color
        self.gender = gender

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def get_location(self):
        pass

    @abstractmethod
    def get_health(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_age(self):
       pass

    def get_gender(self):
        return self.gender;

    def get_color(self):
        return self.color;

    def get_species(self):
        return self.species;

    def show_information(self):
        print("Nama Hewan:", self.get_name());
        print("Spesies:", self.get_species())
        print("Umur:", self.get_age());
        print("Berat:", self.get_weight());
        print("Tempat/Lokasi:", self.get_location());
        print("Jenis Kelamin:", self.get_gender());
        print("Warna Hewan:",self.get_color());
        print("Kondisi Kesehatan:",self.get_health());
        
class Mamalia(Animal):
    def get_weight(self):
        return "3 kilo"
    
    def get_location(self):
        return "bitung"
    
    def get_health(self):
        return "kurang sehat"
    
    def get_name(self):
        return "Kucing"
    
    def get_age(self):
        return "2 Tahun"
    
    
class Bird(Animal):
    def get_weight(self):
        return "15 kilo"

    def get_location(self):
        return "Jawa"
    
    def get_health(self):
        return "sehat"
    
    def get_name(self):
        return "Elang"
    
    def get_age(self):
        return "5 Tahun"
    
    
class Fish(Animal):
    def get_weight(self):
        return "2 kilo"

    def get_location(self):
        return "Laut/sungai"
    
    def get_health(self):
        return "Moderate"
    
    def get_name(self):
        return "Salmon"
    
    def get_age(self):
        return '7 bulan'
    
class Amfibi(Animal):
    def get_weight(self):
        return "80 Kilo"
    
    def get_location(self):
        return "sungai"
    
    def get_health(self):
        return "Sehat"
    
    def get_name(self):
        return "Buaya"
    
    def get_age(self):
        return "15 Tahun"
    
    
# object are created and the parameterized constructor is called
obj_cat = Mamalia('Mamalia', 'white', 'Betina') # Object 1
obj_bird = Bird('Burung', 'white', 'Jantan') # object 2
obj_salmon = Fish('Ikan', 'Silver', 'Betina') # Object 3
obj_buaya = Amfibi('Reptil', 'Green', 'Jantan') # Object 4

# user-defined function is called from object
obj_cat.show_information();
print("");
obj_bird.show_information();
print("");
obj_salmon.show_information();
print("");
obj_buaya.show_information();