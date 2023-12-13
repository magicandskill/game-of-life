def get_initial_state(config):
  out = []
  for row_config in config:
    row_state = []
    for cell_config in list(row_config):
      if(cell_config == '*'):
        row_state.append(True)
      else:
        row_state.append(False)
    out.append(row_state)
  return out

def compute_new_state(curr_grid):
  new_grid = []
  for i, curr_row in enumerate(curr_grid):
    new_row = []
    for j, curr_cell in enumerate(curr_row):
      count = get_neighbor_count(curr_grid, i, j)
      new_cell = count == 3 or count == 2 and curr_cell
      new_row.append(new_cell)
    new_grid.append(new_row)
  return new_grid

def is_in_bound(i):
  return i >= 0 and i <= 49

def has_neighbor(grid, i, j):
  return is_in_bound(i) and is_in_bound(j) and grid[i][j]

def get_neighbor_count(grid, i, j):
  count = 0
  if(has_neighbor(grid, i-1, j)): 
    count+=1
  if(has_neighbor(grid, i+1, j)): 
    count+=1
  if(has_neighbor(grid, i, j-1)): 
    count+=1
  if(has_neighbor(grid, i, j+1)): 
    count+=1
  if(has_neighbor(grid, i-1, j-1)): 
    count+=1
  if(has_neighbor(grid, i-1, j+1)): 
    count+=1
  if(has_neighbor(grid, i+1, j-1)): 
    count+=1
  if(has_neighbor(grid, i+1, j+1)): 
    count+=1
  return count
