from fleet.fleet_manager import FleetManager
from src.electric_scooter import ElectricScooter
#Implementation of pytest for battery filter
def test_battery_filter():
    fleet = FleetManager()
    fleet.add_hub("Downtown")

    fleet.add_vehicle_to_hub("Downtown", ElectricScooter("S1", "A", 85, 20))
    fleet.add_vehicle_to_hub("Downtown", ElectricScooter("S2", "B", 60, 25))

    high_battery = fleet.search_by_battery(threshold=80)

    assert len(high_battery) == 1
    assert high_battery[0].vehicle_id == "S1"
