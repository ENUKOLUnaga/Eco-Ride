from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
        self.__maintenance_status = "Available"
        self.__rental_price = 0.0
    # UC-2 Encapsulation
    @property
    def battery_percentage(self):
        return self._battery_percentage
    @battery_percentage.setter
    def battery_percentage(self, value):
        if 0 <= value <= 100:
            self._battery_percentage = value
        else:
            raise ValueError("Battery percentage must be between 0 and 100")
    def get_maintenance_status(self):
        return self.__maintenance_status
    def set_maintenance_status(self, status):
        self.__maintenance_status = status
    def get_rental_price(self):
        return self.__rental_price
    def set_rental_price(self, price):
        if price >= 0:
            self.__rental_price = price
        else:
            raise ValueError("Rental price cannot be negative")
    @abstractmethod
    def calculate_trip_cost(self, value):
        pass
    def __str__(self):
        return f"{self.vehicle_id} | {self.model} | Battery: {self.battery_percentage}%"