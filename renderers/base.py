from games import Game


class BaseRenderer:
    def render(self, game: Game) -> None:
        """Dibuja el estado actual del juego. Llamar una vez por frame."""
        raise NotImplementedError
