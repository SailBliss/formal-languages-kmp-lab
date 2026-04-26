# kmp-lab-python

## Propósito

El objetivo es entender e implementar el algoritmo de Knuth-Morris-Pratt (KMP) y la función failure desde cero, siguiendo un proceso paso a paso con pseudocódigo y ejemplos manuales.

## Entorno

- Sistema operativo: Windows 11
- Versión de Python: 3.13.7

## Herramientas usadas

- Python (solo librería estándar)
- Git
- Visual Studio Code
- Claude (tutor con IA)

## Estructura del proyecto

```
kmp-lab-python/
├── failure.py      # función failure (arreglo de prefijo-sufijo)
├── kmp.py          # algoritmo de búsqueda KMP
├── examples.py     # ejemplos de uso y salidas
├── docs/
│   └── hw-2.pdf    # material de referencia
└── README.md
```

## Algoritmos

### Función failure -> `failure.py`

Calcula una tabla para el patrón.

En cada posición se guarda cuántas letras del inicio del patrón también aparecen al final de esa parte del patrón.

Esta tabla ayuda a KMP a saber hasta dónde volver cuando hay una diferencia, sin revisar letras de más.

Ejemplo:

```
patrón:   A  B  A  B
failure:  0  0  1  2
```

### Búsqueda KMP -> `kmp.py`

Busca un patrón dentro de un texto de forma rápida.

El algoritmo usa una tabla llamada failure para no repetir comparaciones innecesarias cuando encuentra una diferencia. Así, el texto se recorre una sola vez y nunca se vuelve hacia atrás.

Ejemplo:

```
texto:    A A B A B A B
patrón:   A B A B
resultado: [1, 3]
```

## Cómo ejecutar

```bash
python examples.py
```

Para probar las funciones por separado:

```bash
python -c "from failure import compute_failure; print(compute_failure('ABAB'))"
# [0, 0, 1, 2]

python -c "from kmp import kmp_search; print(kmp_search('AABABAB', 'ABAB'))"
# [1, 3]
```

## Declaración de uso de IA

Este proyecto fue desarrollado con la asistencia de Claude (Anthropic) como herramienta de aprendizaje.

Claude se utilizó para:
- Explicar los conceptos de la función failure y el algoritmo KMP paso a paso.
- Ayudar a entender el pseudocódigo antes de escribir el código.

El formato del documento (REAMDE.md) fue
generado con Claude por motivos estéticos. Sin embargo, toda la información y el contenido fueron
escritos a mano y de forma consciente; las herramientas de IA se
usaron únicamente como apoyo y en ningún momento reemplazaron el aprendizaje. Todo el codigo fue escrito a mano.

