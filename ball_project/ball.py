from dataclasses import dataclass
from typing import Tuple
from typing_extensions import Self

@dataclass
class Ball:
    x: int
    y: int
    size: int
    
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
    
    def move_to(self, pos: Tuple[int, int]) -> Self:
        """
        Purpose: moves a Ball's position to pos
        """
        self.x = pos[0]
        self.y = pos[1]

