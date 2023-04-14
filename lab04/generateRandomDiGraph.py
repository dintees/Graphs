############################ZESTAW 4 ZADANIE 1###################################
import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import defaultdict

def draw_digraph(nodes, edges):
  G = nx.DiGraph()
  nx.circular_layout(G)
  G.add_nodes_from(range(0, nodes))
  G.add_edges_from(edges)
  nodes_pos = nx.circular_layout(G)
  nx.draw(G=G, with_labels=True, pos=nodes_pos)
  plt.show()

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
 
#n - liczba wierzcholkow
#p - prawdopodobienstwo istnienia krawedzi miedzy wierzcholkami
n = 5
p = 0.3
#wygenerowanie losowego digrafu
rdigraph = generate_random_digraph(5,0.3)

#wyrysowanie wygenerowanego losowego digrafu
draw_graph(len(rdigraph.nodes), rdigraph.edges)

#lista sasiedztwa
neighbour_list_listning(get_neighbour_list_for_digraph(rdigraph),n)