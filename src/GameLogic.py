from pyray import *
from GameObjects import *
import random as ran
from raylib import (
    KEY_RIGHT,
    KEY_LEFT,
    KEY_UP,
)


class Player:
    def __init__(self, position, speed, radius, can_jump, player_hor_spd=200.0, player_gravity=300.0):
        self.position = position
        self.radius = radius
        self.speed = speed
        self.can_jump = can_jump
        self.rect = Rectangle(position["x"] - radius, position["y"] - radius, radius * 2, radius * 2)
        self.player_hor_spd = player_hor_spd
        self.player_gravity = player_gravity

    def update(self, map, delta):
        original_x, original_y = self.position["x"], self.position["y"]
        if is_key_down(KEY_RIGHT):
            self.position["x"] += self.player_hor_spd * delta
            if self.check_bounds(map):
                self.position["x"] = original_x
        elif is_key_down(KEY_LEFT):
            self.position["x"] -= self.player_hor_spd * delta
        if self.check_bounds(map):
            self.position["x"] = original_x
        elif is_key_down(KEY_UP) and self.can_jump:
            self.speed = -350
            self.can_jump = False

        # Apply gravity
        self.position["y"] += self.speed * delta
        self.speed += self.player_gravity * delta
        is_grounded = self.check_grounded(map)

        if is_grounded:
            self.position["y"] = original_y
            self.speed = 0
            self.can_jump = True

    def check_grounded(self, map):
        self.rect = Rectangle(self.position["x"] - self.radius, self.position["y"] - self.radius, self.radius * 2, self.radius * 2)
        for m in map:
            if m.blocking == 1 and check_collision_recs(m.rect, self.rect):
                return True
        return False

    def check_bounds(self, map):
        self.rect = Rectangle(self.position["x"] - self.radius, self.position["y"] - self.radius, self.radius * 2, self.radius * 2)
        for m in map:
            if m.blocking == 2 and check_collision_recs(m.rect, self.rect):
                return True
        return False
    
    def draw(self):
        draw_circle(int(self.position["x"]), int(self.position["y"]), self.radius, RED)
        draw_rectangle_rec(self.rect, BLUE)
    
class Game:
    def __init__(self):
        self.player = Player({"x": 100, "y": 100}, 0, 20, True)
        self.map = (
            Map(Rectangle(0, get_screen_height()-50, get_screen_width(), 50), 1, BLUE),
            Map(Rectangle(0, 100, 0, 100), 2, BLUE),
            Map(Rectangle(get_screen_width()-50, 0, 50, get_screen_height()), 2, BLUE),
            Map(Rectangle(0, 0, 50, get_screen_height()), 2, BLUE)
        )

    def update(self, delta):
        self.player.update(self.map, delta)

    def draw(self):
            self.player.draw()
            for m in self.map:
                draw_rectangle_rec(m.rect, m.color)