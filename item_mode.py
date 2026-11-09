from pico2d import *
import game_framework
import game_world

img = None
selected_item = 1  # 0: 공 없음, 1: 작은공, 2: 큰공


def init():
    global img
    img = load_image('item_select.png')


def finish():
    global img
    del img


def handle_events():
    global selected_item
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_i:
                # 아이템 선택 취소: play_mode는 스택에 살아 있으므로 그대로 복귀
                game_framework.pop_mode()
            elif event.key in (SDLK_0, SDLK_1, SDLK_2):
                # 0/1/2 키로 아이템을 고르고 바로 게임 화면으로 복귀
                selected_item = event.key - SDLK_0
                game_framework.pop_mode()


def update():
    # 게임 로직을 진행하지 않는다. play_mode의 월드가 그대로 얼어 있다.
    pass


def render():
    clear_canvas()
    game_world.render()   # 멈춰 있는 게임 화면을 그대로 깔고
    img.draw(400, 300)    # 그 위에 아이템 선택 이미지를 겹쳐 보여준다
    update_canvas()
