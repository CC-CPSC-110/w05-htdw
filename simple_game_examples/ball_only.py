import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        pass
    screen.fill("blue")
    pygame.draw.circle(screen, "red", (100, 100), 100) 
    pygame.display.flip()
    clock.tick(60)