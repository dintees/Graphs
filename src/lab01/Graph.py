import numpy as np
import networkx as nx
import copy
import matplotlib.pyplot as plt
from itertools import combinations
from random import sample, random, randint


class Graph():
    def __init__(self):
        pass

    def incidence_matrix_to_adjacency_list(matrix):
        matrix = np.array(matrix)
        n = matrix.shape[0] # nodes
        k = matrix.shape[1] # edges
        adjacency_list = [[] for i in range(n)]

        for i in range(k):
            v = []
            for index, j in enumerate(matrix.T[i]):
                if j == 1: 
                    v.append(index)
            if len(v) == 2:
                if v[0] not in adjacency_list[v[1]]: adjacency_list[v[1]].append(v[0])
                if v[1] not in adjacency_list[v[0]]: adjacency_list[v[0]].append(v[1])
        
        return [tuple([ el for el in lst]) for lst in adjacency_list]

    def incidence_matrix_to_adjacency_matrix(matrix):
        matrix = np.array(matrix)
        n = matrix.shape[0] # nodes
        k = matrix.shape[1] # edges
        adjacency_matrix = np.zeros((n, n), dtype=int)

        for i in range(k):
            v = []
            for index, j in enumerate(matrix.T[i]):
                if j == 1: 
                    v.append(index)
            if len(v) == 2:
                # matrix
                adjacency_matrix[v[0]][v[1]] = 1
                adjacency_matrix[v[1]][v[0]] = 1

        return  adjacency_matrix.tolist()

    def adjacency_matrix_to_adjacency_list(adjacency_matrix) : 
        rows = len(adjacency_matrix)
        cols = len(adjacency_matrix[0])
        adjacency_list = []

        for x in range (rows) :
            adjacency_list.append([])
            for y in range(cols) : 
                if (adjacency_matrix[x][y] == 1) :
                    adjacency_list[-1].append(y)

        return [tuple(lst) for lst in adjacency_list]


    def adjacency_matrix_to_incidence_matrix(adjacency_matrix) : 
        howManyEgdeInGraph = 0
        listOfTuplesEdges = [[]]
        for x, _ in enumerate(adjacency_matrix) : 
            for y, _ in enumerate(adjacency_matrix[0]) : 
                if (y > x) :
                    if (adjacency_matrix[x][y] == 1) :
                        egdeTuple = (x + 1,y + 1)
                        listOfTuplesEdges[-1].append(egdeTuple)
                        howManyEgdeInGraph = howManyEgdeInGraph + 1

        matrixIncident = [[0 for x in range(howManyEgdeInGraph)] for y in range(len(adjacency_matrix))]
        for y in range(howManyEgdeInGraph) : 
            firstTopNumber = listOfTuplesEdges[0][y][0]
            secondTopNumber = listOfTuplesEdges[0][y][1]
            matrixIncident[firstTopNumber - 1][y] = 1
            matrixIncident[secondTopNumber - 1][y] = 1
        
        return matrixIncident

    def adjacency_list_to_adjacency_matrix(adjacency_list):
        neighbours = adjacency_list
        adjacency_matrix = [[1 if i in node_neighbours else 0 for i in range(len(neighbours))] for node_neighbours in neighbours]
        return adjacency_matrix

    def adjacency_list_to_incidence_matrix(adjacency_list):
        neighbours = copy.deepcopy(adjacency_list)
        edges = []
        for i in range(len(neighbours)):
            for node in neighbours[i]:
                edges.append([i, node])
                neighbours[node].remove(i)

        incidence_matrix = [[0 for _ in range(len(edges))] for _ in range(len(neighbours))]
        for count, edge in enumerate(edges):
            incidence_matrix[edge[0]][count] = 1
            incidence_matrix[edge[1]][count] = 1

        return incidence_matrix

    def randomNE(n, e):
        """Returns list of e random edges for nodes in range [0, n-1]"""
        if n*(n-1)/2 < e or n < 0 or e < 0:
            return None
        allEdges = combinations(range(n), 2)
        edges = sample(list(allEdges), e)
        return edges 

    def randomNP(n, p):
        """Returns list of random edges with probability p for nodes in range [0, n-1]"""
        if p < 0 or p > 1 or n < 0:
            return None 
        edges = combinations(range(n), 2)
        edges = list(filter(lambda _: random() < p, edges))
        return edges

    # !pip install networkx
    def showGraph(representation, repr_type, filename = "graph.png"):
        """Shows graph"""
        
        adjacency_list = None
        if repr_type == "list":
            adjacency_list = representation
        elif repr_type == "adjacency":
            adjacency_list= Graph.adjacency_matrix_to_adjacency_list(representation)
        elif repr_type == "incidence":
            adjacency_list = Graph.incidence_matrix_to_adjacency_list(representation)
        
        nodes = Graph.getNodes(adjacency_list)
        edges = Graph.getEdges(adjacency_list)
        
        g = nx.Graph()
        g.add_nodes_from(nodes)
        g.add_edges_from(edges)

        p = plt.figure(randint(0, 10e10))
        p.set_size_inches(8,8)

        node_opts = {"node_size": 500, "node_color": "tab:red", "edgecolors": "black", "linewidths": 1.0}
        pos = nx.circular_layout(g)
        nx.draw_networkx_nodes(g, pos, **node_opts)
        nx.draw_networkx_labels(g, pos, font_size=14)
        nx.draw_networkx_edges(g, pos, width=2.0, edge_color="black")
        p.tight_layout()

        plt.savefig(filename)
    
    def showWeightedGraph(weightedEges):
        g = nx.Graph(weightedEges)

        p = plt.figure(randint(0, 10e10))
        p.set_size_inches(8,8)

        node_opts = {"node_size": 500, "edgecolors": "black", "linewidths": 1.0}
        pos = nx.circular_layout(g)
        edge_labels = nx.get_edge_attributes(g,'weight')
        nx.draw_networkx_nodes(g, pos, **node_opts)
        nx.draw_networkx_labels(g, pos, font_size=20, font_color="white")
        nx.draw_networkx_edges(g, pos, width=2.0, edge_color="black")
        nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels, font_size=20, label_pos=0.4)

        p.tight_layout()

        plt.savefig("temp.png")
    
    def showWeightedDirectedGraph(weightedDirectedEdges):
        g = nx.DiGraph()
        g.add_edges_from(weightedDirectedEdges)

        lastNode = g.size() - 1

        p = plt.figure(randint(0, 10e10))
        p.set_size_inches(8,8)

        pos = nx.circular_layout(g)

        node_opts = {"node_size": 700, "edgecolors": "black", "linewidths": 1.0}
        edge_labels = nx.get_edge_attributes(g, 'weight')
        node_colors = ['red' if (node == 0 or node == len(g.nodes) - 1) 
                            else 'blue' for node in g.nodes()]
        nx.draw_networkx_nodes(g, pos, node_color=node_colors, **node_opts)
        nx.draw_networkx_labels(g, pos, font_size=20, font_color="white")
        nx.draw_networkx_edges(g, pos, width=2.0, edge_color="black", arrowsize=15)
        nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels, font_size=20, label_pos=0.4)

        p.tight_layout()
        plt.axis('off')
        plt.savefig("temp.png")

    
    def getNodes(adjacency_list):
        return list(range(len(adjacency_list)))
    
    def getEdges(adjacency_list):
        edges = []
        for i, lst in enumerate(adjacency_list):
            for el in lst:
                edges.append((i, el))
        return edges
    
    def edges_to_adjacency_list(edges):
        nodes = sorted(list(set([node for edge in edges for node in edge])))
        adjacency_list = [[] for _ in range(len(nodes))]
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
        for edge in edges:
            adjacency_list[edge[1]].append(edge[0])
        return adjacency_list 
        
            
    def read_from_file(path):
        with open(path, "r") as f:
            text = f.read()
            result = [[int(el) for el in line.strip().split(" ")] for line in text.split("\n") if len(line.strip()) > 0]
            return result
    
        