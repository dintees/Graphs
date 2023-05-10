class Edge():
  def __init__(self, begin, end, weight):
    self.begin = begin
    self.end = end
    self.weight = weight
  
  def get_tuple(self):
    return ((self.begin, self.end), self.weight)

  def __str__(self):
    return str(self.get_tuple())

  __repr__ = __str__