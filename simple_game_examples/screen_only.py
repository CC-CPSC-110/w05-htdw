import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
while True:
    for event in pygame.event.get():
        pass
    screen.fill("blue")
    pygame.display.flip()