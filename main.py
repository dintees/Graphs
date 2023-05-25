from pathlib import Path
from pprint import pprint 
import argparse
import os
from pathlib import Path
from random import randint

from src.lab01.Graph import Graph

from src.lab02.ex1_is_graphical_graph import is_graphical_graph
from src.lab02.ex2_randomize_graph import draw_graph, process_graph, randomize_graph
from src.lab02.ex3_findGraphComponent import findGraphComponent, draw_graph_colorized
from src.lab02.ex4_Eulerian_graph import random_eulerian_graph
from src.lab02.ex5_make_k_regular import generate_k_regular_graph
from src.lab02.ex6_has_hamiltionian_cycle import has_hamiltonian_cycle

from src.lab03.Edge import Edge
from src.lab03.ex1_generate_random_connected_graph_with_weight import generate_random_connected_graph_with_weight
from src.lab03.ex2_djikstra import dijkstra
from src.lab03.ex3_find_shortest_paths_matrix import find_shortest_paths_matrix
from src.lab03.ex4_find_center_node import find_center_node_and_minimax
from src.lab03.ex5_prim import prim

from src.lab04.Vertice import Vertice
from src.lab04.ex1_generate_random_digraph import generate_random_digraph, neighbour_list_listning, get_neighbour_list_for_digraph
from src.lab04.ex1_generate_random_digraph import draw_digraph, get_neighbour_matrix_from_digraph, matrix_listning, get_incidence_matrix
from src.lab04.ex2_Kosaraju_algorithm import kosaraju
from src.lab04.ex3_bellman_ford import bellman_ford
from src.lab04.ex4_johnson import johnson

from src.lab05.ex1_generate_random_flow_network import generate_random_flow_network
from src.lab05.ex2_ford_fulkerson import ford_fulkerson

from src.lab06.ex1_page_Rank import page_rank_random_walk, page_rank_vector_iteraton

def pp(*args):
    pprint(*args, compact=False, width=150)

