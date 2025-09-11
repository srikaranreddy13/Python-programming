from abc import ABC, abstractmethod
import time
class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate   
        self.__owner_name = owner_name         
        self.entry_time = None                 
    def get_license_plate(self):
        return self.__license_plate
    def get_owner_name(self):
        return self.__owner_name
    def set_owner_name(self, new_name):
        self.__owner_name = new_name
    def display(self):
        print(f"Vehicle [{self.__license_plate}] owned by {self.__owner_name}")
    def calculate_parking_fee(self, hours):
        return 0  
class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike [{self.get_license_plate()}] | Owner: {self.get_owner_name()} | Helmet Required: {self.helmet_required}")
    def calculate_parking_fee(self, hours):
        return 20 * hours
class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats
    def display(self):
        print(f"Car [{self.get_license_plate()}] | Owner: {self.get_owner_name()} | Seats: {self.seats}")
    def calculate_parking_fee(self, hours):
        return 50 * hours
class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive
    def display(self):
        print(f"SUV [{self.get_license_plate()}] | Owner: {self.get_owner_name()} | 4WD: {self.four_wheel_drive}")
    def calculate_parking_fee(self, hours):
        return 70 * hours
class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity=10000):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity
    def display(self):
        print(f"Truck [{self.get_license_plate()}] | Owner: {self.get_owner_name()} | Max Load: {self.max_load_capacity}kg")
    def calculate_parking_fee(self, hours):
        return 100 * hours
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.__size = size       
        self.__occupied = False   
        self.__vehicle = None
    def get_status(self):
        return "Occupied" if self.__occupied else "Available"
    def assign_vehicle(self, vehicle):
        if self.__occupied:
            print(f"Spot {self.spot_id} is already occupied.")
            return False
        if self.__size == "S" and isinstance(vehicle, Bike):
            self.__vehicle = vehicle
        elif self.__size == "M" and isinstance(vehicle, Car):
            self.__vehicle = vehicle
        elif self.__size == "L" and isinstance(vehicle, SUV):
            self.__vehicle = vehicle
        elif self.__size == "XL" and isinstance(vehicle, Truck):
            self.__vehicle = vehicle
        else:
            print(f"Vehicle {vehicle.get_license_plate()} does not fit in spot {self.spot_id} ({self.__size}).")
            return False
        self.__occupied = True
        vehicle.entry_time = time.time()
        print(f"Vehicle {vehicle.get_license_plate()} parked at spot {self.spot_id}.")
        return True
    def remove_vehicle(self):
        if not self.__occupied:
            print(f"Spot {self.spot_id} is already empty.")
            return None, 0
        vehicle = self.__vehicle
        hours = max(1, int((time.time() - vehicle.entry_time) // 3600))  
        self.__vehicle = None
        self.__occupied = False
        print(f"Vehicle {vehicle.get_license_plate()} left spot {self.spot_id}.")
        return vehicle, hours
class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []
    def add_spot(self, spot):
        self.spots.append(spot)
    def show_spots(self):
        for spot in self.spots:
            print(f"Spot {spot.spot_id} ({spot._ParkingSpot__size}): {spot.get_status()}")
    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.get_status() == "Available":
                if spot.assign_vehicle(vehicle):
                    return True
        print(f"No suitable spot found for {vehicle.get_license_plate()}.")
        return False
    def unpark_vehicle(self, vehicle, payment_method):
        for spot in self.spots:
            if spot.get_status() == "Occupied" and spot._ParkingSpot__vehicle == vehicle:
                vehicle, hours = spot.remove_vehicle()
                fee = vehicle.calculate_parking_fee(hours)
                payment_method.process_payment(fee)
                return True
        print(f"Vehicle {vehicle.get_license_plate()} not found in lot.")
        return False
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} in cash.")
class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using credit/debit card.")
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI.")
if __name__ == "__main__":
    lot = ParkingLot("Smart Parking Lot")
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "L"))
    lot.add_spot(ParkingSpot(4, "XL"))
    v1 = Bike("KA01AB1234", "Alice")
    v2 = Car("KA02CD5678", "Bob")
    v3 = SUV("KA03EF9999", "Charlie")
    v4 = Truck("KA04GH0001", "David")
    print("\n--- Vehicle Details ---")
    for v in [v1, v2, v3, v4]:
        v.display()
    print("\n--- Parking Vehicles ---")
    lot.park_vehicle(v1)
    lot.park_vehicle(v2)
    lot.park_vehicle(v3)
    lot.park_vehicle(v4)
    print("\n--- Parking Lot Status ---")
    lot.show_spots()
    print("\n--- Unparking Vehicles & Payments ---")
    lot.unpark_vehicle(v1, CashPayment())
    lot.unpark_vehicle(v2, CardPayment())
    lot.unpark_vehicle(v3, UPIPayment())
    lot.unpark_vehicle(v4, CashPayment())