import numpy as np
from pathlib import Path
from pprint import pprint 
import argparse

from src.lab01.Graph import Graph

from src.lab02.ex1_is_graphical_graph import is_graphical_graph
from src.lab02.ex2_randomize_graph import draw_graph, process_graph, randomize_graph
from src.lab02.ex3_findGraphComponent import draw_graph_colorized, findGraphComponent
from src.lab02.ex4_Eulerian_graph import random_eulerian_graph, find_eulerian_path
from src.lab02.ex5_make_k_regular import make_k_regular
from src.lab02.ex6_has_hamiltionian_cycle import has_hamiltonian_cycle

from src.lab03.Edge import Edge
from src.lab03.ex1_generate_random_connected_graph_with_weight import draw_graph_with_weights, generate_random_connected_graph_with_weight
from src.lab03.ex2_djikstra import dijkstra, seq_dijkstra, display_dijkstra
from src.lab03.ex3_find_shortest_paths_matrix import find_shortest_paths_matrix
from src.lab03.ex4_find_center_node import find_center_node_and_minimax
from src.lab03.ex5_prim import prim

# from src.lab04.Vertice import Vertice
# from src.lab04.ex2_Kosaraju_algorithm import kosaraju

# from src.lab05.ex1_generate_random_flow_network import generate_random_flow_network

def pp(*args):
    pprint(*args, compact=False, width=150)

def main(lab_num):
    incidence_matrix  = Graph.read_from_file(Path("src", "lab01", "incidence.txt"))
    adjacency_matrix = Graph.read_from_file(Path("src", "lab01", "adjacency.txt"))
    adjacency_list = Graph.read_from_file(Path("src", "lab01", "list.txt"))

    if lab_num == 1:
        # 1.
        pp(Graph.adjacency_list_to_adjacency_matrix(adjacency_list))
        pp(Graph.incidence_matrix_to_adjacency_matrix(incidence_matrix))
        pp(Graph.incidence_matrix_to_adjacency_list(incidence_matrix))
        pp(Graph.adjacency_matrix_to_adjacency_list(adjacency_matrix))
        pp(Graph.adjacency_list_to_incidence_matrix(adjacency_list))
        pp(Graph.adjacency_matrix_to_incidence_matrix(adjacency_matrix))

        # 2.
        Graph.showGraph(incidence_matrix, repr_type="incidence", filename="lab01_ex02_incidence")
        Graph.showGraph(adjacency_matrix, repr_type="adjacency", filename="lab01_ex02_adjacency")
        Graph.showGraph(adjacency_list, repr_type="list", filename="lab01_ex02_list")

        # 3.
        # G(n, l)
        random_graph1 = Graph.randomNE(4, 5)
        draw_graph(3, random_graph1, "lab01_ex03a")

        # G(n, p)
        random_graph2 = Graph.randomNP(10, 1)
        draw_graph(9, random_graph2, "lab01_ex03b")
    
    elif lab_num == 2:
        # 1.
        A = [1, 3, 3, 7, 2, 3, 1,] # false
        print("Graphical graph? : ", is_graphical_graph(A))
        
        A = [1, 3, 2, 3, 2, 4, 1,] # true
        print("Graphical graph? : ", is_graphical_graph(A))

        edges = process_graph(A)
        if edges is not None:
            draw_graph(len(A), edges, "lab02_ex01")

        # 2.
        edges = randomize_graph(A, number_of_iteration=10)
        if edges is not None:
            draw_graph(len(A), edges, "lab02_ex02")

        # 3.
        nodes = 9
        edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1,2), (1, 3), (2, 4), (5, 6), (7,8)]
        #edges = [(1, 2), (1, 3), (1, 4), (1, 5), (2,3), (2, 4), (3, 5), (6, 7), (8,9)]
        #tableOfContents = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,2),(7,2)]
        tableOfComponents, greatest, everyComponent = findGraphComponent(nodes,edges)
        print("Lista wszystkich spójnych składowych: ")
        for el in everyComponent:
            print(el)
  
        print("Największa spójna składowa: ")
        print(greatest)
        draw_graph_colorized(nodes, edges, tableOfComponents, "lab02_ex03")

        # 4.
        n = 8
        edges = random_eulerian_graph(n)
        eulerian_path = find_eulerian_path(n, edges)
        print("Cykl Eulera: "+str(eulerian_path))
        draw_graph(n, edges, "lab02_ex04")

        # 5.
        # *** TODO ***
        # graph = make_k_regular(5, 2)

        # 6.
        edges = Graph.randomNE(5, 8)
        adjacency_list = Graph.edges_to_adjacency_list(edges)
        print(has_hamiltonian_cycle(adjacency_list))

    elif lab_num == 3:
        #1.
        A, edges, edgesWithWeight = generate_random_connected_graph_with_weight(5)
        draw_graph_with_weights(len(A), edgesWithWeight, "lab03_ex01")

        #2.
        n = 5
        start_node = 4

        ds, ps, edgesWithWeight = dijkstra(edgesWithWeight, n, start_node)
        print(ds, ps)
        seq = seq_dijkstra(ds, ps, start_node)
        display_dijkstra(seq, ds)
        draw_graph_with_weights(n, edgesWithWeight, "lab03_ex02")

        #3.
        distance_matrix = find_shortest_paths_matrix(edgesWithWeight, n)
        print(distance_matrix)

        #4.
        center, minimax = find_center_node_and_minimax(edgesWithWeight, n)
        print("Centrum =", center)
        print("Minimax =", minimax)

        #5.
        nodes = list(range(1, 13))
        edges = [Edge(1, 2, 3), Edge(1, 5, 9), Edge(1, 3, 2), Edge(2, 5, 4), Edge(3, 5, 6), Edge(2, 4, 2), Edge(4, 7, 3), Edge(5, 7, 1), Edge(5, 8, 2), Edge(8, 10, 5), Edge(7, 10, 5), Edge(8, 12, 9), Edge(10, 12, 5), Edge(3, 6, 9), Edge(6, 8, 1), Edge(6, 9, 2), Edge(9, 11, 2), Edge(8, 11, 6), Edge(11, 12, 3),]

        minimal_spanning_tree, spanning_tree_edges = prim(nodes, edges)

        print("Minimal spanning tree:", minimal_spanning_tree) # text representation
        draw_graph(12, [[i.begin, i.end] for i in spanning_tree_edges], "lab03_ex05") # graphical interpretation
    
    # elif lab_num == 4:

    #     dg = generate_random_digraph(5, 0.5)
    #     res = kosaraju(dg.nodes, dg.edges)
    #     print(res)

    # 1.
    
    # 2.
    # example from presentation
    # neighbourhood_list = [
    #     Vertice(1, [7]),
    #     Vertice(2, [1, 3, 6, 7]),
    #     Vertice(3, [2, 6]),
    #     Vertice(4, [3, 5]),
    #     Vertice(5, [3]),
    #     Vertice(6, [5]),
    #     Vertice(7, [1])
    # ]
    # nodes = [i.number for i in neighbourhood_list]
    # comp = kosaraju(nodes, neighbourhood_list)
    # for i in range(max(comp)):
    #     print(f'Silna spojna skladowa {i+1}: {[nodes[j] for j in range(len(nodes)) if comp[j] == (i + 1) ]}')

    # elif lab_num == 5:
    #     nodes, edges = generate_random_flow_network(3)
    #     print(edges)
    #     Graph.showWeightedDirectedGraph(edges)


    else:
        print("There is no laboratories with the given number.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lab", type=int, help="lab number")
    args = parser.parse_args()

    main(args.lab)

