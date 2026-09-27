Restaurante App

Semana 15 - Conceptos fundamentales de manejo de eventos

Estudiante: Anderson Joel Morales Lara
Asignatura: Programación Orientada a Objetos
Proyecto: restaurante_app
Semana: 15

---

1. Descripción del proyecto

"restaurante_app" es una aplicación desarrollada en Python que permite gestionar información básica de un restaurante mediante una interfaz gráfica construida con Tkinter.

El proyecto utiliza una arquitectura modular que separa los datos, modelos, servicios y la interfaz gráfica.

En la Semana 15 se continúa el desarrollo realizado en semanas anteriores, incorporando el manejo de eventos mediante botones y callbacks para registrar ventas.

La aplicación permite:

- Iniciar sesión.
- Consultar usuarios registrados.
- Consultar productos disponibles.
- Seleccionar un usuario.
- Seleccionar un producto.
- Registrar una venta.
- Guardar las ventas en un archivo JSON.
- Visualizar las ventas registradas en la interfaz.

---

2. Objetivo de la Semana 15

El objetivo principal es comprender los fundamentos básicos del manejo de eventos en una aplicación gráfica.

En este proyecto, una acción realizada por el usuario inicia una secuencia de operaciones:

Usuario → Botón → "command=" → Callback → RestauranteServicio → Persistencia → Respuesta visual

De esta manera, la interfaz gráfica se encarga de recibir las acciones del usuario, mientras que las reglas y operaciones del sistema permanecen dentro de la capa de servicios.

---

3. Manejo de eventos

La operación principal de esta semana es el registro de ventas.

El botón "Registrar venta" utiliza el parámetro "command=" para ejecutar el método:

command=self.registrar_venta_callback

Cuando el usuario presiona el botón, se ejecuta el callback:

def registrar_venta_callback(self):

El callback obtiene el usuario y producto seleccionados desde la interfaz y solicita al servicio que registre la operación.

El flujo implementado es:

Usuario
   ↓
Selecciona usuario y producto
   ↓
Presiona "Registrar venta"
   ↓
command=
   ↓
registrar_venta_callback()
   ↓
RestauranteServicio
   ↓
Validación de usuario y producto
   ↓
Creación de la venta
   ↓
ventas.json
   ↓
Actualización de la tabla
   ↓
Mensaje de confirmación

---

4. Gestión de ventas

La aplicación permite relacionar un usuario existente con un producto existente.

Cada venta contiene:

- ID de la venta.
- ID del usuario.
- ID del producto.
- Fecha y hora de la operación.

La información se representa mediante el modelo "Venta".

Ejemplo:

{
    "id": 1,
    "usuario_id": 1,
    "producto_id": 2,
    "fecha": "2026-09-27 18:30:00"
}

Las ventas se almacenan permanentemente en:

datos/ventas.json

---

5. Persistencia en archivos JSON

El proyecto utiliza archivos JSON para almacenar la información.

Los archivos principales son:

productos.json
usuarios.json
ventas.json

La lectura y escritura de estos archivos se realiza mediante la clase:

ArchivoServicio

De esta forma, la interfaz gráfica no manipula directamente los archivos JSON.

La persistencia se encuentra separada de la interfaz para mantener una mejor organización del proyecto.

---

6. Arquitectura del proyecto

La estructura principal del proyecto es:

restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│   ├── logo.png
│   └── icono_venta.png
│
├── main.py
│
└── README.md

---

7. Responsabilidad de cada componente

Datos

La carpeta "datos" contiene los archivos JSON utilizados para conservar la información del sistema.

Modelos

La carpeta "modelos" contiene las clases principales:

- "Producto"
- "Usuario"
- "Venta"

Estas clases representan las entidades utilizadas por la aplicación.

Servicios

La carpeta "servicios" contiene la lógica relacionada con los datos y las operaciones del restaurante.

"ArchivoServicio" se encarga de leer y guardar información en archivos JSON.

"RestauranteServicio" contiene operaciones como:

- Obtener usuarios.
- Validar usuarios.
- Obtener productos.
- Obtener ventas.
- Registrar ventas.

Interfaz

La carpeta "ui" contiene las ventanas de la aplicación.

"LoginView" gestiona el inicio de sesión.

"MainView" presenta las secciones de usuarios, productos y ventas.

Assets

La carpeta "assets" contiene los recursos visuales utilizados por la aplicación, como el logotipo y el ícono de ventas.

---

8. Interfaz gráfica

La aplicación utiliza Tkinter y ttk para construir la interfaz gráfica.

La ventana principal contiene diferentes secciones:

- Usuarios: permite visualizar los usuarios registrados.
- Productos: permite visualizar los productos disponibles.
- Ventas: permite seleccionar un usuario y un producto y registrar una venta.

Las ventas registradas se muestran mediante un componente "Treeview".

La interfaz también utiliza recursos visuales almacenados en la carpeta "assets".

---

9. Validaciones

Antes de registrar una venta, el sistema verifica que el usuario y el producto seleccionados existan.

Estas validaciones se realizan dentro de "RestauranteServicio", no directamente en la interfaz.

Si el usuario seleccionado no existe, el sistema muestra un mensaje de error.

Si el producto seleccionado no existe, también se informa al usuario.

Esto permite mantener separadas las responsabilidades de la interfaz y de la lógica del sistema.

---

10. Ejecución del proyecto

Para ejecutar la aplicación se debe tener Python instalado.

Desde la carpeta principal del proyecto se ejecuta:

python main.py

Al iniciar la aplicación aparece la ventana de inicio de sesión.

Se pueden utilizar los usuarios registrados en "usuarios.json".

Por ejemplo:

Usuario: juan
Contraseña: 1234

Después de iniciar sesión se muestra la ventana principal del restaurante.

---

11. Prueba del registro de una venta

Para comprobar el funcionamiento de la Semana 15:

1. Ejecutar "main.py".
2. Iniciar sesión.
3. Ingresar a la sección Ventas.
4. Seleccionar un usuario.
5. Seleccionar un producto.
6. Presionar Registrar venta.
7. Verificar el mensaje de confirmación.
8. Revisar que la venta aparezca en la tabla.
9. Revisar que la información se haya guardado en "ventas.json".
10. Cerrar y volver a ejecutar la aplicación para comprobar que la venta permanece almacenada.

---

12. Conclusión

La Semana 15 permite aplicar los conceptos fundamentales del manejo de eventos en una aplicación gráfica.

El proyecto demuestra cómo una acción realizada por el usuario puede iniciar un evento mediante "command=", ejecutar un callback y delegar la operación a "RestauranteServicio".

La información de las ventas se mantiene mediante persistencia en archivos JSON y posteriormente se actualiza la interfaz para mostrar el resultado de la operación.

De esta manera, "restaurante_app" continúa evolucionando sobre la arquitectura desarrollada en semanas anteriores, manteniendo una separación clara entre modelos, servicios, datos e interfaz gráfica.