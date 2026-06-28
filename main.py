import time


# ---------------------------------------------------------------------------
# 1. InputState — contrato de entrada, igual para todas las plataformas
# ---------------------------------------------------------------------------
class InputState:
    def __init__(self):
        self.buttons = {
            "A": False, "B": False,
            "UP": False, "DOWN": False,
            "LEFT": False, "RIGHT": False,
            "START": False, "SELECT": False,
        }
        self.buttons_pressed = set()


# ---------------------------------------------------------------------------
# 2. Game — lógica pura, sin display, sin hardware
# ---------------------------------------------------------------------------
class Game:
    def __init__(self):
        self.last_pressed = "Press a button"

    def update(self, inp):
        if inp.buttons_pressed:
            self.last_pressed = " + ".join(sorted(inp.buttons_pressed))


# ---------------------------------------------------------------------------
# 3. Hardware — cada plataforma lee inputs a su manera
# ---------------------------------------------------------------------------
class PyBadgeHardware:
    def __init__(self):
        from adafruit_pybadger import pybadger
        self._hw = pybadger
        self._state = InputState()
        self._prev = dict(self._state.buttons)

    def poll(self):
        b = self._hw.button_values
        buttons = {
            "A": b.a, "B": b.b,
            "UP": b.up, "DOWN": b.down,
            "LEFT": b.left, "RIGHT": b.right,
            "START": b.start, "SELECT": b.select,
        }
        self._state.buttons_pressed = {
            k for k, v in buttons.items() if v and not self._prev.get(k, False)
        }
        self._prev = buttons
        self._state.buttons = buttons
        return self._state


class PygameHardware:
    def __init__(self):
        import pygame
        pygame.init()
        self._pygame = pygame
        self._state = InputState()
        self._prev = dict(self._state.buttons)
        self._keymap = {
            pygame.K_z: "A", pygame.K_x: "B",
            pygame.K_UP: "UP", pygame.K_DOWN: "DOWN",
            pygame.K_LEFT: "LEFT", pygame.K_RIGHT: "RIGHT",
            pygame.K_RETURN: "START", pygame.K_RSHIFT: "SELECT",
        }

    def poll(self):
        self._pygame.event.pump()
        keys = self._pygame.key.get_pressed()
        buttons = {name: bool(keys[k]) for k, name in self._keymap.items()}
        self._state.buttons_pressed = {
            k for k, v in buttons.items() if v and not self._prev.get(k, False)
        }
        self._prev = buttons
        self._state.buttons = buttons
        return self._state


# ---------------------------------------------------------------------------
# 4. Renderer — cada plataforma dibuja a su manera
# ---------------------------------------------------------------------------
class DisplayIORenderer:
    def __init__(self):
        import displayio, terminalio
        from adafruit_display_text import label
        from adafruit_pybadger import pybadger

        display = pybadger.display
        bg = displayio.Bitmap(display.width, display.height, 1)
        palette = displayio.Palette(1)
        palette[0] = 0x000000

        self._label = label.Label(
            terminalio.FONT, text="", color=0xFFFFFF, scale=2
        )
        self._label.anchor_point = (0.5, 0.5)
        self._label.anchored_position = (display.width // 2, display.height // 2)

        group = displayio.Group()
        group.append(displayio.TileGrid(bg, pixel_shader=palette))
        group.append(self._label)
        display.root_group = group

    def render(self, game):
        self._label.text = game.last_pressed


class PygameRenderer:
    WIDTH, HEIGHT = 160, 128

    def __init__(self):
        import pygame
        self._pygame = pygame
        self._screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self._font = pygame.font.SysFont(None, 24)

    def render(self, game):
        self._screen.fill((0, 0, 0))
        text = self._font.render(game.last_pressed, True, (255, 255, 255))
        rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self._screen.blit(text, rect)
        self._pygame.display.flip()


# ---------------------------------------------------------------------------
# 5. Loop principal — cambia hw + renderer para cambiar de plataforma
# ---------------------------------------------------------------------------
# hw       = PyBadgeHardware()
# renderer = DisplayIORenderer()
hw       = PygameHardware()
renderer = PygameRenderer()

game = Game()

while True:
    inp = hw.poll()
    game.update(inp)
    renderer.render(game)
    time.sleep(0.016)
