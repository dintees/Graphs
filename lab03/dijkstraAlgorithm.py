from generateRandomGraphWithWeight import generate_random_connected_graph_with_weight, draw_graph
from math import inf
import numpy as np
import time
from collections import Counter     

def init(n, start_node):
    ds = [inf for _ in range(n)]
    ps = [None for _ in range(n)]
    ds[start_node-1] = 0
    return ds, ps

def dist(u,v, edgesWithWeight):
    weight = [edge[1] for edge in edgesWithWeight if edge[0] == (u,v) or edge[0] == (v,u)]
    return weight[0]


def relax(u, v, ds, ps, edgesWithWeight): 
    w = dist(u+1, v+1, edgesWithWeight)

    if ds[v] > ds[u] + w:
        ds[v] = ds[u] + w
        ps[v] = u + 1


def arrays_equal(a, b):
    return Counter(a) == Counter(b)

def find_neighbour(ind, edges):
    neighbours = []

    for edge in edges: 
        if edge[0][0] == ind or edge[0][1] == ind:
            if edge[0][0] == ind:
                neighbours.append(edge[0][1]-1)
            elif edge[0][1] == ind:
                neighbours.append(edge[0][0]-1)

    return neighbours

def dijkstra(n, start_node):
    A, edges, edgesWithWeight = generate_random_connected_graph_with_weight(n)

    ds, ps = init(n, start_node)
    S = []
    G = range(1,n+1)

    while not arrays_equal(S, G):
        if(len(S) == 0):
            u = start_node-1
        else:
            tmp = [inf if i == start_node-1 or i+1 in S else ds[i] for i in range(n)]
            u = tmp.index(min(tmp)) 

        S.append(u+1)
        neighbours = find_neighbour(u+1, edgesWithWeight)
        for neighbour in neighbours:
            if neighbour + 1 not in S:
                relax(u, neighbour, ds, ps, edgesWithWeight)

    return ds, ps, edgesWithWeight

def display_dijkstra(seq, ds):
    for i in range(len(ds)):
        print("d("+str(i+1)+") = " + str(ds[i]) + " ==> [",  end='')
        for j in range(len(seq[i])-1, -1, -1):
            if j != 0:
                print(str(seq[i][j]), end=" - ")
            else:
                print(str(seq[i][j]), end="")
        
        print("]")
    
def seq_dijkstra(ds, ps, node):
    seq = [[i+1] for i in range(len(ps))]
    for i in range(len(ds)):
            parent = ps[i]
            if parent != None:
                while parent != node:
                    seq[i].append(parent)
                    tmp = parent - 1
                    parent = ps[tmp]   
                seq[i].append(parent)      
    return seq
    


if __name__ == "__main__":
    n = 9
    start_node = 4

    ds, ps, edgesWithWeight = dijkstra(n, start_node)
    print(ds, ps)
    seq = seq_dijkstra(ds, ps, start_node)
    display_dijkstra(seq, ds)
    draw_graph(n, edgesWithWeight)
