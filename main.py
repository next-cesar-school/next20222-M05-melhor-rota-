from graph import Graph
from wrappers import BestRouteWrapper

nodes = ["V1", "V2", "V3", "V4",
         "V5", "V6", "V7", "V8"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["V1"]["V2"] = 33
init_graph["V1"]["V4"] = 41
init_graph["V1"]["V7"] = 15
init_graph["V2"]["V3"] = 18
init_graph["V2"]["V7"] = 11
init_graph["V3"]["V6"] = 37
init_graph["V3"]["V7"] = 32
init_graph["V3"]["V8"] = 26
init_graph["V4"]["V5"] = 7
init_graph["V4"]["V7"] = 27
init_graph["V4"]["V8"] = 13
init_graph["V5"]["V6"] = 27
init_graph["V5"]["V8"] = 25
init_graph["V6"]["V8"] = 10

grafo = Graph(nodes, init_graph)

brw = BestRouteWrapper()
brw.best_route(grafo, 'V5', 'V3')



