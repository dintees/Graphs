from ..lab01.Graph import Graph
def does_fulfill_dirac_theorem(adjacency_list):
    node_count = len(adjacency_list)
    if node_count >= 3: 
        for lst in adjacency_list:
            if len(lst) >= node_count//2:
                continue    
            return False 
    return True 


def has_hamiltonian_cycle(adjacency_list):
    if len(adjacency_list) == 0:
        return True
    if does_fulfill_dirac_theorem(adjacency_list):
        return True

    adjacency_list = [[el for el in lst] for lst in adjacency_list]
    stack = [0]
    while len(stack) > 0:
        curr = stack[-1]

        #check if last node has edge to 0, if yes then return True 
        if len(stack) == len(adjacency_list):
            if 0 in adjacency_list[curr]:
                return True

            #unmark nodes in list and pop node from stack otherwise
            adjacency_list[curr] = [abs(el) for el in adjacency_list[curr]]
            stack.pop()
            continue

        #push node into stack if it is not there, and mark node in adjacency list with minus sign
        for idx, el in enumerate(adjacency_list[curr]):
            if el > 0 and el not in stack:
                stack.append(el)
                adjacency_list[curr][idx] *= -1
                break
        #unmark nodes in list and pop node from stack if are 0 nodes to move to 
        else:
            adjacency_list[curr] = [abs(el) for el in adjacency_list[curr]]
            stack.pop()
            continue
    
    return False