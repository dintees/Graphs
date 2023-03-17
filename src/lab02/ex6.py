from functools import reduce
from ..lab01.Graph import Graph
import time

def fulfill_dirac_theorem(adjacency_list):
    node_count = len(adjacency_list)
    if node_count >= 3: 
        for lst in adjacency_list:
            if len(lst) >= node_count//2:
                continue    
            return False 
    return True 


def is_hamiltonian(adjacency_list):
    if len(adjacency_list) == 0:
        return True
    if fulfill_dirac_theorem(adjacency_list):
        return True

    matrix = Graph.adjacency_list_to_adjacency_matrix(adjacency_list)


def dfs(node, adjacency_matrix, in_stack, stack_count):
    if stack_count == len(adjacency_matrix):
        return True
    for i in range(len(adjacency_matrix)):
        pass


        
    
    return False











    
    return False
    



    # return node_count, edge_count


