import pygame
from state import get_initial_state

pygame.init()
screen = pygame.display.set_mode((500, 500))
is_running = True
clock = pygame.time.Clock()

with open('config.txt', 'r') as f:
  state = get_initial_state(f.readlines())

while is_running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False

  rect = pygame.Rect((0, 0), (10, 10))
  pygame.draw.rect(screen, "green3", rect)
  
  pygame.display.flip()
  clock.tick(10)

pygame.quit()
