import numpy as np

def get_switched_edges(edgeA, edgeB):
    if edgeA[0] == edgeB[0] and edgeA[1] == edgeB[1]:
        return edgeA, edgeB
    return (edgeA[0], edgeB[1]), (edgeA[1], edgeB[0])

def make_k_regular(v_count, deg):
    vertices = [v for v in range(1, v_count)]
    edges = []
    for v in vertices:
        j = 0
        while j<v_count:
            edges.append((v, ))


    pass
