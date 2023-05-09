class Vertice():
  def __init__(self, v: float, n: list):
    self.number = v
    self.neighbours = n

  def __str__(self):
    return f'{self.number}: {self.neighbours}'

  __repr__ = __str__