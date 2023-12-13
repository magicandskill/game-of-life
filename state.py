def get_initial_state(config):
  grid = []
  for i in range(0, len(config)):
    row = []
    for j in range(0, len(config[i])):
      cell = config[i][j] == '*'
      row.append(cell)
    grid.append(row)
  return grid
