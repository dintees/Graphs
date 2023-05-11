############################################ZESTAW 2 ZADANIE 3 - INDEKSOWANIE WIERZCHOLKOW OD ZERA###################################################
from networkx.generators.classic import null_graph
import copy
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def draw_graph_colorized(nodes, edges, tableOfContents, filename="graph.png"):
  plt.figure()
  G = nx.Graph()
  nx.circular_layout(G)
  G.add_nodes_from(range(1, nodes+1))
  G.add_edges_from(edges)
  nodes_pos = nx.circular_layout(G)
  #nx.draw(G=G, with_labels=True, pos=nodes_pos)
  #plt.show()
  color_map = []
  for ncontent in tableOfContents:
    color_map.append(ncontent[1])
  nx.draw(G=G, node_color=color_map, pos=nodes_pos,with_labels=True)
  plt.savefig(filename)

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
  vertices = list(range(1,nodes + 1))
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