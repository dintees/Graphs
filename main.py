import numpy as np
from pathlib import Path
from pprint import pprint 
import argparse

from src.lab01.Graph import Graph
from src.lab02.ex6_has_hamiltionian_cycle import has_hamiltonian_cycle 
from src.lab03.ex2_djikstra import djikstra
from src.lab05.ex1_generate_random_flow_network import generate_random_flow_network

def pp(*args):
    pprint(*args, compact=False, width=150)

def main(lab_num):
    incidence_matrix  = Graph.read_from_file(Path("src", "lab01", "incidence.txt"))
    adjacency_matrix = Graph.read_from_file(Path("src", "lab01", "adjacency.txt"))
    adjacency_list = Graph.read_from_file(Path("src", "lab01", "list.txt"))

    if lab_num == 1:
        pp(Graph.adjacency_list_to_adjacency_matrix(adjacency_list))
        pp(Graph.incidence_matrix_to_adjacency_matrix(incidence_matrix))
        pp(Graph.incidence_matrix_to_adjacency_list(incidence_matrix))
        pp(Graph.adjacency_matrix_to_adjacency_list(adjacency_matrix))
        pp(Graph.adjacency_list_to_incidence_matrix(adjacency_list))
        pp(Graph.adjacency_matrix_to_incidence_matrix(adjacency_matrix))

        Graph.showGraph(incidence_matrix, repr_type="incidence")
        Graph.showGraph(adjacency_matrix, repr_type="adjacency")
        Graph.showGraph(adjacency_list, repr_type="list")
    
    elif lab_num == 2:
        edges = Graph.randomNE(5, 8)
        adjacency_list = Graph.edges_to_adjacency_list(edges)
        print(has_hamiltonian_cycle(adjacency_list))

    elif lab_num == 3:
        djikstra()

    elif lab_num == 5:
        nodes, edges = generate_random_flow_network(3)
        print(edges)
        Graph.showWeightedDirectedGraph(edges)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lab", type=int, help="lab number")
    args = parser.parse_args()

    main(args.lab)

