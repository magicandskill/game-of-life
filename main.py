import pygame
from state import get_initial_state, compute_new_state

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
is_running = True

with open('config.txt', 'r') as f:
  state = get_initial_state(f.readlines())

def draw_grid(grid):
  for i, row in enumerate(grid):
    for j, cell in enumerate(row):
      draw_cell(cell, i, j)

def draw_cell(cell, i, j):
  leftTop = (j * 10, i * 10)
  widthHeight = (10, 10)
  rect = pygame.Rect(leftTop, widthHeight)
  if(cell):
    pygame.draw.rect(screen, "green3", rect)
  else:
    pygame.draw.rect(screen, "blue3", rect)

while is_running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False

  state = compute_new_state(state)
  draw_grid(state)
  
  pygame.display.flip()
  clock.tick(10)

pygame.quit()
