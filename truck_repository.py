from Truck import Truck

class Truck_repository:
    def __init__(self):
        self.__repository= {}

    def insert_truck(self, truck):
        self.__repository.update({truck.get_id(): truck})
    
    def list_all (self):
        trucks = self.__repository.values()
        for truck in trucks:
            print(f'Id: {truck.get_id()}')
            if (truck.get_status()):
                print('Status: Loaded')
            else:
                print('Status: Empty')
            print(f'Localization: {truck.get_localization()}')
            print('------------------------------------------')

    def update_truck_status(self, id, status):
        truck = self.__repository.get(id)
        truck.set_status(status)
        self.__repository.update({truck.get_id(): truck})
    
    def update_truck_localization(self, id, localization):
        truck = self.__repository.get(id)
        truck.set_localization(localization)
        self.__repository.update({truck.get_id(): truck})

    