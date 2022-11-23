from graph import Graph
from dijkstra import dijkstra_algorithm

class Best_route_wrapper(object):

    def best_route(self, grafo, ponto_de_saida, ponto_de_chegada):
        previous_nodes, shortest_path = dijkstra_algorithm(grafo, ponto_de_saida)
        
        caminho = []
        node = ponto_de_chegada

        while node != ponto_de_saida:
            caminho.append(node)
            node = previous_nodes[node]

    # Add the start node manually
        caminho.append(ponto_de_saida)

        print("Minha joia, o caminho mais curto é de {} km, através desses vértices:".format(
            shortest_path[ponto_de_chegada]))
        print(" -> ".join(reversed(caminho)))    