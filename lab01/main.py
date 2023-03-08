import numpy as np
import networkx as nx
import copy
import matplotlib.pyplot as plt
from itertools import combinations
from random import sample, random, randint


class Graph():
    def __init__(self):
        # self.nodes = []
        # self.edges = []
        self.neighbourhood_list = []

    def convert_from_incidence_matrix(self, matrix):
        n = matrix.shape[0] # nodes
        k = matrix.shape[1] # edges
        adjacency_matrix = np.zeros((n, n), dtype=int)
        adjacency_list = [[] for i in range(n)]
        # print(n, k)

        for i in range(k):
            v = []
            for index, j in enumerate(matrix.T[i]):
                if j == 1: 
                    v.append(index)
            if len(v) == 2:
                # matrix
                adjacency_matrix[v[0]][v[1]] = 1
                adjacency_matrix[v[1]][v[0]] = 1

                # list
                if v[0] not in adjacency_list[v[1]]: adjacency_list[v[1]].append(v[0])
                if v[1] not in adjacency_list[v[0]]: adjacency_list[v[0]].append(v[1])
        
        self.neighbourhood_list = adjacency_list

        return adjacency_matrix, adjacency_list

    ###################convert neighbour matrix to neighbour list########################
    def convertNeighbourMatrixToList(self, neighourhoodMatrix) : 
        rows = len(neighourhoodMatrix)
        cols = len(neighourhoodMatrix[0])
        singleNeighourhoodList = [[0 for x in range(rows)]]
        neighourhoodList = []

        for x in range (rows) :
            neighourhoodList.append([])
        
            for y in range(cols) : 
                if (neighourhoodMatrix[x][y] == 1) :
                    neighourhoodList[-1].append(y + 1)
        self.neighbourhood_list = neighourhoodList 
        return neighourhoodList


    def showNeighbourhoodList(self, list) : 
        length = len(list)
        for idx in range(length) :
            print(list[idx])
        
        print()
        
    ###################convert neighbour matrix to matirx of incidence#####################
    def convertNeighbourMatrixToMatrixOfIncidence(self, neighourhoodMatrix) : 
        rows = len(neighourhoodMatrix)
        cols = len(neighourhoodMatrix[0])
        howManyEgdeInGraph = 0
        listOfTuplesEdges = []
        listOfTuplesEdges.append([])
        for x in range (rows) : 
            for y in range(cols) : 
                if (y > x) :
                    if (neighourhoodMatrix[x][y] == 1) :
                        egdeTuple = (x + 1,y + 1)
                        listOfTuplesEdges[-1].append(egdeTuple)
                        howManyEgdeInGraph = howManyEgdeInGraph + 1

        matrixIncident = [[0 for x in range(howManyEgdeInGraph)] for y in range(rows)]
        for y in range(howManyEgdeInGraph) : 
            firstTopNumber = listOfTuplesEdges[0][y][0]
            secondTopNumber = listOfTuplesEdges[0][y][1]
            matrixIncident[firstTopNumber - 1][y] = 1
            matrixIncident[secondTopNumber - 1][y] = 1
        
        return matrixIncident

    ################### convert adjacency list #####################
    def convert_from_adjacency_list(self, adjacency_list):
        lines = adjacency_list.readlines()

        neighbours = []
        for line in lines:
            line = line.rstrip().split(". ")
            line = list(map(int, line[1].split(" ")))
            neighbours.append(line)

        adjacency_matrix = [[1 if i+1 in node_neighbours else 0 for i in range(len(neighbours))] for node_neighbours in neighbours]

        edges = []
        neighbours_copy = copy.deepcopy(neighbours)

        for i in range(len(neighbours_copy)):
            for node in neighbours_copy[i]:
                edges.append([i, node-1])
                neighbours_copy[node-1].remove(i+1)

        incidence_matrix = [[0 for _ in range(len(edges))] for _ in range(len(neighbours))]
        count = 0
        for edge in edges:
            incidence_matrix[edge[0]][count] = 1
            incidence_matrix[edge[1]][count] = 1
            count += 1

        return np.array(adjacency_matrix),  np.array(incidence_matrix)


    def showMatrixOfIncidence(self, matrix) : 
        length = len(matrix)
        for idx in range(length) :
            print(matrix[idx])
        
        print()
    
    def randomNE(n, e):
        """Returns list of e random edges for nodes in range [0, n-1]"""
        if n*(n-1)/2 < e or n < 0 or e < 0:
            return None
        allEdges = combinations(range(1, n+1), 2)
        edges = sample(list(allEdges), e)
        return edges 

    def randomNP(n, p):
        """Returns list of random edges with probability p for nodes in range [0, n-1]"""
        if p < 0 or p > 1 or n < 0:
            return None 
        edges = combinations(range(1, n+1), 2)
        edges = list(filter(lambda _: random() < p, edges))
        return edges

    # !pip install networkx
    def showGraph(g):
        """Shows graph"""
        p = plt.figure(randint(0, 10e10))
        p.set_size_inches(8,8)
        node_opts = {"node_size": 500, "node_color": "tab:red", "edgecolors": "black", "linewidths": 1.0}
        pos = nx.circular_layout(g)
        nx.draw_networkx_nodes(g, pos, **node_opts)
        nx.draw_networkx_labels(g, pos, font_size=14)
        nx.draw_networkx_edges(g, pos, width=2.0, edge_color="black")
        p.tight_layout()
        p.show()
    
    def getNodes(self):
        return list(range(1, len(self.neighbourhood_list)))
    
    def getEdges(self):
        edges = []
        for i, lst in enumerate(self.neighbourhood_list):
            for el in lst:
                edges.append((i+1, el))
        return edges
            
            

