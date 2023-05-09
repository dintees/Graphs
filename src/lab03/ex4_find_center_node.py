from .ex3_find_shortest_paths_matrix import find_shortest_paths_matrix


def find_center_node(edgesWithWeight, n):
    print(find_shortest_paths_matrix(edgesWithWeight, n))
    return ""


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-n", type=int, help="node count")
#     args = parser.parse_args()
#     _, _, edgesWithWeight =generate_random_connected_graph_with_weight(args.n) 
#     print(find_center_node(edgesWithWeight, args.n))