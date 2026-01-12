import csv

def save_to_csv(filename, hubs):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Hub", "Vehicle ID", "Model", "Battery", "Type"])
        for hub, vehicles in hubs.items():
            for v in vehicles:
                writer.writerow([
                    hub,
                    v.vehicle_id,
                    v.model,
                    v.battery_percentage,
                    v.__class__.__name__
                ])
