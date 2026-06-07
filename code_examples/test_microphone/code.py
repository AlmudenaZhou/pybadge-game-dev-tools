import time
import board
import analogio

# Configuración del pin analógico D2
mic = analogio.AnalogIn(board.D2)

# UMBRAL DE RUIDO: El ruido flotante rara vez supera los 5000.
# Una palmada fuerte o hablar cerca del MAX4466 superará los 15000.
UMBRAL_SONIDO = 10000

print("=== SISTEMA DE DIAGNÓSTICO DEL MICRÓFONO INICIADO ===")
print(f"Filtro activo: Ignorando variaciones menores a {UMBRAL_SONIDO}")
print("Esperando señal real...\n")

ultimo_mensaje_silencio = 0

while True:
    valor_min = 65535
    valor_max = 0

    # Captura rápida de la onda durante 50 milisegundos
    tiempo_inicio = time.monotonic()
    while time.monotonic() - tiempo_inicio < 0.05:
        lectura = mic.value
        if lectura > valor_max:
            valor_max = lectura
        if lectura < valor_min:
            valor_min = lectura

    # Calcular la amplitud real detectada
    amplitud = valor_max - valor_min

    # CASO 1: El sonido supera el umbral
    if amplitud > UMBRAL_SONIDO:
        print(f"[SONIDO DETECTADO] -> Amplitud: {amplitud} (¡Acción ejecutada!)")
        time.sleep(0.2)  # Pausa breve para evitar repetir el mensaje instantáneamente

    # CASO 2: Silencio o ruido fantasma del pin flotante (Se ignora)
    else:
        # Imprime un recordatorio cada 3 segundos para ver que el código funciona
        if time.monotonic() - ultimo_mensaje_silencio > 3.0:
            print(f"[Estado: Silencio] El pin flota en {amplitud}. Esperando micrófono...")
            ultimo_mensaje_silencio = time.monotonic()
