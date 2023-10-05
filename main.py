from scipy.spatial.distance import cityblock
from laberinto import Tree, Coordinate, Road

labyrinth = [
    ["1", "0", "S", "0", "0", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["0", "1", "0", "1", "1", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "1", "1", "1"],
    ["0", "0", "1", "1", "0", "1", "1", "0", "0", "1", "1", "1", "1", "0", "1", "0", "1", "0", "0", "1"],
    ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "1", "1", "0", "1"],
    ["1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1"],
    ["1", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "1", "1", "1", "1", "0", "1", "1", "0", "1"],
    ["1", "0", "1", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "0", "1", "0", "1", "0", "0", "1"],
    ["1", "0", "0", "0", "1", "0", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0", "0", "1", "0", "1"],
    ["1", "0", "1", "1", "1", "0", "1", "1", "0", "1", "0", "1", "0", "0", "0", "0", "1", "1", "0", "1"],
    ["1", "0", "0", "0", "1", "0", "1", "1", "0", "1", "0", "1", "1", "1", "1", "0", "1", "1", "0", "1"],
    ["1", "0", "1", "1", "1", "0", "1", "0", "0", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "1"],
    ["0", "0", "0", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "1", "1"],
    ["0", "0", "0", "0", "0", "1", "0", "0", "1", "0", "1", "0", "1", "0", "0", "0", "1", "0", "0", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "0", "0", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "1", "1", "1", "1"],
    ["0", "1", "0", "0", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1"],
    ["0", "0", "0", "1", "1", "1", "1", "0", "1", "1", "1", "0", "0", "0", "0", "1", "1", "1", "1", "1"],
    ["1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "1"],
    ["1", "1", "0", "0", "1", "1", "0", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "1"],
    ["1", "1", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "E", "1"],
]

start = Coordinate(2, 0)
end = Coordinate(18, 19)
      
def get_manhattan_distance(position: Coordinate) -> int:
  return cityblock([position.x, position.y], [end.x, end.y])

def get_labyrinth_value(position: Coordinate) -> str:
  return labyrinth[position.x][position.y]

# Returns None in case there is no way to go, returns a coordinate array ordered from best to worst position otherwise
def get_next_positions(current: Coordinate, previous: Coordinate):
  coordinates = []
  x = current.get_x()
  y = current.get_y()

  if (x - 1 >= 0 and labyrinth[y][x - 1] != "1"):
    left = Coordinate(x - 1, y)
    if (left != current and left != previous):
      coordinates.append(left)
  if (y + 1 < len(labyrinth) and labyrinth[y + 1][x] != "1"):
    down = Coordinate(x, y + 1)
    if (down != current and down != previous):
      coordinates.append(down)
  if (x + 1 < len(labyrinth[y]) and labyrinth[y][x + 1] != "1"):
    right = Coordinate(x + 1, y)
    if (right != current and right != previous):
      coordinates.append(right)
  if (y - 1 >= 0 and labyrinth[y - 1][x] != "1"):
    up = Coordinate(x, y - 1)
    if (up != current and up != previous):
      coordinates.append(up)

  coordinates.sort(key=get_manhattan_distance)
  return coordinates

if __name__ == "__main__":
  tree_head = Tree(start)
  solution_found = False
  no_possible_moves = False
  road = []
  print("Labyrinth:")
  for row in labyrinth:
    print(row)
  print("\n\n")
  # The graph will be created at the same time as the algorithm is running
  iterations = 0
  current_node = tree_head  
  while not no_possible_moves and not solution_found:
    previous_position = current_node.previous.position if current_node.previous else Coordinate(-1, -1)
    next_positions = get_next_positions(current_node.position, previous_position)
    # Solution found
    if (current_node.position == end):
      solution_found = True
    # Theres no possible moves
    elif (len(next_positions) == 0):
      if (current_node.previous):
        current_node = current_node.previous
        if (len(road) > 0):
          road.pop()
      else:
        print("No solution found")
        no_possible_moves = True

    # Choosing the best move
    elif (not current_node.best and len(next_positions) > 0 and next_positions[0] not in road):
        best_coordinate = next_positions[0]
        best_node = Tree(best_coordinate)
        best_node.previous = current_node
        current_node.best = best_node
        current_node = best_node
        road.append(Road(best_coordinate, "best"))
    
    # Choosing the middle move
    elif (not current_node.middle and len(next_positions) > 1 and next_positions[1] not in road):
        middle_coordinate = next_positions[1]
        middle_node = Tree(middle_coordinate)
        middle_node.previous = current_node
        current_node.middle = middle_node
        current_node = middle_node
        road.append(Road(middle_coordinate, "middle"))
    
    # Choosing the worst move
    elif (not current_node.worst and len(next_positions) > 2 and next_positions[2] not in road):
        worst_coordinate = next_positions[2]
        worst_node = Tree(worst_coordinate)
        worst_node.previous = current_node
        current_node.worst = worst_node
        current_node = worst_node
        road.append(Road(worst_coordinate, "worst"))

    # Going backwards
    elif (current_node.previous):
      road.pop()
      current_node = current_node.previous
    else:
      no_possible_moves = True
    iterations += 1
  
  for step in road:
    labyrinth[step.position.y][step.position.x] = " "
    
  if (len(road) > 0):
    print("Solved labyrinth:")
    for row in labyrinth:
      print(row)
  else:
    print("No solution found")
  print("Iterations: " + str(iterations))