# PyBadge Game — Estructura del proyecto

```
CIRCUITPY/
│
├── code.py                        # Punto de entrada (main.py renombrado)
│
├── core/                          # Compartido por todas las capas
│   ├── __init__.py
│   └── input_state.py             # Contrato de entrada (InputState)
│
├── games/                         # Lógica pura — sin display, sin hardware
│   ├── __init__.py
│   ├── base.py                    # Interfaz abstracta (Game)
│   └── demo.py                    # Juego de demostración (DemoGame)
│
├── hardware/                      # Lectura de botones
│   ├── __init__.py
│   ├── base.py                    # Interfaz abstracta (BaseHardware)
│   ├── pybadge.py                 # Hardware real (adafruit_pybadger)
│   └── pygame_hardware.py         # Simulador de escritorio (pygame)
│
├── renderers/                     # Dibujado en pantalla
│   ├── __init__.py
│   ├── base.py                    # Interfaz abstracta (BaseRenderer)
│   ├── displayio_renderer.py      # Pantalla PyBadge (displayio)
│   └── pygame_renderer.py         # Ventana escritorio (pygame)
│
└── lib/                           # Librerías de Adafruit (ya en el dispositivo)
    ├── adafruit_pybadger/
    └── adafruit_display_text/
```

## Flujo de datos por frame

```
hw.poll() → InputState → game.update() → Game → renderer.render()
```

## InputState — helpers disponibles

```python
inp.just_pressed("A")    # True solo en el primer frame en que se pulsa
inp.is_held("UP")        # True mientras el botón esté presionado
inp.just_released("B")   # True solo en el frame en que se suelta
```

## Añadir un juego nuevo

1. Crea `games/mi_juego.py` con una clase que extienda `Game` e implemente `update()`.
2. Actívalo en `main.py`.

```python
# games/mi_juego.py
from core.input_state import InputState
from .base import Game

class MiJuego(Game):
    def update(self, inp: InputState) -> None:
        if inp.just_pressed("A"):
            pass  # tu lógica aquí
```

La lógica en `games/` nunca importa nada de `hardware/` ni de `renderers/`.

## Desplegar en PyBadge

1. Copia las carpetas `core/`, `games/`, `hardware/` y `renderers/` a `CIRCUITPY/`.
2. Copia `main.py` a `CIRCUITPY/` y renómbralo `code.py`.
3. En `code.py` activa el hardware y renderer de PyBadge (no el de pygame).
4. La consola se reiniciará automáticamente al detectar `code.py`.

Puedes usar **Thonny** o arrastrar y soltar desde el explorador de archivos
si el PyBadge aparece como unidad USB.
