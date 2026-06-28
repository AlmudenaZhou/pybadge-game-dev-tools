# ---------------------------------------------------------------------------
# Hardware — cada plataforma lee inputs a su manera
# ---------------------------------------------------------------------------
from .base import BaseHardware
from core.input_state import InputState


class PyBadgeHardware(BaseHardware):
    # Mapeo entre nombre lógico y atributo de pybadger.button
    _BUTTON_ATTRS = {
        "A": "a",
        "B": "b",
        "UP": "up",
        "DOWN": "down",
        "LEFT": "left",
        "RIGHT": "right",
        "START": "start",
        "SELECT": "select",
    }

    def __init__(self):
        from adafruit_pybadger import pybadger

        self._hw = pybadger
        self._prev: dict[str, bool] = {name: False for name in self._BUTTON_ATTRS}

    def poll(self) -> InputState:
        b = self._hw.button
        current = {
            name: bool(getattr(b, attr)) for name, attr in self._BUTTON_ATTRS.items()
        }

        state = InputState()
        state.buttons = current
        state.buttons_pressed = {
            k for k, v in current.items() if v and not self._prev[k]
        }
        state.buttons_released = {
            k for k, v in self._prev.items() if v and not current[k]
        }

        self._prev = current
        return state
