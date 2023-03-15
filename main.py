from pathlib import Path
from lab01.Graph import Graph
from pprint import pprint 
import numpy as np

def pp(*args):
    pprint(*args, compact=False, width=150)

incidence_matrix  = Graph.read_from_file(Path("lab01", "incidence.txt"))
adjacency_matrix = Graph.read_from_file(Path("lab01", "adjacency.txt"))
adjacency_list = Graph.read_from_file(Path("lab01", "list.txt"))




pp(Graph.adjacency_list_to_adjacency_matrix(adjacency_list))
pp(Graph.adjacency_list_to_incidence_matrix(adjacency_list))
pp(Graph.incidence_matrix_to_adjacency_list(incidence_matrix))
pp(Graph.incidence_matrix_to_adjacency_matrix(incidence_matrix))
pp(Graph.adjacency_matrix_to_adjacency_list(adjacency_matrix))
pp(Graph.adjacency_matrix_to_incidence_matrix(adjacency_matrix))

Graph.showGraph(incidence_matrix, repr_type="incidence")
# Graph.showGraph(adjacency_matrix, repr_type="adjacency")
# Graph.showGraph(adjacency_list, repr_type="list")
