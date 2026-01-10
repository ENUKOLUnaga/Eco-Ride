from src.electric_car import ElectricCar
from src.electric_scooter import ElectricScooter
class FleetManager:
    def __init__(self):
        self.hubs = {}
    def add_hub(self, hub_name):
        if hub_name in self.hubs:
            raise ValueError("Hub already exists")
        self.hubs[hub_name] = []
    def add_vehicle_to_hub(self, hub_name, vehicle):
        if hub_name not in self.hubs:
            raise ValueError("Hub does not exist")
    #Checking for duplicate vehicles by list comprehension
        existing_ids = [v.vehicle_id for v in self.hubs[hub_name]]
        if vehicle.vehicle_id in existing_ids:
            raise ValueError("Duplicate Vehicle ID not allowed in this hub")
        self.hubs[hub_name].append(vehicle)
    def get_vehicles_by_hub(self, hub_name):
        return self.hubs.get(hub_name, [])
    # Uc-8 search vehicles by hub
    def search_by_hub(self, hub_name):
        return self.hubs.get(hub_name, [])
    def search_by_battery(self, threshold):
        return [
            v for hub in self.hubs.values()
            for v in hub if v.battery_percentage > threshold
        ]
    #uc-9 Categorized view
    def categorize_by_type(self):
        categories = {
            "ElectricCar": [],
            "ElectricScooter": []
        }
        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                if isinstance(vehicle, ElectricCar):
                    categories["ElectricCar"].append(vehicle)
                elif isinstance(vehicle, ElectricScooter):
                    categories["ElectricScooter"].append(vehicle)
        return categories
    # UC-10: Fleet Analytics
    def fleet_status_summary(self):
        summary = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }
    # Count vehicles in all hubs
        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                status = vehicle.get_maintenance_status()
                if status in summary:
                    summary[status] += 1
                else:
                    summary[status] = 1
        return summary


