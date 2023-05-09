import numpy as np
from .ex1_is_graphical_graph import is_graphical_graph
from .ex2_randomize_graph import process_graph
import random

# def generate_random_graphical(amountVertices, amountEdges):
#   random.seed()
#   A = []
#   edges = []
#   if (amountVertices == 1):
#     A.append(0)
#     return A, edges

#   while ((is_graphical_graph(A)) == False):
#       A.clear()
#       for i in range(1,amountVertices+1):
#         A.append(random.randint(1, amountVertices - 1))
 
#   edges = process_graph(A)  
#   return A, edges

# def get_switched_edges(edgeA, edgeB):
#     if edgeA[0] == edgeB[0] and edgeA[1] == edgeB[1]:
#         return edgeA, edgeB
#     return (edgeA[0], edgeB[1]), (edgeA[1], edgeB[0])

# def make_k_regular(v_count, deg_count):
#     def even(a, b):
#         return a % b == 2
#     if deg_count < v_count or (even(deg_count) and not even(v_count)):
#         return None


#     print(generate_random_graphical(3))



#     vertices = [v for v in range(1, v_count)]
#     edges = []
#     for v in vertices:
#         j = 0
#         while j<v_count:
#             edges.append((v, ))
#     pass
import random

def generate_k_regular_graph(edges, degree):
    if edges % 2 != 0 or degree % 2 != 0:
        print("Invalid input. The number of edges and degree should be even.")
        return None
    
    if edges < degree:
        print("Invalid input. The number of edges should be greater than or equal to the degree.")
        return None
    
    num_nodes = edges // 2
    graph = [[] for _ in range(num_nodes)]
    
    # Create an initial regular graph
    for i in range(num_nodes):
        for j in range(1, degree // 2 + 1):
            neighbor = (i + j) % num_nodes
            graph[i].append(neighbor)
            graph[neighbor].append(i)
    
    # Rewire the graph to make it more random
    for i in range(num_nodes):
        for j in range(degree // 2):
            if random.random() < 0.5:
                new_neighbor = random.randint(0, num_nodes - 1)
                while new_neighbor == i or new_neighbor in graph[i]:
                    new_neighbor = random.randint(0, num_nodes - 1)
                old_neighbor = graph[i][j]
                graph[i][j] = new_neighbor
                graph[new_neighbor].remove(i)
                graph[new_neighbor].append(old_neighbor)
                graph[old_neighbor].remove(new_neighbor)
                graph[old_neighbor].append(i)
    
    return graph
