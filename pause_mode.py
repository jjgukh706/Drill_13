from pico2d import *
import game_framework
import game_world

img = None


def init():
    global img
    img = load_image('pause.png')


def finish():
    global img
    del img


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            # 일시정지 해제: 이 모드를 닫고 아래에 살아 있던 play_mode로 복귀
            game_framework.pop_mode()


def update():
    # 게임 로직을 진행하지 않는다. play_mode의 월드가 그대로 얼어 있다.
    pass


def render():
    clear_canvas()
    game_world.render()   # 멈춰 있는 게임 화면을 그대로 깔고
    img.draw(400, 300)    # 그 위에 pause 이미지를 겹쳐 보여준다
    update_canvas()
