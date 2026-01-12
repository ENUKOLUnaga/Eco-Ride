import json
#UC14-Save-to-Json
def save_to_json(filename, hubs):
    data = {}
    for hub, vehicles in hubs.items():
        data[hub] = [
            {
                "vehicle_id": v.vehicle_id,
                "model": v.model,
                "battery": v.battery_percentage,
                "type": v.__class__.__name__
            }
            for v in vehicles
        ]

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
