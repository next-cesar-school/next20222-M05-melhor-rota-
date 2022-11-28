from Truck import Truck

class Truck_repository:
    def __init__(self):
        self.__repository= {}

    def insert_truck(self, truck):
        self.__repository.update({truck.get_id(): truck})
    
    def get_all (self):
       return self.__repository

    def update_truck_status(self, id, status):
        truck = self.__repository.get(id)
        truck.set_status(status)
        self.__repository.update({truck.get_id(): truck})
    
    def update_truck_localization(self, id, localization):
        truck = self.__repository.get(id)
        truck.set_localization(localization)
        self.__repository.update({truck.get_id(): truck})

    