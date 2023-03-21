############################################ZESTAW 2 ZADANIE 3 - INDEKSOWANIE WIERZCHOLKOW OD ZERA###################################################
from networkx.generators.classic import null_graph
import copy
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def draw_graph(nodes, edges, tableOfContents):
  G = nx.Graph()
  nx.circular_layout(G)
  G.add_nodes_from(range(0, nodes))
  G.add_edges_from(edges)
  nodes_pos = nx.circular_layout(G)
  #nx.draw(G=G, with_labels=True, pos=nodes_pos)
  #plt.show()
  color_map = []    
  for ncontent in tableOfContents:
    color_map.append(ncontent[1])
  nx.draw(G=G, node_color=color_map, pos=nodes_pos,with_labels=True)
  plt.show()

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


def findGraphComponent(nodes, edges):
  #numer skladowej
  ncomponent = 0
  #indeksy wiercholkow
  vertices = list(range(0,nodes))
  #comp[0] oznacza numer spojnej skladowej do ktorej nalezy 
  #wierzcholek v
  #comp[1] indeks tego wierzcholka
  comp = []
  greatestComponentList = []
  wholeCompList = []
  compVal = []
  
  #−1 oznacza, że wierzchołek v jeszcze nie został odwiedzony
  #poczatkowo wszystkie sa nieodwiedzone
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
  greatestComponentNumber = max(set(compVal), key=compVal.count)
  for i in comp:
    if i[0] == greatestComponentNumber:
      greatestComponentList.append(i[1])

  for i in range(1, howManyComponents + 1):
    singleComponent = []
    for el in comp:
      if el[0] == i:
        singleComponent.append(el[1])   
    wholeCompList.append(singleComponent)

  tableOfComponents = []
  for el in comp:
    tuple = (el[1], el[0])
    tableOfComponents.append(tuple)
  return tableOfComponents, greatestComponentList, wholeCompList      
  
if __name__ == "__main__":
  nodes = 9
  edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1,2), (1, 3), (2, 4), (5, 6), (7,8)]
  #edges = [(1, 2), (1, 3), (1, 4), (1, 5), (2,3), (2, 4), (3, 5), (6, 7), (8,9)]
  #tableOfContents = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,2),(7,2)]
  tableOfComponents, greatest, everyComponent = findGraphComponent(nodes,edges)
  print("Lista wszystkich spójnych składowych: ")
  for el in everyComponent:
    print(el)
  
  print("Największa spójna składowa: ")
  print(greatest)
  draw_graph(nodes, edges, tableOfComponents)