import copy

def is_graphical_graph(M):
  """
  Checks if the graph is graphical graph
  Param M: sequence of natural numbers
  Return: true if given graph is graphical
  """
  A = copy.deepcopy(M)
  n = len(A)
  if len(A) <= 1:
    return False
  odd = sum(1 for i in A if i%2)
  if odd % 2: 
    return False
  
  A.sort(reverse=True)

  while True:
    # All elements are equal to 0
    if check_elements(A): return True

    if A[0] >= n or is_element_less_than_zero(A): return False

    # Subtracting the first value from others
    for i in range(1, A[0] + 1):
      A[i] = A[i] - 1
    A[0] = 0
    A.sort(reverse=True)

def check_elements(A):
  """
  Cheks all elements if they are equal to 0
  Param A: sequence of natural number
  Return: true if all elements are equal to 0
  """
  for i in A:
    if i != 0:
      return False
  return True

def is_element_less_than_zero(A):
  """
  Checks all elements if there is at least one less than 0
  Param A: sequence of natural number
  Return: true if there is such as element
  """
  for i in A:
    if i < 0: return True
  return False
