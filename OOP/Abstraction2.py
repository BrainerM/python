from abc import ABC, abstractmethod

# class abstract
class Animal(ABC):
    def _init_(self, species, color, gender):
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

    def show_informations(self):
        print(self.get_name());
        print(self.get_age());
        print(self.get_weight());
        print(self.get_location());
        print(self.get_gender());
        print(self.get_color())
        print(self.get_health());

class Mamalia(Animal):
    def get_weight(self):
        return "Berat adalah: 1 Kilo"
    
    def get_location(self):
        return "Tempat/ Lokasi: Bitung"
    
    def get_health(self):
        return "Kondisi Kesehatan: sick"
    
    def get_name(self):
        return "Nama Hewan: Kucing"
    
    def get_age(self):
        return 'Umur adalah: 2 Tahun'
    
class Bird(Animal):
    def get_weight(self):
        return "Berat adalah: 0.5 Kilo"
    
    def get_location(self):
        return "Tempat/ Lokasi: Tropical Forest"
    
    def get_health(self):
        return "Kondisi Kesehatan: Healthy"
    
    def get_name(self):
        return "Nama Hewan: Elang"
    
    def get_age(self):
        return 'Umur adalah: 5 Tahun'
    
class Fish(Animal):
    def get_weight(self):
        return "Berat adalah: 2 Kilo"
    
    def get_location(self):
        return "Tempat/ Lokasi: Ocean"
    
    def get_health(self):
        return "Kondisi Kesehatan: Moderate"
    
    def get_name(self):
        return "Nama Hewan: Salmon"
    
    def get_age(self):
        return 'Umur adalah: 7 bulan'
    
class Amfibi(Animal):
    def get_weight(self):
        return "Berat adalah: 400 Kilo"
    
    def get_location(self):
        return "Tempat/ Lokasi: River"
    
    def get_health(self):
        return "Kondisi Kesehatan: Weak"
    
    def get_name(self):
        return "Nama Hewan: Crocodile"
    
    def get_age(self):
        return 'Umur adalah: 47 Tahun'
    
# Objects are created and the parameterized constructor is called
obj_cat = Mamalia('Mamalia', 'Warna Hewan: white', 'Jenis Kelamin: Female') # Object 1
obj_bird = Bird('Bird', 'Warna Hewan: white', 'Jenis Kelamin: Female') # object 2
obj_salmon = Fish('Fish', 'Warna Hewan: Blue', 'Jenis Kelamin: Female') # Object 3
obj_buaya = Amfibi('Reptile', 'Warna Hewan: Green Moss', 'Jenis Kelamin: Male') # Object 4

# User defined function is called from object 1
obj_cat.show_informations();
print("");
print("-----------------------------------")
obj_bird.show_informations();
print("")
print("-----------------------------------")
obj_salmon.show_informations();
print("");
print("-----------------------------------")
obj_buaya.show_informations();
print("");
print("-----------------------------------")