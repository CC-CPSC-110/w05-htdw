import pygame
from typing_extensions import Self
from dataclasses import dataclass
from cs110 import expect, summarize

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

@dataclass
class Ball:
    x: int
    y: int
    
    def move(self, x: int, y: int) -> Self:
        """
        Purpose: moves a Ball's position by x and y
        Example:
            ball.x -> ball.x + x
            ball.y -> ball.x + y
        """
        self.x = self.x + x
        self.y = self.y + y
        return self

ball = Ball(100, 100)
expect(ball.move(1, 1), Ball(101, 101))
summarize()


while True:
    for event in pygame.event.get():
        pass
    screen.fill("blue")
    pygame.draw.circle(screen, "red", (ball.x, ball.y), 100)
    ball.move(1, 1)
    pygame.display.flip()
    clock.tick(60)
