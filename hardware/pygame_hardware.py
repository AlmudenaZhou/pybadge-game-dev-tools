from core.input_state import InputState


class PygameHardware:
    def __init__(self):
        import pygame

        pygame.init()
        self._pygame = pygame
        self._state = InputState()
        self._prev = dict(self._state.buttons)
        self._keymap = {
            pygame.K_z: "A",
            pygame.K_x: "B",
            pygame.K_UP: "UP",
            pygame.K_DOWN: "DOWN",
            pygame.K_LEFT: "LEFT",
            pygame.K_RIGHT: "RIGHT",
            pygame.K_RETURN: "START",
            pygame.K_RSHIFT: "SELECT",
        }

    def poll(self) -> InputState:
        self._pygame.event.pump()
        keys = self._pygame.key.get_pressed()
        buttons = {name: bool(keys[k]) for k, name in self._keymap.items()}
        self._state.buttons_pressed = {
            k for k, v in buttons.items() if v and not self._prev.get(k, False)
        }
        self._prev = buttons
        self._state.buttons = buttons
        return self._state
