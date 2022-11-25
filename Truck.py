class Truck:
    
    def __init__(self, id, status, localization):
        self.__id = id
        self.__status = status
        self.__localization = localization

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
    
    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
    
    def get_localization(self):
        return self.__localization
    
    def set_localization(self, localization):
        self.__localization = localization

