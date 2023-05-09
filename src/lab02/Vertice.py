class Vertice():
  def __init__(self, n, i):
    self.n = n
    self.i = i

  def __repr__(self):
    return f'[{self.i}]: {self.n}'