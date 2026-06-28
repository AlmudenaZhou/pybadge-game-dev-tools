# ---------------------------------------------------------------------------
# Game — lógica pura, sin display, sin hardware
# ---------------------------------------------------------------------------

from core.input_state import InputState
from .base import Game


class DemoGame(Game):

    RESET_COMBO = {"SELECT", "B"}

    def __init__(self):
        self.last_pressed: str = "Pulsa un botón"
        self.held_buttons: set[str] = set()

    def reset(self) -> None:
        self.last_pressed = "Pulsa un botón"
        self.held_buttons = set()

    def update(self, inp: InputState) -> None:
        """
        Actualiza el estado del juego a partir del input del frame actual.
        Llamar una vez por frame, antes de renderizar.
        """
        if inp.buttons_pressed:
            self.last_pressed = " + ".join(sorted(inp.buttons_pressed))

        if self.RESET_COMBO.issubset(self.held_buttons):
            self.reset()
            return
        # Ejemplo: registrar qué botones se mantienen pulsados
        self.held_buttons = {k for k, v in inp.buttons.items() if v}
