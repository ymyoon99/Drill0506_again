from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def load_resources():  # 함수와 함수 사이에 두줄이 권장
    global TUK_ground, character
    global arrow

    arrow = load_image('hand_arrow.png')
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global running, cx, cy, frame
    global hx, hy
    global sx, sy
    global t
    global action

    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 3

    sx, sy = cx, cy # p1 : 시작점
    hx, hy = 50, 50
    # hx, hy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT) # p2 : 끝점.
    t = 0.00

def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(hx, hy)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)
    update_canvas()

def update_world():
    global frame  # 자동으로 global 추가
    global cx,cy
    global t
    global action

    frame = (frame + 1) % 8
    action = 1 if cx < hx else 0 # 파이썬에서 가능한 문법


    if t < 1.0: # t가 1이 넘으면 안됨
        cx = (1-t)*sx + t*hx  # cx는 시작x와 끝x를 1-t:t의 비율로 섞은 위치
        cy = (1-t)*sy + t*hy

        t += 0.001


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()

while running:
    render_world()
    update_world()
    handle_events()

close_canvas()
