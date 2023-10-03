class Coordinate:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
    
  def __str__(self):
    return "(x: " + str(self.x) + ", y: " + str(self.y) + ")"
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  # Getters
  
  def get_x(self):
    return self.x
  
  def get_y(self):
    return self.y
  
class Road:
  # direction can be "best", "worst" or "middle"
  def __init__(self, position: Coordinate, direction: str):
    self.position: Coordinate = position
    self.direction = direction
  
  def __str__(self):
    return "(position: " + str(self.position) + ", direction: " + self.direction + ")"
  
  def __eq__(self, other):
    return self.position == other
  # Getters
  
  def get_direction(self):
    return self.direction

  def get_position(self):
    return self.position
  
class Tree:
  def __init__(self, position: Coordinate):
    self.best: Tree = None
    self.middle: Tree = None
    self.worst: Tree = None
    self.position: Coordinate = position
    self.previous: Tree = None

  def __eq__(self, other):
    return self.position == other.position
  
  def __str__(self):
    tree_str = ""
    if (self.previous):
      tree_str += "\t\t-> previous: " + self.previous.position.__str__() + "\n"
    tree_str += "\t\t-> current: " + self.position.__str__() + "\n"
    if (self.best):
      tree_str += "best: " + self.best.position.__str__() + "\t"
    if (self.middle):
      tree_str += "middle: " + self.middle.position.__str__() + "\t"
    if (self.worst):
      tree_str += "worst: " + self.worst.position.__str__()
    tree_str += "\n"
    return tree_str
