import unittest
from src.electric_car import ElectricCar
class TestVehicle(unittest.TestCase):
    def test_vehicle_creation(self):
        car = ElectricCar("C100", "Tesla", 80, 5)
        self.assertEqual(car.vehicle_id, "C100")
        self.assertEqual(car.model, "Tesla")
        self.assertEqual(car.battery_percentage, 80)
    def test_battery_validation(self):
        car = ElectricCar("C101", "BMW", 50, 5)
        with self.assertRaises(ValueError):
            car.battery_percentage = 150
    def test_encapsulation_maintenance(self):
        car = ElectricCar("C102", "Audi", 70, 4)
        car.set_maintenance_status("Under Maintenance")
        self.assertEqual(car.get_maintenance_status(), "Under Maintenance")
    def test_vehicle_equality(self):
        car1 = ElectricCar("C200", "Tesla", 90, 5)
        car2 = ElectricCar("C200", "Tesla X", 85, 7)
        self.assertEqual(car1, car2)

if __name__ == "__main__":
    unittest.main()
