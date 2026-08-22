# Restaurante App - Semana 10

## Datos del estudiante

**Nombre:** Joel Morales  
**Asignatura:** Programación Orientada a Objetos  
**Actividad:** Semana 10

## Descripción del proyecto

Restaurante App es un sistema desarrollado en Python para administrar productos de un restaurante mediante programación orientada a objetos.

En esta Semana 10 se incorporó la persistencia de datos mediante archivos JSON. Esto permite que los productos registrados no se pierdan cuando se cierra el programa.

El sistema permite registrar, listar, buscar, actualizar y eliminar productos. Los productos son manejados durante la ejecución como objetos de la clase `Producto` y posteriormente se convierten a diccionarios únicamente para almacenarlos en el archivo JSON.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md