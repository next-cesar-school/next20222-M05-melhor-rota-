class Truck:
    
    def __init__(self, id, isFull, localization):
        self.__id = id
        self.__isFull = isFull
        self.__localization = localization

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
    
    def get_isFull(self):
        return self.__isFull

    def set_isFull(self, isFull):
        self.__isFull = isFull
    
    def get_localization(self):
        return self.__localization
    
    def set_localization(self, localization):
        self.__localization = localization

