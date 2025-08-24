from pyray import *
import random as ran
from GameObjects import *
from GameLogic import *

init_window(800, 450, "Hello")
set_target_fps(60)
game = Game()


while not window_should_close():
    # Updates
    delta = get_frame_time()
    game.update(delta)

    # Drawing
    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world!", 190, 200, 20, VIOLET)
    game.draw()
    end_drawing()
    print(game.player.position, game.player.speed, game.player.can_jump)

close_window()