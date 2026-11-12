
import sys
import json
import re
import unicodedata


def normalizar(texto):
    texto = texto.lower()

    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    texto = re.sub(r"[^a-z0-9]+", " ", texto)

    return " ".join(texto.split())


categorias = {}
total_aprobadas = 0
total_preguntas = 0

for linea in sys.stdin:
    linea = linea.strip()

    if not linea:
        continue

    datos = json.loads(linea)

    categoria = datos["categoria"]
    esperado = normalizar(datos["esperado"])
    respuesta = normalizar(datos["respuesta"])

    aprobado = (
        f" {esperado} " in f" {respuesta} "
    )

    if categoria not in categorias:
        categorias[categoria] = [0, 0]

    categorias[categoria][1] += 1
    total_preguntas += 1

    if aprobado:
        categorias[categoria][0] += 1
        total_aprobadas += 1

for categoria in sorted(categorias):
    aprobadas, total = categorias[categoria]
    print(f"{categoria}: {aprobadas}/{total}")

porcentaje = total_aprobadas / total_preguntas * 100

print(
    f"total: {total_aprobadas}/{total_preguntas} "
    f"({porcentaje:.1f}%)"
)