def main(lab_num):
    os.makedirs("figures", exist_ok=True)
    incidence_matrix  = Graph.read_from_file(Path("src", "lab01", "incidence.txt"))
    adjacency_matrix = Graph.read_from_file(Path("src", "lab01", "adjacency.txt"))
    adjacency_list = Graph.read_from_file(Path("src", "lab01", "list.txt"))

    if lab_num == 1:
        try:

            print(f"1.1a adjacency_list_to_adjacency_matrix(adjacency_list={adjacency_list})")
            print(f"Output:")
            pp(Graph.adjacency_list_to_adjacency_matrix(adjacency_list))

            print(f"\n1.1b incidence_matrix_to_adjacency_matrix(incidence_matrix={incidence_matrix})")
            print(f"Output:")
            pp(Graph.incidence_matrix_to_adjacency_matrix(incidence_matrix))

            print(f"\n1.1c incidence_matrix_to_adjacency_list(incidence_matrix={incidence_matrix})")
            print(f"Output:")
            pp(Graph.incidence_matrix_to_adjacency_list(incidence_matrix))

            print(f"\n1.1d adjacency_matrix_to_adjacency_list(adjacency_matrix={adjacency_matrix})")
            print(f"Output:")
            pp(Graph.adjacency_matrix_to_adjacency_list(adjacency_matrix))

            print(f"\n1.1e adjacency_list_to_incidence_matrix(adjacency_list={adjacency_list})")
            print(f"Output:")
            pp(Graph.adjacency_list_to_incidence_matrix(adjacency_list))

            print(f"\n1.1f adjacency_matrix_to_incidence_matrix(adjacency_matrix={adjacency_matrix})")
            print(f"Output:")
            pp(Graph.adjacency_matrix_to_incidence_matrix(adjacency_matrix))
        except Exception as e:
            print("Exercise 1.1 failed", e)

        # 2.
        try:
            Graph.showGraph(incidence_matrix, repr_type="incidence", filename="figures/lab01_ex02a_incidence")
            Graph.showGraph(adjacency_matrix, repr_type="adjacency", filename="figures/lab01_ex02b_adjacency")
            Graph.showGraph(adjacency_list, repr_type="list", filename="figures/lab01_ex02c_list")
        except Exception as e:
            print("Exercise 1.2 failed", e)

        # 3.
        node_count = 4
        edge_count = 5
        print(f"\nrandom_graph(node_count={node_count}, edge_count={edge_count})")
        try:
            random_graph1 = Graph.randomNE(node_count, edge_count)
            print(f"Output:\n {random_graph1}")
            draw_graph(3, random_graph1, "figures/lab01_ex03a_random_graph_nodes_edges")
        except Exception as e:
            print("Exercise 1.3 failed", e)

        # 4.
        node_count = 10
        probability = 0.5
        print(f"\nrandom_graph(node_count={node_count}, probability={probability})")
        try:
            random_graph2 = Graph.randomNP(node_count, probability)
            print(f"Output:\n {random_graph2}")
            draw_graph(9, random_graph2, "figures/lab01_ex03b_random_graph_nodes_probability")
        except Exception as e:
            print("Exercise 1.4 failed", e)
    

    elif lab_num == 2:
        # 1.
        degrees = [1, 3, 3, 7, 2, 3, 1,] # false
        print(f"\n2.1a is_graphical({degrees}")
        try:
            print(f"Output: {is_graphical_graph(degrees)}")
            edges = process_graph(degrees)
            if edges is not None:
                draw_graph(len(degrees), edges, "figures/lab02_ex01_graphical_graph")
        except Exception as e:
            print("Exercise 2.1 failed", e)

        degrees = [1, 3, 2, 3, 2, 4, 1,]
        print(f"\n2.1b is_graphical({degrees}")
        try:
            print(f"Output: {is_graphical_graph(degrees)}")
            edges = process_graph(degrees)
            if edges is not None:
                draw_graph(len(degrees), edges, "figures/lab02_ex01_graphical_graph")
        except Exception as e:
            print("Exercise 2.1 failed", e)


        # 2.
        degrees = [1, 3, 2, 3, 2, 4, 1,]
        iterations = 10
        print(f"\n2.2 randomized_graph(degrees={degrees}, number_of_iterations={iterations})")
        try:
            edges = randomize_graph(degrees, number_of_iteration=iterations)
            print(f"Output: {edges}")
            if edges is not None:
                draw_graph(len(degrees), edges, "figures/lab02_ex02_randomized_graph")
        except Exception as e:
            print("Exercise 2.2 failed:", e)


        # 3.
        nodes_count = 7
        degrees = [1, 3, 2, 3, 2, 4, 1,]
        edges = process_graph(degrees) 
        print(f"\n2.3 find_graph_component(nodes={nodes_count}, edges={edges})")
        try:
            tableOfComponents, greatest, everyComponent = findGraphComponent(nodes=nodes_count,edges=edges)
            print("Lista wszystkich spójnych składowych: ")
            for el in everyComponent:
                print(el)
  
            print("Największa spójna składowa: ")
            print(greatest)
            draw_graph_colorized(nodes_count, edges, tableOfComponents, "figures/lab02_ex03_component_graph")
        except Exception as e:
            print("Exercise 2.3 failed:", e)


        # 4.
        n = 8
        print(f"\n2.4 random_eulerian_graph(n={n})")
        try:
            edges = random_eulerian_graph(n)
            print(f"Output: {edges}")
            draw_graph(n, edges, "figures/lab02_ex04_random_eulerian")
        except Exception as e:
            print("Exercise 2.4 failed:", e)


        # 5.
        vertices_count = 6
        degree_count = 3
        print(f"\n2.5 generate_k_regular_graph(vertices={vertices_count}, degrees={degree_count})")
        try:
            edges = generate_k_regular_graph(vertices_count, degree_count)
            print(f"Output: {edges}")
            draw_graph(5, edges, "figures/lab02_ex05_k_regular_graph" )
        except Exception as e:
            print("Exercise 2.5 failed:", e)


        # 6.
        adjacency_list = adjacency_list
        print(f"\n2.6 has_hamilton_cycle(adjacency_list={adjacency_list})")
        try:
            res = has_hamiltonian_cycle(adjacency_list)
            print(f"Output: {res}")
        except Exception as e:        
            print("Exercise 2.6 failed:", e)

    elif lab_num == 3:

        # 1.
        vertices_count=5
        print(f"\n3.1 generate_random_connected_graph_with_weight(vertices={vertices_count})")
        try:
            _, _, edgesWithWeight= generate_random_connected_graph_with_weight(5) 
            print(f"Output: {edgesWithWeight}")
            Graph.showWeightedGraph(edgesWithWeight, filename="figures/lab03_ex01_random_weighted_graph")
        except Exception as e:
            print("Exercise 3.1 failed:", e)


        # 2.
        nodes_count = 5
        start_node = 1
        _, _, edgesWithWeight= generate_random_connected_graph_with_weight(nodes_count) 
        print(f"\n3.2 dijkstra(edges_with_weight={edgesWithWeight}, nodes_count={nodes_count}, start_node={start_node})")
        try:
            distances, _, _= dijkstra(edgesWithWeight, nodes_count, start_node)
            print(f"Output: {distances}")
            Graph.showWeightedGraph(edgesWithWeight, filename="figures/lab03_ex02_dijkstra")
        except Exception as e:
            print("Exercise 3.2 failed:", e)

        
        # 3.
        nodes_count = 5
        _, _, edgesWithWeight= generate_random_connected_graph_with_weight(nodes_count) 
        print(f"\n3.3 find_shortest_paths_matrix(edges_with_weight={edgesWithWeight}, nodes_count={nodes_count})")
        try:
            matrix = find_shortest_paths_matrix(edgesWithWeight, nodes_count)
            Graph.showWeightedGraph(edgesWithWeight, filename="figures/lab03_ex03_shortest_path_matrix")
            print(f"Output: {matrix}")
        except Exception as e:
            print("Exercise 3.3 failed:", e)


        # 4.
        nodes_count = 5
        _, _, edgesWithWeight= generate_random_connected_graph_with_weight(nodes_count) 
        print("\n3.4 find_center_node()")
        try:
            res = find_center_node_and_minimax(edgesWithWeight, nodes_count)
            Graph.showWeightedGraph(edgesWithWeight, filename="figures/lab03_ex04_find_center_node_and_minimax")
            print(f"Output: center: {res[0]}, minmax: {res[1]}")
        except Exception as e:
            print("Exercise 3.4 failed:", e)
        

        # 5.
        nodes = list(range(1, 13))
        edges = [Edge(1, 2, 3), Edge(1, 5, 9), Edge(1, 3, 2), Edge(2, 5, 4), Edge(3, 5, 6)
                 , Edge(2, 4, 2), Edge(4, 7, 3), Edge(5, 7, 1), Edge(5, 8, 2), Edge(8, 10, 5)
                 , Edge(7, 10, 5), Edge(8, 12, 9), Edge(10, 12, 5), Edge(3, 6, 9), Edge(6, 8, 1)
                 , Edge(6, 9, 2), Edge(9, 11, 2), Edge(8, 11, 6), Edge(11, 12, 3),]
        print(f"\n3.5 prim(nodes={nodes}, edges={edges})")
        try:
            minimal_spanning_tree, spanning_tree_edges = prim(nodes, edges)
            edges = [edge.get_tuple() for edge in spanning_tree_edges]
            print(f"Output: minimal_spanning_tree={minimal_spanning_tree}, spanning_tree_edges={edges}")
            Graph.showWeightedGraph(edges, filename="figures/lab03_ex05_prim_spanning_tree")
        except Exception as e:
            print("Exercise 3.5 failed:", e)


    elif lab_num == 4:
        print("4.1")
        # 1.
        #n - liczba wierzcholkow
        #p - prawdopodobienstwo istnienia krawedzi miedzy wierzcholkami
        n = 5
        p = 0.3
        #wygenerowanie losowego digrafu
        rdigraph = generate_random_digraph(n, p)

        #wyrysowanie wygenerowanego losowego digrafu
        draw_digraph(len(rdigraph.nodes), rdigraph.edges, "figures/lab04_ex01_random_digraph")

        #lista sasiedztwa
        print("Lista sasiedztwa: ")
        neighbour_list_listning(get_neighbour_list_for_digraph(rdigraph),n)
        print("\n")

        print("Macierz sasiedztwa: ")
        matrix_listning(get_neighbour_matrix_from_digraph(rdigraph))
        print("\n")

        print("Macierz incydencji: ")
        print(get_incidence_matrix(rdigraph))
        print("\n")

        # 2.
        print("4.2")
        try:
            # example from presentation
            neighbourhood_list = [
                Vertice(1, [7]),
                Vertice(2, [1, 3, 6, 7]),
                Vertice(3, [2, 6]),
                Vertice(4, [3, 5]),
                Vertice(5, [3]),
                Vertice(6, [5]),
                Vertice(7, [1])
            ]
            nodes = [i.number for i in neighbourhood_list]
            comp = kosaraju(nodes, neighbourhood_list)
            for i in range(max(comp)):
                print(f'Silna spojna skladowa {i+1}: {[nodes[j] for j in range(len(nodes)) if comp[j] == (i + 1) ]}')
        except Exception as e:
            print("Exercise 4.2 failed:", e)

        # 3.
        digraph = generate_random_digraph(5, 0.5)
        nodes = digraph.nodes
        edges = [[list(edge), randint(-5, 10)] for edge in digraph.edges]
        source_node = 0
        print(f"\n4.3 bellman_ford(nodes={nodes}, edges={edges}, source_node={source_node})")
        try:
            is_negative_cycle, d_s, p_s= bellman_ford(nodes, edges, source_node)
            Graph.showWeightedDirectedGraph(((edge[0][0], edge[0][1],{"weight": edge[1]}) for edge in edges), "figures/lab04_ex03_bellman_ford")
            print(f"Output: is_negative_cycle={is_negative_cycle}, d_s={d_s}, p_s={p_s}")
        except Exception as e:
            print("Exercise 4.3 failed:", e)

        # 4.
        digraph = generate_random_digraph(5, 0.5)
        nodes = digraph.nodes
        edges = [[list(edge), randint(-5, 10)] for edge in digraph.edges]
        print(f"\n4.4 johnson(nodes={nodes}, edges={edges}, source_node={source_node})")
        try:
            res = johnson(nodes, edges)
            Graph.showWeightedDirectedGraph(((edge[0][0], edge[0][1],{"weight": edge[1]}) for edge in edges), "figures/lab04_ex04_johnson")
            print(f"Output: {res}")
        except Exception as e:
            print("Exercise 4.4 failed:", e)

    elif lab_num == 5:
        # 1.
        intermediate_layers = 2
        print("\n5.1 generate_random_flow_network()")
        try:
            nodes, edges = generate_random_flow_network(intermediate_layers)
            Graph.showWeightedDirectedGraph(edges, filename="figures/lab05_ex01_random_flow_network")
        except Exception as e:
            print("Exercise 5.1 failed:", e)

        # 2.
        print("\n5.2 ford_fulkerson()")
        try:
            maximum_flow = ford_fulkerson(nodes, edges)
            print("Maximum flow: "+str(maximum_flow))
        except Exception as e:
            print("Exercise 5.2 failed:", e)  

    elif lab_num == 6:     
        graph = {
            0: [4, 5, 8],
            1: [0, 2, 5],
            2: [1,3, 4, 11],
            3: [2, 4, 7, 8, 10],
            4: [2, 6, 7, 8],
            5: [1, 6],
            6: [4, 5, 7],
            7: [3, 6, 8, 11],
            8: [3, 4, 7, 9],
            9: [8],
            10: [3, 8],
            11: [0,7]
        }

        rankSortedMetodA = page_rank_random_walk(graph, 100000)
        rankSortedMethodB = page_rank_vector_iteraton(graph, 1000)

        print("Metoda a - Ranking stron internetowych:")
        for el in rankSortedMetodA:
            print(f'Strona internetowa:',el[0],' Page Rank:',el[1])

        print("\n")

        print("Metoda b - Ranking stron internetowych:")
        for el in rankSortedMethodB:
            print(f'Strona internetowa:',el[0],' Page Rank:',el[1])
                
    else:
        print("There is no laboratory with the given number.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lab", type=int, help="lab number")
    args = parser.parse_args()

    main(args.lab)

