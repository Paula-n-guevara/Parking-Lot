class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.parking_spots = [ParkingSpot() for _ in range(total_spots)]

    def park_vehicle(self, vehicle):
        if self.is_full():
            print("Parking lot is full.")
        else:
            for spot in self.parking_spots:
                if spot.is_available():
                    spot.park_vehicle(vehicle)
                    self.available_spots -= 1
                    print(f"Vehicle {vehicle.get_license_plate()} parked successfully.")
                    break

    def remove_vehicle(self, vehicle):
        for spot in self.parking_spots:
            if not spot.is_available() and spot.vehicle == vehicle:
                spot.remove_vehicle()
                self.available_spots += 1
                print(f"Vehicle {vehicle.get_license_plate()} removed successfully.")
                break

    def is_full(self):
        return self.available_spots == 0

    def get_available_spots(self):
        return self.available_spots


class ParkingSpot:
    def __init__(self):
        self.spot_number = None
        self.vehicle = None
        self.is_available_spot = True

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.is_available_spot = False

    def remove_vehicle(self):
        self.vehicle = None
        self.is_available_spot = True

    def is_available(self):
        return self.is_available_spot


class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def get_license_plate(self):
        return self.license_plate

    def get_vehicle_type(self):
        return self.vehicle_type
