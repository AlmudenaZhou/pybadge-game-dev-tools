import board
import digitalio
import audioio
import audiocore  # <-- La versión 10 requiere importar audiocore para las muestras
import array
import math
import time

# 1. Activar el amplificador del altavoz integrado
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

# 2. Generar una onda sinusoidal pura de 440Hz en la memoria RAM
FRECUENCIA_MUESTREO = 8000
FRECUENCIA_TONO = 440
LONGITUD_ONDA = FRECUENCIA_MUESTREO // FRECUENCIA_TONO
# Crear el buffer de audio (valores de 16 bits sin signo)
datos_onda = array.array("H", [0] * LONGITUD_ONDA)

for i in range(LONGITUD_ONDA):
    # Calcula los puntos de la curva senoidal
    seno = math.sin(math.pi * 2 * i / LONGITUD_ONDA)
    # Escala el valor para el DAC de 16 bits (0 a 65535) con volumen moderado
    datos_onda[i] = int((seno + 1.0) * 8000 + 32768)

# Convertir los datos crudos usando audiocore en la Versión 10
tono_puro = audiocore.RawSample(datos_onda, sample_rate=FRECUENCIA_MUESTREO)

# 3. Configurar la salida de hardware y reproducir
audio = audioio.AudioOut(board.SPEAKER)

print("¡Probando altavoz en v10! Reproduciendo tono...")
audio.play(tono_puro, loop=True)  # 'loop=True' hace que suene continuo

time.sleep(2.0)  # Suena durante 2 segundos

audio.stop()
print("Prueba finalizada.")
