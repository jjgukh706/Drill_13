from pico2d import *
import game_framework

img = None

logo_start_time = 0.0


def init():
    global img
    global logo_start_time
    img = load_image('tuk_credit.png')
    running = True
    logo_start_time = get_time()


def finish():
    global img
    del img

def update():
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        game_framework.quit()


def handle_events():
    events = get_events()

def render():
    clear_canvas()
    img.draw(400,300)
    update_canvas()


