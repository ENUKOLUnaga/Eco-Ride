#  Eco-Ride Urban Mobility & Fleet Management System

Welcome to **Eco-Ride**, an urban mobility system built using **Python OOP**, designed to manage electric vehicles across multiple hubs.
This project demonstrates real-world concepts like encapsulation, inheritance, polymorphism, data integrity, sorting, filtering, analytics, and file persistence.

---

##  Outcomes Covered

1. **OOP Pillars**: Encapsulation, Inheritance, Abstraction, Polymorphism
2. **Python Collections**: Manage fleet data using dictionaries & lists
3. **File I/O**: Read/write fleet data using CSV and JSON
4. **Data Integrity**: Duplicate checks, advanced sorting/filtering
5. **Exception Handling**: Robust user interaction and error handling

---

#  Project Structure

```
EcoRide/
├── src/
│   ├── eco_ride_main.py
│   ├── vehicle.py
│   ├── electric_car.py
│   ├── electric_scooter.py
│   └── fleet_manager.py
├── tests/
│   ├── test_fleet_manager.py
│   ├── test_vehicle.py
│   └── conftest.py
├── data/
│   ├── fleet_data.csv
│   └── fleet_data.json
├── README.md
└── requirements.txt
```

---

#  Features (Use Cases)

## UC1: Basic Fleet Setup

* Create a `Vehicle` object with:

  * `vehicle_id`
  * `model`
  * `battery_percentage`

---

## UC2: Encapsulation & Security

* Sensitive data stored as private attributes:

  * `__maintenance_status`
  * `__rental_price`
* Access via getters & setters
* Validation in setters:

  * battery must be between 0 and 100

---

## UC3: Inheritance & Specialization

* `ElectricCar` and `ElectricScooter` extend `Vehicle`
* Unique attributes:

  * `ElectricCar`: `seating_capacity`
  * `ElectricScooter`: `max_speed_limit`

---

## UC4: Abstraction (Contracts)

* `Vehicle` is an abstract class (ABC)
* Enforces `calculate_trip_cost(distance)` method

---

## UC5: Polymorphism

* `calculate_trip_cost()` is implemented differently:

  * **Car:** `5 + 0.5 * distance`
  * **Scooter:** `1 + 0.15 * duration`
* Same method works for both vehicle types

---

## UC6: Fleet Management (Multiple Hubs)

* Multiple hubs supported using a dictionary:

  * `{ hub_name: [vehicles] }`

---

## UC7: Data Integrity & Equality

* Prevent duplicate vehicle IDs in the same hub
* Override `__eq__()` in `Vehicle` to compare IDs

---

## UC8: Search Functionality

* Search by hub
* Filter by battery level using lambda/filter

---

## UC9: Categorized View

* Group vehicles by type:

  * Cars vs Scooters

---

## UC10: Fleet Analytics

* Count vehicles by status:

  * Available
  * On Trip
  * Under Maintenance

---

## UC11: Alphabetical Sorting

* Sort vehicles in a hub by model name
* Override `__str__()` for clean output

---

## UC12: Advanced Sorting

* Sort by:

  * Battery level
  * Fare price
* Supports descending order

---

## UC13: File I/O (CSV Persistence)

* Save all fleet data into CSV
* Load fleet data from CSV on startup

---

## UC14: File I/O (JSON Integration)

* Save nested hub-vehicle data into JSON
* Serialize custom objects properly

---



