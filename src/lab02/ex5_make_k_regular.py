import numpy as np
from .ex1_is_graphical_graph import is_graphical_graph
from .ex2_randomize_graph import process_graph
import random

def even(a):
    return a % 2 == 0 

def edge_exists(edge, edges):
    return len([e for e in edges    if e[0] == edge[0] and e[1] == edge[1] or e[1] == edge[0] and e[0] == edge[1]]) != 0

def switch_edges(edgeA, edgeB, edges):
    if edgeA[0] == edgeB[1] or edgeA[1] == edgeB[0]:
        return False 
    
    newEdgeA = [edgeA[0], edgeB[1]]
    newEdgeB = [edgeA[1], edgeB[0]]
    if edge_exists(newEdgeA, edges) or edge_exists(newEdgeB, edges):
        return False 

    edgeA[0], edgeA[1] = newEdgeA
    edgeB[0], edgeB[1] = newEdgeB
    return True

import random
def generate_k_regular_graph(vertices, degree):
    if degree > vertices or (not even(vertices) and not even(degree)):
        return None
    
    edges = process_graph([degree for _ in range(vertices)])
    edges = [[edge[0], edge[1]] for edge in edges]

    i = 0
    while i < (vertices * degree)**2:
        switch_edges(edges[random.randint(0, vertices-1)], edges[random.randint(0, vertices-1)], edges)
        i+=1

    return edges


    
