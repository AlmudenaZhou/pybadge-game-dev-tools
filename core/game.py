# ---------------------------------------------------------------------------
# Game — lógica pura, sin display, sin hardware
# ---------------------------------------------------------------------------

from .input_state import InputState


class Game:
    def __init__(self):
        self.last_pressed: str = "Pulsa un botón"
        self.held_buttons: set[str] = set()

    def update(self, inp: InputState) -> None:
        """
        Actualiza el estado del juego a partir del input del frame actual.
        Llamar una vez por frame, antes de renderizar.
        """
        if inp.buttons_pressed:
            self.last_pressed = " + ".join(sorted(inp.buttons_pressed))

        # Ejemplo: registrar qué botones se mantienen pulsados
        self.held_buttons = {k for k, v in inp.buttons.items() if v}
