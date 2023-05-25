import numpy as np
import random

def rand_int(start, end):
    return random.randint(start, end)

def page_rank_random_walk(graph, N):
  amountVertices = len(graph)
  eachVertexCounter = np.zeros(amountVertices, dtype=int)
  if (amountVertices) == 0 :
    print("Graph has no vertex")
    return
  randomVertexFromRange = rand_int(0, amountVertices - 1)

  for _ in range(N):
    randProbability = rand_int(0, 100)
    if (randProbability <= 15):
      randomVertexFromRange = rand_int(0, amountVertices - 1)
    
    else:     
      nextVertex = random.sample(graph[randomVertexFromRange], k=1)[0]
      randomVertexFromRange = nextVertex
      
    eachVertexCounter[randomVertexFromRange] = eachVertexCounter[randomVertexFromRange] + 1

  print(eachVertexCounter/N)

  rank = []
  for idx,el in enumerate(eachVertexCounter) :
    elToAdd = [idx, el/N]
    rank.append(elToAdd)
  rankSorted = sorted(rank, key=lambda x: x[1], reverse = True)

  return rankSorted



def page_rank_vector_iteraton(graph, max_iter, d = 0.15, epsilon=1e-8):
  amountVertices = len(graph)
  p = np.zeros(amountVertices)
  for i in range(len(p)):
    p[i] = 1/amountVertices

  A = np.zeros((amountVertices, amountVertices))

  for i in range(amountVertices):
    neighbors = graph[i]
    
    if len(neighbors) > 0:
     for j in neighbors:
       A[j][i] = 1 / len(neighbors)
    else:
       A[:, i] = 1 / amountVertices

  for _ in range(max_iter):
   prev_p = p.copy()
   for i in range(amountVertices):
    p[i] = (1 - d) * np.dot(A[i], p) + d / amountVertices
   if np.linalg.norm(p - prev_p) < epsilon:
    break

  rank = []
  for idx,el in enumerate(p):
    elToAdd = [idx, el]
    rank.append(elToAdd)
  rankSorted = sorted(rank, key=lambda x: x[1], reverse = True)

  return rankSorted
