# ---------------------------------------------------------------------------
# Renderer — cada plataforma dibuja a su manera
# ---------------------------------------------------------------------------
from .base import BaseRenderer
from core.game import Game


class DisplayIORenderer(BaseRenderer):

    def __init__(self):
        import displayio
        import terminalio
        from adafruit_display_text import label
        from adafruit_pybadger import pybadger

        display = pybadger.display

        # Fondo negro
        bg      = displayio.Bitmap(display.width, display.height, 1)
        palette = displayio.Palette(1)
        palette[0] = 0x000000

        # Etiqueta centrada
        self._label = label.Label(
            terminalio.FONT,
            text="",
            color=0xFFFFFF,
            scale=2,
        )
        self._label.anchor_point      = (0.5, 0.5)
        self._label.anchored_position = (display.width // 2, display.height // 2)

        group = displayio.Group()
        group.append(displayio.TileGrid(bg, pixel_shader=palette))
        group.append(self._label)
        display.root_group = group

    def render(self, game: Game) -> None:
        self._label.text = game.last_pressed
