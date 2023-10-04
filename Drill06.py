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
    global mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            points.append((event.x, TUK_HEIGHT - 1 - event.y))  # 클릭된 위치를 새로운 점으로 추가.
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global running, cx, cy, frame
    global t
    global action
    global mx, my
    global points

    mx, my = 0, 0

    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 3

    points = []
    set_new_target_arrow()


def set_new_target_arrow():
    global sx, sy, hx, hy, t
    global action
    global frame
    global target_exists

    if points:  # points 리스트 안에 남아있는 점이 있으면 True
        sx, sy = cx, cy  # p1 : 시작점
        hx, hy = points[0]  # 첫번째 요소를 가져옴
        t = 0.00
        action = 1 if sx < hx else 0  # 파이썬에서 가능한 문법
        frame = 0
        target_exists = True
    else:
        action = 3 if action == 1 else 2  # 이전에 소년의 이동방향에 따른 idle 방향 설정
        frame = 0
        target_exists = False


def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for p in points:
        arrow.draw(p[0], p[1])
    arrow.draw(mx, my)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)
    update_canvas()


def update_world():
    global frame  # 자동으로 global 추가
    global cx, cy
    global t

    frame = (frame + 1) % 8

    if target_exists:
        if t < 1.0:  # t가 1이 넘으면 안됨
            cx = (1 - t) * sx + t * hx  # cx는 시작x와 끝x를 1-t:t의 비율로 섞은 위치
            cy = (1 - t) * sy + t * hy
            t += 0.001
        else:  # 소년이 목표지점에 도달하면
            cx, cy = hx, hy  # 캐릭터와 목표의 위치를 강제로 정확하게 일치시킴.
            del points[0]  # 목표지점에 도달했기 때문에, 리스트의 첫번째 원소를 삭제함
            set_new_target_arrow()
    elif points:  # 목표 지점이 없는 상황에서, 새로운 폭표 지점이 생기면 이동
        set_new_target_arrow()


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()

while running:
    render_world()
    update_world()
    handle_events()

close_canvas()
