from Truck import Truck

class Truck_repository:
    def __init__(self):
        self.__repository= {}

    def insert_truck(self, truck):
        self.__repository.update(truck.getId(), truck)
    
    def list_all (self):
        self.__repository.items()

    def update_truck_status(self, id, status):
        truck = self.__repository.get(id)
        truck.set_status(status)
        self.__repository.update(truck.getId(), truck)
    
    def update_truck_localization(self, id, localization):
        truck = self.__repository.get(id)
        truck.set_localization(localization)
        self.__repository.update(truck.getId(), truck)

    