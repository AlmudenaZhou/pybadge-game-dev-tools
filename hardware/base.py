from core.input_state import InputState


class BaseHardware:
    def poll(self) -> InputState:
        """
        Lee el estado actual de los botones y devuelve un InputState.
        Debe llamarse exactamente una vez al inicio de cada frame.
        """
        raise NotImplementedError
