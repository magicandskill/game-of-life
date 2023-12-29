def get_initial_state(config):
  grid = []
  for i in range(0, 50):
    row = []
    for j in range(0, 50):
      cell = config[i][j] == '*'
      row.append(cell)
    grid.append(row)
  return grid

def compute_new_state(old_grid):
  grid = []
  for i in range(0, len(old_grid)):
    row = []
    for j in range(0, len(old_grid[i])):
      count = get_neighbor_count(old_grid, i, j)
      cell = count == 3 or count == 2 and old_grid[i][j]
      row.append(cell)
    grid.append(row)
  return grid

def get_neighbor_count(grid, i, j):
  return [
    is_live(grid, i-1, j),
    is_live(grid, i+1, j),
    is_live(grid, i, j-1),
    is_live(grid, i, j+1),
    is_live(grid, i-1, j-1),
    is_live(grid, i-1, j+1),
    is_live(grid, i+1, j-1),
    is_live(grid, i+1, j+1)
  ].count(True)

def is_live(grid, i, j):
  return is_within_bounds(i) and is_within_bounds(j) and grid[i][j]

def is_within_bounds(index):
  return index >= 0 and index <= 49
