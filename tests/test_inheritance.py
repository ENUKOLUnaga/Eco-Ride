from src.electric_car import ElectricCar
from src.electric_scooter import ElectricScooter

def test_polymorphic_fare():
    car = ElectricCar("C1", "Tesla", 90, 5)
    scooter = ElectricScooter("S1", "Xiaomi", 80, 25)

    assert car.calculate_trip_cost(10) == 10.0
    assert scooter.calculate_trip_cost(10) == 2.5
