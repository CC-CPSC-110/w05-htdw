import pygame
from ball import Ball
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

my_ball = Ball(100, 100, 20)

balls = []
for i in range(0, 100):
    x = random.randint(0, screen.get_width())
    y = random.randint(0, screen.get_height())
    balls.append(Ball(x, y, 10))

while True:
    for event in pygame.event.get():
        pass
    screen.fill("blue")
    pygame.draw.circle(screen, "red", (my_ball.x, my_ball.y), my_ball.size)
    
    #    my_ball.move(1, 1)
    pos = pygame.mouse.get_pos()
    my_ball.move_to(pos)
    
    for b in balls:
        b.move(random.randint(-1,1), random.randint(-1,1))

    for b in balls:
        pygame.draw.circle(screen, "yellow", (b.x, b.y), b.size)
        
    
    pygame.display.flip()
    clock.tick(60)

