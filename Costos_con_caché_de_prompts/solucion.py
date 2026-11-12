
import sys
import json
from decimal import Decimal


def calcular_costo(datos):
    entrada = datos["input_tokens"]
    escritura = datos["cache_creation_input_tokens"]
    lectura = datos["cache_read_input_tokens"]
    salida = datos["output_tokens"]

    costo = (
        Decimal(entrada) * 3
        + Decimal(escritura) * Decimal("3.75")
        + Decimal(lectura) * Decimal("0.30")
        + Decimal(salida) * 15
    ) / 1000000

    sin_cache = (
        Decimal(entrada + escritura + lectura) * 3
        + Decimal(salida) * 15
    ) / 1000000

    return costo, sin_cache


total = Decimal(0)
total_sin_cache = Decimal(0)
aciertos = 0
solicitudes = 0

for linea in sys.stdin:
    linea = linea.strip()

    if not linea:
        continue

    datos = json.loads(linea)
    solicitudes += 1

    costo, sin_cache = calcular_costo(datos)

    total += costo
    total_sin_cache += sin_cache

    if datos["cache_read_input_tokens"] > 0:
        aciertos += 1

    print(f"solicitud {solicitudes}: ${costo:.6f}")

ahorro = total_sin_cache - total

print(f"total: ${total:.6f}")
print(f"sin_cache: ${total_sin_cache:.6f}")
print(f"ahorro: ${ahorro:.6f}")
print(f"aciertos_de_cache: {aciertos}/{solicitudes}")
