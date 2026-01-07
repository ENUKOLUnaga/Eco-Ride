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
        existing_ids = [v.vehicle_id for v in self.hubs[hub_name]]
        if vehicle.vehicle_id in existing_ids:
            raise ValueError("Duplicate Vehicle ID not allowed in this hub")
        self.hubs[hub_name].append(vehicle)
    def get_vehicles_by_hub(self, hub_name):
        return self.hubs.get(hub_name, [])
