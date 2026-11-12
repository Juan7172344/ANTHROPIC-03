# ANTHROPIC-03

## Descripción

Este repositorio contiene la solución de cinco ejercicios de programación desarrollados en Python, enfocados en el procesamiento de respuestas de modelos de inteligencia artificial, uso de herramientas, cálculo de costos, límites de velocidad y evaluación de respuestas.

Cada ejercicio cuenta con su propio código fuente, archivo de entrada y archivo de salida.

## Tecnologías utilizadas

- Python 3
- JSON
- Visual Studio Code
- Git y GitHub

No se requieren librerías externas.

## Ejercicios desarrollados

### A. Respuesta en streaming

Procesa eventos de una respuesta transmitida por streaming.

El programa reconstruye el texto recibido y muestra la razón de finalización, los tokens de entrada y los tokens de salida.

### B. Uso de herramientas

Simula la ejecución de herramientas solicitadas por un modelo de inteligencia artificial.

Incluye una calculadora para operaciones matemáticas y una herramienta de consulta de temperaturas. También identifica herramientas desconocidas y contabiliza los errores.

### C. Costos con caché de prompts

Calcula el costo de las solicitudes según los tokens utilizados.

Considera los tokens de entrada, salida, escritura y lectura de caché. Finalmente, muestra el costo total, el costo sin caché, el ahorro y los aciertos de caché.

### D. Límites de velocidad

Simula un sistema de control de solicitudes mediante límites de peticiones y tokens.

Determina si una solicitud puede procesarse o si debe rechazarse con un código `429`, indicando el tiempo de espera necesario.

### E. Evaluación de respuestas

Evalúa respuestas comparándolas con los resultados esperados.

Normaliza el texto para ignorar diferencias entre mayúsculas, minúsculas, tildes y signos de puntuación. Presenta los resultados por categoría y el porcentaje total de aprobación.

## Estructura del repositorio

```text
ANTHROPIC-03/
│
├── Streaming/
│   ├── solucion.py
│   ├── Entrada.txt
│   └── salida.txt
│
├── Uso_de_Herramientas/
│   ├── solucion.py
│   ├── Entrada.txt
│   └── salida.txt
│
├── Costos_Cache/
│   ├── solucion.py
│   ├── Entrada.txt
│   └── salida.txt
│
├── Limites_Velocidad/
│   ├── solucion.py
│   ├── Entrada.txt
│   └── salida.txt
│
├── Evaluacion_Respuestas/
│   ├── solucion.py
│   ├── Entrada.txt
│   └── salida.txt
│
└── README.md
```

## Ejecución

1. Clonar o descargar el repositorio.
2. Abrir el proyecto en Visual Studio Code.
3. Acceder desde la terminal a la carpeta del ejercicio que se desea ejecutar.
4. Ejecutar el programa utilizando su archivo de entrada.

Ejemplo en PowerShell:

```powershell
Get-Content -Encoding UTF8 Entrada.txt | python solucion.py
```

Para guardar el resultado en un archivo:

```powershell
Get-Content -Encoding UTF8 Entrada.txt | python solucion.py | Out-File -Encoding utf8 salida.txt
```

## Objet