matrix = np.loadtxt("neighbour_matrix.txt", dtype=int)
adjacency_list = open("neighbour_list.txt","r+")
# print(matrix)

choice = input("Wejscie:\n1. Macierz sasiedztwa\n2. Lista sasiedztwa\n3. Macierz incydencji  ")

g = Graph()
if choice == '1':
    neighbourList = g.convertNeighbourMatrixToList(matrix)
    matrixIncidence = g.convertNeighbourMatrixToMatrixOfIncidence(matrix)
    print("Lista sasiedztwa:")
    g.showNeighbourhoodList(neighbourList)
    print("Macierz incydencji:")
    g.showMatrixOfIncidence(matrixIncidence)
elif choice == '2':
    adjacency_matrix, incidence_matrix = g.convert_from_adjacency_list(adjacency_list)
    print("Macierz sasiedztwa:")
    g.showNeighbourhoodList(adjacency_matrix)
    print("Macierz incydencji:")
    g.showMatrixOfIncidence(incidence_matrix)
elif choice == '3':
    adjacency_matrix, adjacency_list = g.convert_from_incidence_matrix(matrix)
    print("Neighbourhood matrix:")
    print(adjacency_matrix)
    print("Neighbourhood list:")
    for i,v in enumerate(adjacency_list):
        print(f'{i+1}. {" ".join(map(lambda x: str(x + 1), sorted(v)))}')
# elif choice == "4":
#     # nodeCount = 5 
#     G = nx.Graph()
#     # nodes = list(range(nodeCount)) # [1,2,3,4,5]
#     # edges = Graph.randomNP(nodeCount, 0.3) # [(1,2), (3,1), (4, 2)]
#     edges = g.getEdges()
#     nodes = g.getNodes()
#     print(edges)
#     print(nodes)
#     G.add_nodes_from(nodes)
#     G.add_edges_from(edges)

#     Graph.showGraph(G)
#     #linijka ponizej zeby sie nie zamykalo
#     plt.savefig('graph.png')
else:
  print("Wrong option")


G = nx.Graph()
# edges = g.getEdges()
# nodes = g.getNodes()
nodeCount = 10
nodes = list(range(1, nodeCount + 1)) # [1,2,3,4,5]
# edges = Graph.randomNE(nodeCount, 5) # [(1,2), (3,1), (4, 2)]
edges = Graph.randomNP(nodeCount, 1) # [(1,2), (3,1), (4, 2)]
# incidencincidence_matrixprint(edges)
print(nodes)
G.add_nodes_from(nodes)
G.add_edges_from(edges)

Graph.showGraph(G)
Graph.showGraph(G)
plt.savefig('graph.png')
plt.plot()
