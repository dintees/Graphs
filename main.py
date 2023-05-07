import numpy as np
from pathlib import Path
from pprint import pprint 
import argparse

from src.lab01.Graph import Graph

from src.lab02.ex1_is_graphical_graph import is_graphical_graph
from src.lab02.ex2_randomize_graph import draw_graph, process_graph, randomize_graph
from src.lab02.ex6_has_hamiltionian_cycle import has_hamiltonian_cycle

from src.lab03.ex2_djikstra import dijkstra
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
        Graph.showGraph(incidence_matrix, repr_type="incidence", filename="graph01")
        Graph.showGraph(adjacency_matrix, repr_type="adjacency", filename="graph02")
        Graph.showGraph(adjacency_list, repr_type="list", filename="graph03")

        # 3. *** TODO ***
        # G(n, l)
        random_graph1 = Graph.randomNE(10, 10)
        # Graph.showGraph(random_graph1, repr_type="list", filename="graph04")
        # G(n, p)
        random_graph2 = Graph.randomNP(10, 1)
        # Graph.showGraph(random_graph2, repr_type="list", filename="graph05")
    
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
        # *** TODO ***

        # 4.
        # *** TODO ***
        
        # 5.
        edges = Graph.randomNE(5, 8)
        adjacency_list = Graph.edges_to_adjacency_list(edges)

        # 6.
        print(has_hamiltonian_cycle(adjacency_list))

    elif lab_num == 3:
        dijkstra()

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

