from dijkstra import dijkstra_algorithm

class Best_route_wrapper(object):

    def best_route(self, graph, starting_point, destination):
        previous_nodes, shortest_path = dijkstra_algorithm(graph, starting_point)
        
        path = []
        node = destination

        while node != starting_point:
            path.append(node)
            node = previous_nodes[node]

        path.append(starting_point)

        print("Minha joia, o caminho mais curto é de {} km, através desses vértices:".format(
            shortest_path[destination]))
        print(" -> ".join(reversed(path)))    