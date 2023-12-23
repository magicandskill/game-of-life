from state import get_initial_state

with open('config.txt', 'r') as f:
  config = f.readlines()
  grid_state = get_initial_state(config)
