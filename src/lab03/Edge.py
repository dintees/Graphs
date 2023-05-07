class Edge():
  def __init__(self, begin, end, weight):
    self.begin = begin
    self.end = end
    self.weight = weight

  def __str__(self):
    return f'{self.begin}-{self.end} [{self.weight}]'

  __repr__ = __str__