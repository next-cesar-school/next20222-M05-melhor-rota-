from model.Truck import Truck
from repository.TruckRepository import TruckRepository
from util.GraphBuilder import GraphBuilder
from wrappers.BestRouteWrapper import BestRouteWrapper

class TruckService:
    truckRepository = TruckRepository()
    graphBuilder = GraphBuilder()
    bestRouteWrapper = BestRouteWrapper()
    nodes = ["D1", "C2", "V3", "V4",
         "D5", "C6", "V7", "V8"]
           
    def addTruck(self):
        id, isFull, localization = self.getData()
        
        truck = Truck(id, isFull, localization)
        self.truckRepository.insert_truck(truck)
        print('Truck sucessfully registered!')

    def updateTruck(self):
        id, isFull, localization = self.getData()
            
        truck = self.truckRepository.get_truck_by_id(id)
        truck.set_isFull(isFull)
        truck.set_localization(localization)
        self.truckRepository.insert_truck(truck)
        print('Truck successfully updated!')

    def removeTruck(self):
        print('Inform the trucks id to remove it')
        id = input()
        self.truckRepository.removeTruck(id)
        print('Truck successfully removed')
    
    def listTrucks(self):
        trucksDict = self.truckRepository.get_all()
        trucks = trucksDict.values()
        for truck in trucks:
            print(f'Id: {truck.get_id()}')
            if (truck.get_isFull()):
                print('Status: Loaded')
            else:
                print('Status: Empty')
            print(f'Localization: {truck.get_localization()}')
            print('------------------------------------------')
    
    def getBestRoute(self):
        print('Inform the trucks Id')
        id = input()
        truck = self.truckRepository.get_truck_by_id(id)
        graph = self.graphBuilder.get_graph()
        path, distance = self.bestRouteWrapper.best_route(graph, truck)

        path_reverse = ' -> '.join(reversed(path))

        print(f'We found the following best path: {path_reverse}; \nDistance: {distance} km.')

    def getData(self):
        print('Please insert plate code')
        id = input()
        isFull = None
        while(isFull == None):
            print('Please inform load status: full or empty')
            status = input()        
            if status.casefold().__eq__('full'):
                isFull = True
            elif status.casefold().__eq__('empty'):
                isFull = False
            else: 
                print('Invalid input, try again')
        
        index = None
        localization = None
        while index == None:
            print('Please inform the trucks localization')
            localization = input()
            #It breaks, fix this!
            index = self.nodes.index(localization)
            if index is None:
                print('Invalid input, try again')
                continue
        
        return id, isFull, localization