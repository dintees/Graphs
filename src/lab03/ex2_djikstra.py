from .ex1_generate_random_connected_graph_with_weight import generate_random_connected_graph_with_weight
from ..lab01.Graph import Graph


def djikstra():
    A, edges, edgesWithWeight = generate_random_connected_graph_with_weight(6)
    Graph.showWeightedGraph(edgesWithWeight)
    print(A)
    print(edges)
    print(edgesWithWeight)
