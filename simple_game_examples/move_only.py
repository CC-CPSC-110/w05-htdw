import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pos = (100, 100)
while True:
    for event in pygame.event.get():
        pass
    screen.fill("blue")
    pygame.draw.circle(screen, "red", pos, 100)
    pos = (pos[0] + 1, pos[1])
    pygame.display.flip()
    clock.tick(60)
