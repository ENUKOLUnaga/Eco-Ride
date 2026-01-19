import pytest
from src.electric_car import ElectricCar

def test_battery_validation():
    with pytest.raises(ValueError):
        ElectricCar("V1", "Tesla", 150, 5)
