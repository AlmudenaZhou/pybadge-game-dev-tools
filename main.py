import time
from games import DemoGame
from hardware import PyBadgeHardware, PygameHardware


# hw = PyBadgeHardware()
hw = PygameHardware()

game = DemoGame()

TARGET_FPS = 60
FRAME_TIME = 1 / TARGET_FPS

while True:
    frame_start = time.monotonic()

    inp = hw.poll()
    game.update(inp)
    hw.render(game)

    elapsed = time.monotonic() - frame_start
    remaining = FRAME_TIME - elapsed
    if remaining > 0:
        time.sleep(remaining)
