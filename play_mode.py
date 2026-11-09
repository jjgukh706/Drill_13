from pico2d import *
import game_framework
import game_world
import title_mode
import pause_mode
from boy import Boy
from grass import Grass

boy = None
paused_at = 0.0


def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            # 일시정지: play_mode는 스택에 그대로 남겨 두고 pause_mode를 위에 올린다.
            game_framework.push_mode(pause_mode)
        else:
            boy.handle_event(event)


def init():
    global boy, paused_at

    paused_at = 0.0
    game_world.clear()

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


def finish():
    game_world.clear()


def pause():
    global paused_at
    paused_at = get_time()


def resume():
    global paused_at
    # 일시정지 동안 흐른 실제 시간만큼 IDLE 타이머를 밀어,
    # 복귀 직후 갑자기 잠드는 일 없이 멈추기 전 상태를 이어 간다.
    if boy is not None and paused_at > 0.0:
        boy.idle_started_at += get_time() - paused_at
    paused_at = 0.0


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()
