import copy

def is_graphical_graph(M):
  A = copy.deepcopy(M)
  n = len(A)
  if len(A) <= 1:
    print("Not enough vertices")
    return False
  odd = sum(1 for i in A if i%2)
  if odd % 2: 
    print("Wrong number of odd degrees")
    return False
  
  A.sort(reverse=True)

  while True:
    # All elements are equal to 0
    if check_elements(A): return True

    if A[0] >= n or all_elements_greater_than_zero(A): return False

    for i in range(1, A[0] + 1):
      A[i] = A[i] - 1
    A[0] = 0
    A.sort(reverse=True)

def check_elements(A):
  for i in A:
    if i != 0:
      return False
  return True

def all_elements_greater_than_zero(A):
  for i in A:
    if i < 0: return True
  return False
