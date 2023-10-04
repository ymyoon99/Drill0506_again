from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def load_resources():  # 함수와 함수 사이에 두줄이 권장
    global TUK_ground, character
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
    global running, x, y, frame
    running = True
    x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0


def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()


def update_world():
    global frame  # 자동으로 global 추가
    frame = (frame + 1) % 8


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()

while running:
    render_world()
    update_world()
    handle_events()

close_canvas()
