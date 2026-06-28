# ---------------------------------------------------------------------------
# InputState — contrato de entrada, igual para todas las plataformas
# ---------------------------------------------------------------------------

class InputState:
    """
    Atributos:
        buttons (dict[str, bool]):  estado actual de cada botón (mantenido).
        buttons_pressed (set[str]): botones que acaban de pulsarse este frame.
        buttons_released (set[str]): botones que acaban de soltarse este frame.
    """

    BUTTON_NAMES = ("A", "B", "UP", "DOWN", "LEFT", "RIGHT", "START", "SELECT")

    def __init__(self):
        self.buttons: dict[str, bool] = {name: False for name in self.BUTTON_NAMES}
        self.buttons_pressed: set[str] = set()
        self.buttons_released: set[str] = set()

    def is_held(self, button: str) -> bool:
        """True mientras el botón esté presionado."""
        return self.buttons.get(button, False)

    def just_pressed(self, button: str) -> bool:
        """True solo en el primer frame en que se pulsa."""
        return button in self.buttons_pressed

    def just_released(self, button: str) -> bool:
        """True solo en el frame en que se suelta."""
        return button in self.buttons_released
