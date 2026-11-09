from pico2d import *
import game_framework
import play_mode

img = None


def init():
    global img
    img = load_image('title.png')


def finish():
    global img
    del img


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_SPACE:
                game_framework.change_mode(play_mode)


def update():
    pass


def render():
    clear_canvas()
    img.draw(400, 300)
    update_canvas()
