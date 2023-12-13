def get_initial_state(config):
  grid = []
  for i in range(0, len(config)):
    row = []
    for j in range(0, len(config[i])):
      cell = config[i][j] == '*'
      row.append(cell)
    grid.append(row)
  return grid

def compute_new_state(curr_grid):
  grid = []
  for i in range(0, len(curr_grid)):
    row = []
    for j in range(0, len(curr_grid[i])):
      count = get_neighbor_count(curr_grid, i, j)
      cell = count == 3 or count == 2 and curr_grid[i][j]
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
  return is_in_bound(i) and is_in_bound(j) and grid[i][j]

def is_in_bound(index):
  return index >= 0 and index <= 49
