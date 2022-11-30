from wrappers.dijkstra import dijkstra_algorithm


class BestRouteWrapper(object):

    def route_calculator(self, graph, starter_node, target_node):
        previous_nodes, shortest_path = dijkstra_algorithm(graph, starter_node)

        path = []
        node = target_node

        while node != starter_node:
            path.append(node)
            node = previous_nodes[node]

    # Add the start node manually
        path.append(starter_node)
        return path, shortest_path[target_node]

    def best_route(self, g, truck):
        if truck.get_isFull():
            pathD1, distanceD1 = self.route_calculator(
                g, truck.get_localization(), "D1")
            pathD5, distanceD5 = self.route_calculator(
                g, truck.get_localization(), "D5")
            if distanceD1 <= distanceD5:
                return pathD1, distanceD1
            else:
                return pathD5, distanceD5
        else:
            pathC2, distanceC2 = self.route_calculator(
                g, truck.get_localization(), "C2")
            pathC6, distanceC6 = self.route_calculator(
                g, truck.get_localization(), "C6")
            if distanceC2 <= distanceC6:
                return pathC2, distanceC2
            else:
                return pathC6, distanceC6
