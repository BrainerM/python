#Nama : Brainer Mundung
#Program : Bgtulah

#create class
class Car:
    #constructor tanpa parameter
    def __init__(self):
        self.car_color = "red";
        self.car_brand = "toyota";
        self.car_year = "Tahun 2023";
    #method 1
    def carInfo(self):
        print("Car color is {0}".format(self.car_color))
        print("Car brand is {0}".format(self.car_brand))

    #method 2
    def carPark(self):
        print("Parking time is over. ")
        return "Return car park.!!!"
    
    #method 3
    def carSpeed(self):
        print("Car speed is too fast. ")
        return "Return car speed.!!!"
    
    #method 4
    def carStatus(self):
        return "car is in good contidion"
    
    # main method
    def main(self):
        print("this is main function of class. ")

        # call function
        self.carInfo();
        self.carPark();
        self.carSpeed();
        self.carStatus();

if __name__ == '__main__':
    #create object of class
    obj_car = Car();
    obj_car.main();
    print(obj_car.car_color);
    print(obj_car.car_brand);
    print(obj_car.car_year);
    print("{0}".format(obj_car.carPark()));
    print("{0}".format(obj_car.carSpeed()));
    print("{0}".format(obj_car.carStatus()));

    #car().main()