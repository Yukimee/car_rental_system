class Car:
    def __init__(self, car_id, make, model, year, mileage, available=True):
        self.__car_id = car_id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__available = available

    def get_car_details(self):
        return f"{self.__make} {self.__model} ({self.__year}), Mileage: {self.__mileage}, Available: {self.__available}"

    def update_availability(self, status):
        self.__available = status


