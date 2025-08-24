from pyray import (
    Rectangle,
    Color
)

class Entity:
    position: dict[str, float]
    speed: float
    can_jump: bool

    def __init__(self, position: dict[str, float], speed: float, can_jump: bool):
        self.position = position
        self.speed = speed
        self.can_jump = can_jump

class Map:
    rect: Rectangle
    blocking: int
    color: Color

    def __init__(self, rect: Rectangle, blocking: int, color: Color):
        self.rect = rect
        self.blocking = blocking
        self.color = color