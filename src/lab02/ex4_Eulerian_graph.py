import random
from .ex2_randomize_graph import randomize_graph

def random_eulerian_graph(n):
  max_deg = n-1
  max_m = (n*(n-1))/2
  min_m = 2*n
  edgesCount = random.randrange(min_m, max_m, 2)

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
  return edges