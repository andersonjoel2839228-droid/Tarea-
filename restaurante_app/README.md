#  Restaurante App - Semana 14

## 👤 Autor
**Nombre:** Anderson Joel Morales Lara  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 14  

---

##  Descripción del proyecto

El presente proyecto corresponde a la Semana 14 de la asignatura Programación Orientada a Objetos. Consiste en el desarrollo de una aplicación de escritorio utilizando Python y Tkinter, orientada a la gestión de productos en un restaurante.

La aplicación implementa una interfaz gráfica organizada mediante componentes y contenedores, respetando una arquitectura modular y utilizando archivos JSON para la persistencia de datos.

---

## Objetivo

Desarrollar una aplicación que permita gestionar productos aplicando los conceptos aprendidos en clase:

- Uso de componentes (Entry, Button, Treeview)
- Uso de contenedores (Frame, LabelFrame)
- Separación de responsabilidades (modelos, servicios, interfaz)
- Persistencia de datos en archivos JSON

---

##  Estructura del proyecto
restaurante_app/ │ ├── datos/ │   ├── productos.json │   └── usuarios.json │ ├── modelos/ │   ├── producto.py │   └── usuario.py │ ├── servicios/ │   ├── archivo_servicio.py │   └── restaurante_servicio.py │ ├── ui/ │   ├── login_view.py │   └── main_view.py │ ├── main.py └── README.md

---

## Funcionalidades

###  Inicio de sesión
- Validación de usuario y contraseña
- Acceso controlado a la aplicación

###  Gestión de productos (CRUD)
La aplicación permite realizar las siguientes operaciones:

- ✔ Registrar productos  
- ✔ Consultar productos  
- ✔ Actualizar productos  
- ✔ Eliminar productos  

---

##  Interfaz gráfica

La interfaz fue desarrollada con Tkinter, utilizando:

###  Contenedores
- Frame
- LabelFrame

###  Componentes
- Entry (entrada de datos)
- Button (acciones del sistema)
- Treeview (visualización de información)

---

##  Flujo de la aplicación

Inicio de la aplicación  
↓  
Pantalla de Login  
↓  
Validación de usuario  
↓  
Vista principal  
↓  
Gestión de productos (CRUD)  
↓  
Actualización de la interfaz  
↓  
Persistencia en archivos JSON  

---

##  Persistencia de datos

Los datos se almacenan en archivos JSON:

- `usuarios.json`: contiene los usuarios registrados
- `productos.json`: almacena los productos ingresados

---

##  Arquitectura del sistema

El proyecto está organizado en capas:

- **Modelos:** representan las entidades del sistema (Producto, Usuario)
- **Servicios:** contienen la lógica de negocio y acceso a datos
- **UI:** gestiona la interfaz gráfica y la interacción con el usuario
- **Datos:** almacenamiento en archivos JSON

Esta separación permite mantener un código organizado, claro y fácil de mantener.

---

## ▶ Ejecución del proyecto

1. Abrir el proyecto en Visual Studio Code  
2. Ejecutar el archivo principal:
python main.py

3. Ingresar con las credenciales:
Usuario: admin Contraseña: 1234

---

##  Requisitos

- Python 3.x  
- Tkinter (incluido en Python)

---

##  Conclusión

Se logró desarrollar una aplicación funcional que cumple con los requerimientos de la Semana 14, aplicando correctamente el uso de componentes y contenedores en Tkinter.

Además, se implementó una arquitectura modular que separa la lógica del sistema de la interfaz gráfica, permitiendo una mejor organización del código y facilitando su mantenimiento.

---