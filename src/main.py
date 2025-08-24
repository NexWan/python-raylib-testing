from pyray import *
from typing import TypedDict

from GameObjects import *
from raylib import (
    KEY_RIGHT,
    KEY_LEFT,
    KEY_UP,
    KEY_DOWN
)

init_window(800, 450, "Hello")
set_target_fps(60)
player_gravity = 300
player_hor_spd = 200.0
player = Entity({"x": 100, "y": 100}, 5, False)
map = (
    Map(Rectangle(0, get_screen_height()-50, get_screen_width(), 50), 1, BLUE),
    Map(Rectangle(0, 100, 0, 100), 2, BLUE),
    Map(Rectangle(get_screen_width()-50, 0, 50, get_screen_height()), 2, BLUE),
    Map(Rectangle(0, 0, 50, get_screen_height()), 2, BLUE)
)

def check_grounded(player: Entity, map: tuple[Map]):
    player.rect = Rectangle(player.position["x"] - 20, player.position["y"] - 20, 40, 40)
    for m in map:
        if m.blocking == 1 and check_collision_recs(m.rect, player.rect):
            return True
    return False

def check_bounds(player: Entity, map: tuple[Map]):
    player.rect = Rectangle(player.position["x"] - 20, player.position["y"] - 20, 40, 40)
    for m in map:
        if m.blocking == 2 and check_collision_recs(m.rect, player.rect):
            return True
    return False

def update_player(player: Entity, map: tuple[Map], delta:float):
    original_x, original_y = player.position["x"], player.position["y"]
    if is_key_down(KEY_RIGHT):
        player.position["x"] += player_hor_spd * delta
        if check_bounds(player, map):
            player.position["x"] = original_x
    elif is_key_down(KEY_LEFT):
        player.position["x"] -= player_hor_spd * delta
        if check_bounds(player, map):
            player.position["x"] = original_x
    elif is_key_down(KEY_UP) and player.can_jump:
        player.speed = -350
        player.can_jump = False

    # Apply gravity
    player.position["y"] += player.speed * delta
    player.speed += player_gravity * delta
    is_grounded = check_grounded(player, map)

    if is_grounded:
        player.position["y"] = original_y
        player.speed = 0
        player.can_jump = True

while not window_should_close():
    # Updates
    delta = get_frame_time()
    update_player(player, map, delta)

    # Drawing
    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world!", 190, 200, 20, VIOLET)
    # Draw player
    draw_circle(int(player.position["x"]), int(player.position["y"]), 20, RED)
    # Player hitbox (draw_rectangle_rec)
    draw_rectangle_rec(player.rect, BLUE)
    # Draw map
    for m in map:
        draw_rectangle_rec(m.rect, m.color)
    end_drawing()
    print(player.position, player.speed, player.can_jump)

close_window()