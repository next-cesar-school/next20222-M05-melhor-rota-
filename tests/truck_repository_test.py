from model.Truck import Truck
from repository.TruckRepository import Truck_repository

truck1 = Truck("pleasework123", True, "sport club do recife")
truck2 = Truck("pleasework456", False, "santa cruz")
truck3 = Truck("pleasework789", True, "CNC")
repository = Truck_repository()

repository.insert_truck(truck1)
repository.insert_truck(truck2)
repository.insert_truck(truck3)

repository.update_truck_localization("pleasework789", 'oslo')

trucksDict = repository.get_all()
trucks = trucksDict.values()
for truck in trucks:
    print(f'Id: {truck.get_id()}')
    if (truck.get_status()):
        print('Status: Loaded')
    else:
        print('Status: Empty')
    print(f'Localization: {truck.get_localization()}')
    print('------------------------------------------')