from Truck import Truck
from truck_repository import Truck_repository

truck1 = Truck("pleasework123", True, "sport club do recife")
truck2 = Truck("pleasework456", False, "santa cruz")
truck3 = Truck("pleasework789", True, "CNC")
repository = Truck_repository()

repository.insert_truck(truck1)
repository.insert_truck(truck2)
repository.insert_truck(truck3)

repository.list_all()

repository.update_truck_localization("pleasework789", 'oslo')

repository.list_all()