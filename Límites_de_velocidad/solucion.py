
import sys

solicitudes_disponibles = 3
tokens_disponibles = 100
tiempo_anterior = 0

for linea in sys.stdin:
    linea = linea.strip()

    if not linea:
        continue

    tipo, tiempo, nuevos, cache = linea.split()

    tiempo = int(tiempo)
    nuevos = int(nuevos)
    cache = int(cache)

    segundos = tiempo - tiempo_anterior

    solicitudes_disponibles = min(
        3, solicitudes_disponibles + segundos
    )

    tokens_disponibles = min(
        100, tokens_disponibles + segundos * 20
    )

    tiempo_anterior = tiempo

    if solicitudes_disponibles >= 1 and tokens_disponibles >= nuevos:
        print("ok")

        solicitudes_disponibles -= 1
        tokens_disponibles -= nuevos

    else:
        faltan_solicitudes = max(
            0, 1 - solicitudes_disponibles
        )

        faltan_tokens = max(
            0, nuevos - tokens_disponibles
        )

        espera_tokens = (faltan_tokens + 19) // 20

        espera = max(
            faltan_solicitudes,
            espera_tokens
        )

        print(f"429 retry-after={espera}")
