
import sys
import json

bloques = {}
input_tokens = 0
output_tokens = 0
stop_reason = ""

for linea in sys.stdin:
    linea = linea.strip()

    if not linea.startswith("data: "):
        continue

    evento = json.loads(linea[6:])
    tipo = evento["type"]

    if tipo == "message_start":
        bloques = {}
        input_tokens = evento["message"]["usage"]["input_tokens"]
        output_tokens = 0
        stop_reason = ""

    elif tipo == "content_block_start":
        indice = evento["index"]
        bloques[indice] = evento["content_block"].get("text", "")

    elif tipo == "content_block_delta":
        if evento["delta"]["type"] == "text_delta":
            indice = evento["index"]
            bloques[indice] += evento["delta"]["text"]

    elif tipo == "message_delta":
        stop_reason = evento["delta"]["stop_reason"]
        output_tokens = evento["usage"]["output_tokens"]

    elif tipo == "message_stop":
        texto = "".join(bloques[i] for i in sorted(bloques))

        print(f"texto: {texto}")
        print(f"stop_reason: {stop_reason}")
        print(f"input_tokens: {input_tokens}")
        print(f"output_tokens: {output_tokens}")
