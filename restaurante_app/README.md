# Restaurante App - Semana 12

**Estudiante:** Anderson Joel Morales Lara

## Descripción

Este proyecto corresponde a la evolución del sistema `restaurante_app`
desarrollado durante la asignatura Programación Orientada a Objetos.

En esta Semana 12 se realizaron mejoras en el uso de colecciones para
optimizar las búsquedas y consultas frecuentes del sistema, manteniendo
las funcionalidades desarrolladas anteriormente.

El sistema permite gestionar usuarios, productos, ventas y controlar
el stock de los productos.

## Mejoras realizadas

Se conservaron las listas principales para almacenar y recorrer los
objetos del sistema:

- Lista de productos.
- Lista de usuarios.
- Lista de ventas.

Además, se incorporaron estructuras auxiliares tipo `dict` para mejorar
las búsquedas y evitar recorridos completos innecesarios.

### Índice de productos

Se creó el diccionario:

```python
productos_por_codigo1
