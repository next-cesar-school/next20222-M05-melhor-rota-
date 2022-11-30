from model.Truck import Truck

class Truck_repository:
    def __init__(self):
        self.__repository= {}

    def insert_truck(self, truck):
        self.__repository.update({truck.get_id(): truck})

    def get_truck_by_id(self, id):
        return self.__repository.get(id)
    
    def get_all(self):
       return self.__repository
    
    def removeTruck(self, id):
        self.__repository.pop(id)

    def update_truck(self, id, status, localization):
        truck = self.__repository.get(id)
        truck.set_isFull(status)
        truck.set_localization(localization)
        self.__repository.update({truck.get_id(): truck})

    def update_truck_status(self, id, status):
        truck = self.__repository.get(id)
        truck.set_isFull(status)
        self.__repository.update({truck.get_id(): truck})
    
    def update_truck_localization(self, id, localization):
        truck = self.__repository.get(id)
        truck.set_localization(localization)
        self.__repository.update({truck.get_id(): truck})

    