
import sys
import json


def ejecutar_herramienta(nombre, datos):
    if nombre == "calculadora":
        operacion = datos["operacion"]
        a = datos["a"]
        b = datos["b"]

        if operacion == "sumar":
            return str(a + b)
        elif operacion == "restar":
            return str(a - b)
        elif operacion == "multiplicar":
            return str(a * b)
        elif operacion == "dividir":
            if b == 0:
                return "error: división por cero"
            return str(int(a / b))
        else:
            return f"error: operación desconocida: {operacion}"

    elif nombre == "clima":
        temperaturas = {
            "Bogotá": 14,
            "Medellín": 24,
            "Cali": 26
        }

        ciudad = datos["ciudad"]

        if ciudad in temperaturas:
            return f"{temperaturas[ciudad]} °C"

        return f"error: ciudad desconocida: {ciudad}"

    return f"error: herramienta desconocida: {nombre}"


llamadas = 0
errores = 0

for linea in sys.stdin:
    linea = linea.strip()

    if not linea:
        continue

    respuesta = json.loads(linea)

    if respuesta["stop_reason"] == "tool_use":
        for bloque in respuesta["content"]:
            if bloque["type"] != "tool_use":
                continue

            resultado = ejecutar_herramienta(
                bloque["name"],
                bloque["input"]
            )

            print(f"tool_result {bloque['id']} {resultado}")

            llamadas += 1

            if resultado.startswith("error:"):
                errores += 1

    elif respuesta["stop_reason"] == "end_turn":
        texto = "".join(
            bloque["text"]
            for bloque in respuesta["content"]
            if bloque["type"] == "text"
        )

        print(f"final: {texto}")

print(f"resumen: {llamadas} llamadas, {errores} errores")
