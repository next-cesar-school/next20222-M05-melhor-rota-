from model.graph import Graph
class GraphBuilder:
    def get_graph(self):
        nodes = ["D1", "C2", "V3", "V4",
            "D5", "C6", "V7", "V8"]

        init_graph = {}
        for node in nodes:
            init_graph[node] = {}

        init_graph["D1"]["C2"] = 33
        init_graph["D1"]["V4"] = 41
        init_graph["D1"]["V7"] = 15
        init_graph["C2"]["V3"] = 18
        init_graph["C2"]["V7"] = 11
        init_graph["V3"]["C6"] = 37
        init_graph["V3"]["V7"] = 32
        init_graph["V3"]["V8"] = 26
        init_graph["V4"]["D5"] = 7
        init_graph["V4"]["V7"] = 27
        init_graph["V4"]["V8"] = 13
        init_graph["D5"]["C6"] = 27
        init_graph["D5"]["V8"] = 25
        init_graph["C6"]["V8"] = 10

        g = Graph(nodes, init_graph)

        return g