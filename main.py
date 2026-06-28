import time
from core import Game
from hardware import PyBadgeHardware, PygameHardware
from renderers import DisplayIORenderer, PygameRenderer


hardware = "pygame"

if hardware == "pybadge":
    hw = PyBadgeHardware()
    renderer = DisplayIORenderer()
elif hardware == "pygame":
    hw = PygameHardware()
    renderer = PygameRenderer()

game = Game()

TARGET_FPS = 60
FRAME_TIME = 1 / TARGET_FPS

while True:
    frame_start = time.monotonic()

    inp = hw.poll()
    game.update(inp)
    renderer.render(game)

    elapsed = time.monotonic() - frame_start
    remaining = FRAME_TIME - elapsed
    if remaining > 0:
        time.sleep(remaining)
