#################################ZESTAW 3 ZADANIE 1 - ZERO INDEXING###########################################################
import copy
import random
import networkx as nx
import matplotlib.pyplot as plt
import random

class Vertice():
  def __init__(self, n, i):
    self.n = n
    self.i = i

  def __repr__(self):
    return f'[{self.i}]: {self.n}'

def is_graphical_graph(M):
  A = copy.deepcopy(M)
  n = len(A)
  if len(A) <= 1:
    #print("Not enough vertices")
    return False
  odd = sum(1 for i in A if i%2)
  if odd % 2: 
    #print("Wrong number of odd degrees")
    return False
  
  A.sort(reverse=True)

  while True:
    # All elements are equal to 0
    if check_elements(A): return True

    if A[0] >= n or all_elements_greater_than_zero(A): return False

    for i in range(1, A[0] + 1):
      A[i] = A[i] - 1
    A[0] = 0
    A.sort(reverse=True)

def check_elements(A):
  for i in A:
    if i != 0:
      return False
  return True

def all_elements_greater_than_zero(A):
  for i in A:
    if i < 0: return True
  return False

def draw_graph(nodes, edgesWithWeight):
  edges = []
  weight = []
  for el in edgesWithWeight:
    edges.append(el[0])
    weight.append(el[1])

  weightedEdges = []
  for i in range(len(edges)):
    el = (edges[i][0], edges[i][1], weight[i])
    weightedEdges.append(el)

  
  G = nx.Graph()
  nx.circular_layout(G)
  G.add_nodes_from(range(0, nodes))
  #G.add_edges_from(edges)
  G.add_weighted_edges_from(weightedEdges)
  nodes_pos = nx.circular_layout(G)
  nx.draw(G=G, with_labels=True, pos=nodes_pos)
  weight = nx.get_edge_attributes(G, 'weight')
  nx.draw_networkx_edge_labels(G, pos=nodes_pos, edge_labels=weight)
  plt.show()

def process_graph(M):
  if not is_graphical_graph: return None

  edges=[]
  A = copy.deepcopy(M)
  A.sort(reverse=True)
  seq = [Vertice(A[i], i) for i,v in enumerate(A)]
  #print(seq)
  while True:
    if sum(i.n for i in seq) == 0:
      return edges

    for i in range(1, seq[0].n + 1):
      seq[i].n -= 1
      edges.append((seq[0].i, seq[i].i))
    seq[0].n = 0
    seq.sort(reverse=True, key=lambda x: x.n)


def neighbourList(node, edges):
  list = []
  for el in edges:
    if (el[0] == node or el[1] == node):
      if (el[0] == node):
        list.append(el[1])
      else:
        list.append(el[0])
  return list

def DFSRecursiveSearch(ncomponent, verticleIndex, comp, edges):
  #print(comp)
  for fidx in neighbourList(verticleIndex, edges): 
    if [-1, fidx] in comp:
      nonVisitedIdx = comp.index([-1, fidx])
      if comp[nonVisitedIdx][0] == -1:
        comp[nonVisitedIdx][0] = ncomponent
        DFSRecursiveSearch(ncomponent, comp[nonVisitedIdx][1], comp, edges)
  return comp

def check_for_complement(edges, A):
  nodes = len(A)
  ncomponent = 0
  vertices = list(range(0,nodes))
  comp = []
  greatestComponentList = []
  wholeCompList = []
  compVal = []
  
  for v in vertices:
    comp.append([-1, v])

  for v in comp:
    if v[0] == -1:
      ncomponent = ncomponent + 1
      v[0] = ncomponent
      comp = DFSRecursiveSearch(ncomponent, v[1], comp, edges)  

  for i in comp:
    compVal.append(i[0])
  howManyComponents = len(set(compVal))

  if(howManyComponents > 1 or howManyComponents == 0):
    return False

  return True

def generate_random_graphical(amountVertices):
  random.seed()
  A = []
  edges = []
  if (amountVertices == 1):
    A.append(0)
    return A, edges

  while ((is_graphical_graph(A)) == False):
      A.clear()
      for i in range(1,amountVertices+1):
        A.append(random.randint(1, amountVertices - 1))
 
  edges = process_graph(A)  
  return A, edges

def add_weight(edges):
   random.seed()
   weight = []
   howManyEdges = len(edges)
   
   for i in range(howManyEdges):
    weight.append(random.randint(1, 10))
   
   edgesWithWeight = []
   idx = 0
   for el in edges:
    tuple = (el, weight[idx])
    idx = idx + 1
    edgesWithWeight.append(tuple)

   return edgesWithWeight

def generate_random_connected_graph_with_weight(amountVertices):
  if(amountVertices < 1):
    print("Wrong number of vertices")
    return None

  random.seed()
  A = []
  A, edges = generate_random_graphical(amountVertices)
  while (check_for_complement(edges, A) == False):
    A, edges = generate_random_graphical(amountVertices)
  
  edgesWithweight = add_weight(edges)
  return A, edges, edgesWithweight
  
##############################################################################
#jako argument funkcja generate_random_connected_graph_with_weight() przyjmuje
#liczbe wezlow 
#losuje spojny, prosty graf w wagami krawedzi

A, edges, edgesWithWeight = generate_random_connected_graph_with_weight(6)
draw_graph(len(A), edgesWithWeight)