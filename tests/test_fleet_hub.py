import pytest
from fleet.fleet_manager import FleetManager
from src.electric_car import ElectricCar
def test_duplicate_vehicle_id():
    fleet = FleetManager()
    fleet.add_hub("Downtown")

    car1 = ElectricCar("C1", "Tesla", 90, 5)
    car2 = ElectricCar("C1", "BMW", 80, 4)  # same ID

    fleet.add_vehicle_to_hub("Downtown", car1)

    with pytest.raises(ValueError):
        fleet.add_vehicle_to_hub("Downtown", car2)
