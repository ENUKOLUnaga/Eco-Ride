# UC 1,2: Vehicle Base Class
class Vehicle:
    def __init__(self,vehicle_id,model,battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
        self.__maintenance_status = "Available"
        self.__rental_price=0.0

    # Encapsulation: Getters & Setters
    @property
    def maintenance_status(self):
        return self.__maintenance_status
    @maintenance_status.setter
    def maintenance_status(self, status):
        if 0 < self.battery_percentage <= 100:
            self.__maintenance_status = status
    @property
    def rental_price(self):
        return self.__rental_price
    @rental_price.setter
    def rental_price(self, rental_price):
        if self.rental_price>=0:
            self.__rental_price = rental_price
def main():
    print("Welcome to Eco-Rider Urban Mobility System")
if __name__ == "__main__":
    main()
