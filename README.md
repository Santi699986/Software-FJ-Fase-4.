# Sistema Integral Software FJ – Fase 4

Proyecto académico del curso Programación (213023), UNAD. Implementa un sistema en Python para gestionar clientes, servicios y reservas sin utilizar bases de datos.

## Requisitos
- Python 3.10 o superior.
- No requiere instalar librerías externas.

## Estructura
- `main.py`: punto de entrada y demostración de 12 operaciones.
- `entidades.py`: clase abstracta Entidad, Cliente, Servicio y servicios especializados.
- `reservas.py`: clase Reserva y sus estados.
- `gestor.py`: listas internas y operaciones de gestión.
- `excepciones.py`: excepciones personalizadas.
- `logs/`: archivo de registro generado al ejecutar el programa.

## Cómo ejecutar
Desde la carpeta del proyecto, abrir una terminal y ejecutar:

```bash
python main.py
```

En Windows también puede ser necesario:

```bash
py main.py
```

El programa crea `logs/software_fj.log` al ejecutarse.

## Conceptos de POO incluidos
- Abstracción: `Entidad` y `Servicio` son clases abstractas.
- Herencia: `Cliente` hereda de `Entidad`; los tres servicios heredan de `Servicio`.
- Encapsulamiento: atributos privados/protegidos y propiedades de validación en `Cliente`.
- Polimorfismo: cada servicio implementa sus propias versiones de `calcular_costo`, `describir` y `validar_parametros`.
- Sobrecarga simulada: `calcular_costo(horas, impuesto=0.0, descuento=0.0)` acepta distintas combinaciones de parámetros opcionales. Python no implementa sobrecarga tradicional por firma de método.
- Excepciones: clases personalizadas, `try/except`, `else`, `finally` y encadenamiento con `raise ... from ...`.
- Colecciones: listas internas para clientes, servicios y reservas.

## Pruebas
La demostración ejecuta 12 operaciones válidas e inválidas. Revisar la salida de la terminal y el archivo `logs/software_fj.log`.

## Nota para la entrega
Antes de entregar, revisa y comprende el código, ejecuta las pruebas en tu equipo, agrega tu información académica y pega en el PDF el enlace real del repositorio de GitHub. No inventes integrantes ni enlaces.
