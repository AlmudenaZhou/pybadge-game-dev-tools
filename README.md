# PyBadge Game — Estructura del proyecto

```
CIRCUITPY/
│
├── code.py                        # Punto de entrada (main.py renombrado)
│
├── core/                          # Lógica pura — sin imports de hardware
│   ├── __init__.py
│   ├── input_state.py             # Contrato de entrada (InputState)
│   └── game.py                    # Lógica del juego (Game)
│
├── hardware/                      
│   ├── __init__.py
│   ├── base.py                    # Interfaz abstracta (BaseHardware)
│   └── pybadge.py                 # Lectura de botones (adafruit_pybadger)
│
├── renderers/                     
│   ├── __init__.py
│   ├── base.py                    # Interfaz abstracta (BaseRenderer)
│   └── displayio_renderer.py      # Pantalla PyBadge (displayio)
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

## Desplegar en PyBadge

1. Copia las carpetas `core/`, `hardware/` y `renderers/` a `CIRCUITPY/`.
2. Copia `main.py` a `CIRCUITPY/` y renómbralo `code.py`.
3. La consola se reiniciará automáticamente al detectar `code.py`.

Puedes usar **Thonny** o arrastrar y soltar desde el explorador de archivos
si el PyBadge aparece como unidad USB.

## Añadir lógica al juego

Todo el código del juego va en `core/game.py`. El método `update()` recibe
un `InputState` cada frame:

```python
def update(self, inp):
    if inp.just_pressed("A"):
        # acción única al pulsar A
        pass

    if inp.is_held("UP"):
        # mover personaje mientras se mantiene arriba
        pass
```

`core/` nunca importa nada de `hardware/` ni de `renderers/`.
