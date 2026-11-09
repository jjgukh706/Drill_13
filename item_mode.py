from pico2d import *
import game_framework
import game_world

img = None


def init():
    global img
    img = load_image('item_select.png')


def finish():
    global img
    del img


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            # 아이템 선택 취소: play_mode는 스택에 살아 있으므로 그대로 복귀
            game_framework.pop_mode()


def update():
    # 게임 로직을 진행하지 않는다. play_mode의 월드가 그대로 얼어 있다.
    pass


def render():
    clear_canvas()
    game_world.render()   # 멈춰 있는 게임 화면을 그대로 깔고
    update_canvas()
