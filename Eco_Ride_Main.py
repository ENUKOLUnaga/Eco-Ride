from src.Electric_Car import ElectricCar
from src.Electric_Scooter import ElectricScooter
from fleet.fleet_manager import FleetManager
#UC6-Fleet management
def show_menu():
    print("1. Add Hub")
    print("2. Add Vehicle to Hub")
    print("3. View Vehicles in Hub")
    print("4. Exit")
def main():
    print("Welcome to Eco-Ride Urban Mobility System")
    manager = FleetManager()
    while True:
        show_menu()
        choice = input("Enter choice: ")
        
        if choice == "1":
            hub_name = input("Enter Hub Name: ")
            manager.add_hub(hub_name)
            print("Hub added successfully!")
        elif choice == "2":
            hub = input("Enter Hub Name: ")
            v_type = input("Vehicle Type (car/scooter): ").lower()
            vid = input("Vehicle ID: ")
            model = input("Model: ")
            battery = int(input("Battery Percentage: "))
            if v_type == "car":
                seats = int(input("Seating Capacity: "))
                vehicle = ElectricCar(vid, model, battery, seats)
            elif v_type == "scooter":
                speed = int(input("Max Speed Limit: "))
                vehicle = ElectricScooter(vid, model, battery, speed)
            else:
                print("Invalid vehicle type")
                continue
            manager.add_vehicle_to_hub(hub, vehicle)
            print("Vehicle added to hub successfully!")
        elif choice == "3":
            hub = input("Enter Hub Name: ")
            vehicles = manager.get_vehicles_by_hub(hub)
            if not vehicles:
                print("No vehicles found.")
            else:
                for v in vehicles:
                    print(v)
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")
        
if __name__ == "__main__":
    main()