import pygame
from state import get_initial_grid, compute_new_grid

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

with open('config.txt', 'r') as f:
  initial_state = get_initial_grid(f.readlines())

state = {
  'grid': initial_state
}

def bound_safe(num, bounds):
  if(num < bounds[0]):
    return bounds[0]
  elif(num > bounds[1]):
    return bounds[1]
  else:
    return num

def cell_rect(i, j):
  _i = bound_safe(i, (0, 49))
  _j = bound_safe(j, (0, 49))
  leftTop = (_j * 10, _i * 10)
  widthHeight = (10, 10)
  return pygame.Rect(leftTop, widthHeight)

def draw(gridState):
  for i, row in enumerate(gridState):
    for j, cell in enumerate(row):
      rect = cell_rect(i, j)
      if(cell):
        pygame.draw.rect(screen, "white", rect)
      else:
        pygame.draw.rect(screen, "black", rect)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

  state['grid'] = compute_new_grid(state['grid'])
  draw(state['grid'])

  pygame.display.flip()
  clock.tick(10)

pygame.quit()
