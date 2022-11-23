#from graph import Graph
from dijkstra import dijkstra_algorithm


class BestRouteWrapper(object):

    def best_route(self, g, start_node, target_node):
        previous_nodes, shortest_path = dijkstra_algorithm(g, "V3")
        path = []
        node = target_node

        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        # Add the start node manually
        path.append(start_node)
        #print(' -> '.join(reversed(path)))
        # print('We found the following best path with a value of {}.'.format(
        #    shortest_path[target_node]))
        #print(' -> '.join(reversed(path)))
