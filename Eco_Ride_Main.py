from src.electric_car import ElectricCar
from src.electric_scooter import ElectricScooter
from fleet.fleet_manager import FleetManager
#UC6-Fleet management
def show_menu():
    print("1. Add Hub")
    print("2. Add Vehicle to Hub")
    print("3. View Vehicles in Hub")
    print("4. Search by hub")
    print("5. Search by Battery")
    print("6. Categorized View")
    print("7. Fleet analysis")
    print("8. Exit")
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
        #Uc-4 Search functionality
        #search by hub
        elif choice == "4":
            hub = input("Enter Hub Name: ")
            vehicles = manager.search_by_hub(hub)

            if not vehicles:
                print("No vehicles found.")
            else:
                for v in vehicles:
                    print(v)
        #search by battery
        elif choice == "5":
            print("\nVehicles with Battery > 80%")
            results = manager.search_by_battery(80)
            for v in results:
                print(v)
        #UC9-Categorized view
        elif choice == "6":  
            categorized = manager.categorize_by_type()
            print("\n--- Electric Cars ---")
            if categorized["ElectricCar"]:
                for car in categorized["ElectricCar"]:
                    print(car)
            else:
                print("No cars available")
            print("\n--- Electric Scooters ---")
            if categorized["ElectricScooter"]:
                for scooter in categorized["ElectricScooter"]:
                    print(scooter)
            else:
                print("No scooters available")
        elif choice == "7":  # UC-10: Fleet Analytics
            summary = manager.fleet_status_summary()
            print("\n--- Fleet Status Summary ---")
            for status, count in summary.items():
                print(f"{status}: {count}")
        elif choice == "8":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")
        
if __name__ == "__main__":
    main()