############################ZESTAW 4 ZADANIE 1###################################
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
from collections import defaultdict

#n - liczba wierzcholkow
#p - prawdopodobienstwo istnienia krawedzi miedzy wierzcholkami
def generate_random_digraph(n, p):
  random_digraph = nx.DiGraph()
  random_digraph.add_nodes_from(range(0, n))
  for i in range(n):
    for j in range(n):
      if i != j and random.random() < p:
        random_digraph.add_edge(i,j)

  return random_digraph

def draw_digraph(nodes, edges, filename):
  G = nx.DiGraph()
  nx.circular_layout(G)
  G.add_nodes_from(range(0, nodes))
  G.add_edges_from(edges)
  nodes_pos = nx.circular_layout(G)
  nx.draw(G=G, with_labels=True, pos=nodes_pos)
  plt.savefig(filename)

def get_neighbour_list_for_digraph(G):
  neighbour_list = defaultdict(list)
  for edge in G.edges:
      e1, e2 = edge
      neighbour_list[e1].append(e2)
  #return list(neighbour_list.values())
  return neighbour_list

def neighbour_list_listning(list, nodes):
  for i in range(nodes):
    print(i, ": ", list[i])

def get_neighbour_matrix_from_digraph(G):
  for edge in G.edges:
      e1, e2 = edge
  num_vertices = G.number_of_nodes()
  adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
  for u, v in G.edges:
      adjacency_matrix[u][v] = 1
  return adjacency_matrix

def matrix_listning(matrix):
  for row in matrix:
    print(" ".join(str(element) for element in row))

def get_incidence_matrix(graph):
   # Uzyskanie listy wierzchołków i krawędzi digrafu
  vertices = list(graph.nodes())
  edges = list(graph.edges())

  # Tworzenie macierzy incydencji jako tablicy NumPy
  incidence_matrix = np.zeros((len(vertices), len(edges)), dtype=int)

  # Wypełnianie macierzy incydencji
  for j, edge in enumerate(edges):
      u, v = edge
      incidence_matrix[vertices.index(u)][j] = -1
      incidence_matrix[vertices.index(v)][j] = 1
  return incidence_matrix