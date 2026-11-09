from pico2d import *
import game_framework
import game_world
import title_mode
from boy import Boy
from grass import Grass

boy = None


def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            boy.handle_event(event)


def init():
    global boy

    game_world.clear()

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


def finish():
    game_world.clear()


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()
