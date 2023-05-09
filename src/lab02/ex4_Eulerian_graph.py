import random
import copy
from .ex2_randomize_graph import randomize_graph
from .ex3_findGraphComponent import findGraphComponent

def random_eulerian_graph(n):
  max_deg = n-1
  max_m = (n*(n-1))/2
  min_m = 2*n
  edgesCount = random.randrange(min_m, max_m, 2)

  while True:
    nodes = []
    counter = edgesCount

    for i in range(max_deg,0,-1):
        comp = counter - 2*i
        if comp > max_deg:                                                                                               
            node_deg = random.randrange(2, max_deg, 2)
        else:
            node_deg = random.randrange(2, comp+1, 2)   
        nodes.append(node_deg)
        counter -= node_deg

    if(counter >= n):
        tmp = int(counter/2)
        nodes.append(2)
        nodes.sort()
        nodes[:tmp] = [x + 2 for x in nodes[:tmp]]
    else:
        nodes.append(counter)

    edges = randomize_graph(nodes)
    if edges != None:
      break

  return edges


def find_eulerian_path(n, src_edges):
    edges = copy.deepcopy(src_edges) 
    nodes = [0 for _ in range(n)]

    for edge in edges:
      nodes[edge[0]-1] += 1
      nodes[edge[1]-1] += 1 
    edges_num = len(edges)
    
    stack = [1]
    neighbours = [[] for _ in range(n)]
    bridges = [[] for _ in range(n)]

    for edge in edges:
        neighbours[edge[0]-1].append(edge[1]-1)
        neighbours[edge[1]-1].append(edge[0]-1)

    while len(stack) != edges_num+1:
      ways = [neighbour for neighbour in neighbours[stack[-1]-1] if neighbour not in bridges[stack[-1]-1] or len(neighbours[stack[-1]-1]) == 1]
      if len(ways) == 0:
        break
      else:
        next = min(ways)

        tableOfComponents, greatest, everyComponent1 = findGraphComponent(n,edges)
        if (stack[-1], next+1) in edges: 
            to_remove = (stack[-1], next+1)
        else: 
            to_remove = (next+1, stack[-1])
        edges.remove(to_remove)
        tableOfComponents, greatest, everyComponent2 = findGraphComponent(n,edges)

        if len(everyComponent1) == len(everyComponent2) or (len(everyComponent1) != len(everyComponent2) and len(ways) == 1):
          neighbours[stack[-1]-1].remove(next)
          neighbours[next].remove(stack[-1]-1)
          stack.append(next+1)
        else:
          edges.append(to_remove)
          bridges[stack[-1]-1].append(next)         

    return stack
