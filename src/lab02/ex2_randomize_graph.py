import copy
import random
import networkx as nx
import matplotlib.pyplot as plt
from .Vertice import Vertice
from .ex1_is_graphical_graph import is_graphical_graph

def draw_graph(nodes, edges, filename = "graph.png"):
  plt.figure()
  G = nx.Graph()
  nx.circular_layout(G)
  G.add_nodes_from(range(1, nodes+1))
  G.add_edges_from(edges)
  nodes_pos = nx.circular_layout(G)
  nx.draw(G=G, with_labels=True, pos=nodes_pos)
  plt.savefig(filename)

# degree_seq
def process_graph(M):
  if not is_graphical_graph(M): return None

  edges=[]
  A = copy.deepcopy(M)
  A.sort(reverse=True)
  seq = [Vertice(A[i], i+1) for i,v in enumerate(A)]
  print(seq)
  while True:
    if sum(i.n for i in seq) == 0:
      return edges

    for i in range(1, seq[0].n + 1):
      seq[i].n -= 1
      edges.append((seq[0].i, seq[i].i))
    seq[0].n = 0
    seq.sort(reverse=True, key=lambda x: x.n)

def randomize_graph(A, number_of_iteration = 10): 
  edges = process_graph(A)
  if edges is None: return None

  range_edges = list(range(len(edges)))
  for i in range(number_of_iteration):
    e1 = (-1, -1)
    e2 = (-1, -1)
    while e1 == (-1, -1) or e1 in edges or (e1[1], e1[0]) in edges or e2 in edges or (e2[1], e2[0]) in edges or e1[0] == e1[1] or e2[0] == e2[1]:
      n1, n2 = random.sample(range_edges, k=2) # a = edges[n1][0]
      e1 = (edges[n1][0], edges[n2][1])
      e2 = (edges[n1][1], edges[n2][0])

    # printing transformations:
    # print(edges[n1], edges[n2], end=' -> ') # old
    # print(e1, e2) # new

    e1_old = edges[n1]
    e2_old = edges[n2]

    edges.remove(e1_old)
    edges.remove(e2_old)
    edges.append(e1)
    edges.append(e2)
  
  return edges