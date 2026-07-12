# Sistema de Restaurante

## Estudiante
**Anderson Joel Morales Lara**

## Descripción

Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos. El sistema permite registrar, listar y buscar productos y clientes mediante un menú interactivo desde la consola.

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

## Uso del constructor

La clase **Producto** utiliza el constructor `__init__()` para crear objetos a partir de los datos ingresados por el usuario mediante el menú interactivo.

## Uso de @property y @setter

La clase **Producto** utiliza `@property` y `@setter` para controlar el acceso a los atributos y validar que el nombre, la categoría y el precio sean correctos antes de almacenarlos.

## Uso de @dataclass

La clase **Cliente** está implementada con `@dataclass`, lo que simplifica la creación de objetos y hace el código más limpio y organizado.

## Menú interactivo

El sistema permite:

- Registrar productos.
- Listar productos.
- Buscar productos.