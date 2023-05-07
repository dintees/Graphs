from .Edge import Edge

def find_edge_from_T_to_W(edges, selected_T, W):
  """ Returns the edge with the minimum weight that is both in the set T and W """
  edge = Edge(0, 0, float("inf"))

  for i in edges:
    if (i.begin == selected_T and i.end in W) or (i.begin in W and i.end == selected_T):
      if i.weight < edge.weight:
        edge = i
  return edge

def prim(nodes, edges):
  """ Returns the minimum spanning tree
      Parameters: 
        nodes : list of nodes
        edges : list of Edge objects
      Returns:
        [list of nodes defining the minimum spanning tree, list of edges]
        """
  T = [nodes[0]]
  W = nodes[1:]

  spanning_tree_nodes = [nodes[0]]
  spanning_tree_edges = []
  while W:
    # finding the light edge
    tmp_edge = Edge(0, 0, float("inf"))
    for T_node in T:
      tmp = find_edge_from_T_to_W(edges, T_node, W)
      if tmp.weight < tmp_edge.weight:
        tmp_edge = tmp

    new_node = tmp_edge.begin if tmp_edge.begin in W else tmp_edge.end
    W.remove(new_node)
    T.append(new_node)
    spanning_tree_nodes.append(new_node)
    spanning_tree_edges.append(tmp_edge)
  return spanning_tree_nodes, spanning_tree_edges