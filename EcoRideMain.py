from src.electric_car import ElectricCar
from src.electric_scooter import ElectricScooter

print("Welcome to Eco-Ride Urban Mobility System")
#vehicle creation
car1 = ElectricCar("C101", "Tesla Model 3", 90, 5)
scooter1 = ElectricScooter("S201", "Xiaomi Pro", 85, 25)
print(car1.model, car1.battery_percentage)
print(scooter1.model, scooter1.battery_percentage)
