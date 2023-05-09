from .ex3_find_shortest_paths_matrix import find_shortest_paths_matrix
import numpy as np


def find_center_node_and_minimax(edgesWithWeight, n):
    M = find_shortest_paths_matrix(edgesWithWeight, n)
    # print(M)
    sums = [sum(i) for i in M]
    # print(sums)
    dintances = [max(i) for i in M]
    # print(dintances)
    return np.argmin(sums) + 1, np.argmin(dintances) + 1