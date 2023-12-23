import pygame
from state import get_initial_state

with open('config.txt', 'r') as f:
  config = f.readlines()
  grid_state = get_initial_state(config)
  
pygame.init()
screen = pygame.display.set_mode((500, 500))
is_running = True

while is_running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False
