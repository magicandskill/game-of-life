import pygame
from state import get_initial_state

def draw_cell(cell, x, y):
  rect = pygame.Rect((x * 10, y * 10, 10, 10))
  if(cell):
    pygame.draw.rect(screen, 'green3', rect)
  else:
    pygame.draw.rect(screen, 'blue3', rect)

def draw_grid(grid):
  for i, row in enumerate(grid):
    for j, cell in enumerate(row):
      draw_cell(cell, j, i)

with open('config.txt', 'r') as f:
  config = f.readlines()
  grid_state = get_initial_state(config)
  
pygame.init()
screen = pygame.display.set_mode((500, 500))
is_running = True
clock = pygame.time.Clock()

while is_running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False

  draw_grid(grid_state)
  pygame.display.flip()
  clock.tick(10)

pygame.quit()
