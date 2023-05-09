from .Vertice import Vertice



def DFS_visit(v, d, f, t, s, neighbourhood_list):
  t[0] += 1
  d[v - 1] = t[0]
  for u in neighbourhood_list[v - 1].neighbours:
    if d[u - 1] == -1:
      DFS_visit(u, d, f, t, s, neighbourhood_list)
  t[0] += 1
  f[v - 1] = t[0]
  s.append(v)

def transpose_graph(n):
    n_T_tmp = [[] for _ in n]
    for i in n:
        for n in i.neighbours:
            n_T_tmp[n - 1].append(i.number)

    n_T = [Vertice(i + 1, v) for i, v in enumerate(n_T_tmp)]
    return n_T
  
def components_r(nr, v, G_T, comp):
  neighbours = next(o.neighbours for o in G_T if o.number == v)
  for u in neighbours:
    if comp[u - 1] == -1:
      comp[u - 1] = nr[0]
      components_r(nr, u, G_T, comp)

def kosaraju(nodes, neighbourhood_list):
  # DFS init
  d = [-1 for i in nodes]
  f = [-1 for i in nodes]
  t = [0]
  s = [] # stack

  for v in nodes:
    if d[v - 1] == -1:
      DFS_visit(v, d, f, t, s, neighbourhood_list)

  # print(d)
  # print(f)
  # print("Stack", s)

  # G^T
  G_T = transpose_graph(neighbourhood_list)
  nr = [0]
  comp = [-1 for _ in range(len(G_T))]

  while len(s) > 0:
    v = s.pop()
    if comp[v - 1] == -1:
      nr[0] += 1
      comp[v - 1] = nr[0]
      components_r(nr, v, G_T, comp)
  return comp
