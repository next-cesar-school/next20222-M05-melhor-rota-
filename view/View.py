from service.TruckService import TruckService

class View:
    truckService = TruckService()
    def execute(self):
        answer = 0
        while answer != '6':
            print('1 - Register truck')
            print('2 - Update truck')
            print('3 - Remove truck')
            print('4 - List trucks')
            print('5 - Calculate best route for truck')
            print('6 - Exit application')
    
            answer = input()
            print()
            match answer:
                case "1":
                    self.truckService.addTruck()
                case "2":
                    self.truckService.updateTruck()
                case "3":
                    self.truckService.removeTruck()
                case "4":
                    self.truckService.listTrucks()
                case "5":
                    self.truckService.getBestRoute()
            print()