from random import randint 
from random import sample
from itertools import permutations
from collections import defaultdict

def generate_random_flow_network(n):
    # wygenerowanie odpowiedniej ilości wierzchołków
    nodes = [i for i in range(2 + n*2 + randint(0, max(n*(n-2), 0)))]
    sourceNode = nodes[0]
    sinkNode = nodes[-1]
    nodesWtihoutEnds = nodes[1:-1]
    #randomizacja wierzchołków
    nodesWtihoutEnds = sample(nodesWtihoutEnds, len(nodesWtihoutEnds))
    
    nodeLayers = get_nodes_divided_into_layers(nodesWtihoutEnds, n)
    
    edgeLayersBetweenNodeLayers = get_edge_layers_between_node_layers(nodeLayers, n)

    edgeLayers = [[(sourceNode, node) for node in nodeLayers[0]]]
    edgeLayers.extend(edgeLayersBetweenNodeLayers)
    edgeLayers.append([(node, sinkNode) for node in nodeLayers[-1]])

    edgesSet = set([edge for edgeLayer in edgeLayers for edge in edgeLayer])
    randomEdges = [edge for edge in list(permutations(nodes, 2)) 
                            if edge[1] != edge[0]
                            and edge[1] != sourceNode
                            and edge[0] != sinkNode
                            and edge not in edgesSet
                            and (edge[1], edge[0]) not in edgesSet]
    edges = list(edgesSet) + sample(randomEdges, 2*n)

    weightedEdges = [(*edge, { "weight": randint(1,10) })for edge in edges]

    return nodes, weightedEdges 


def get_nodes_divided_into_layers(nodes, n):
    nodeLayers = [None for i in range(n)]

    #równomierne podzielenie wierzchołków między warstwy
    step = len(nodes) // n
    for i in range(0, step*n, step):
        nodeLayers[i//step] = nodes[i:i+step]
    
    #losowe przydzielenie pozostałych wierzchołków
    nodes = nodes[i+step:]
    while len(nodes) > 0:
        randIdx = randint(0, len(nodeLayers)-1)
        if len(nodeLayers[randIdx]) < n:
            nodeLayers[randIdx].append(nodes[0])
            nodes = nodes[1:]
            
    return nodeLayers

def get_edge_layers_between_node_layers(nodeLayers, n):
    edgeLayers = []
    for i in range(1, len(nodeLayers)):
        edges = []

        j, k = 0, 0
        lenA, lenB = len(nodeLayers[i-1]), len(nodeLayers[i])
        #pętla dopóki nie wykorzystane zostaną wierzchołki z obu sąsiednich warstw
        while j < lenA or k < lenB:
            edges.append((nodeLayers[i-1][j%lenA], nodeLayers[i][k%lenB]))
            j+=1
            k+=1

        edgeLayers.append(edges)
    return edgeLayers 





    


