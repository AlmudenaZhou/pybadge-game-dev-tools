from core.input_state import InputState
from renderers.base import BaseRenderer


class BaseHardware:
    renderer: BaseRenderer = None

    def poll(self) -> InputState:
        raise NotImplementedError

    def render(self, game) -> None:
        self.renderer.render(game)
