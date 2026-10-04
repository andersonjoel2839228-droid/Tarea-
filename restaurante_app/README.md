Restaurante App

Aplicación de escritorio desarrollada en Python con Tkinter para la gestión básica de un restaurante.

El proyecto utiliza una arquitectura modular y almacenamiento de información mediante archivos JSON.

Semana 16 — Manejo de eventos en Tkinter

En esta semana se incorpora el manejo de eventos en la interfaz gráfica utilizando Tkinter.

Se trabajan eventos como:

- "command=" para ejecutar acciones desde botones.
- "bind()" para asociar eventos del teclado y componentes.
- "<<TreeviewSelect>>" para detectar la selección de registros.
- "<<ComboboxSelected>>" para detectar cambios en el rol seleccionado.
- "<Return>" para registrar usuarios mediante la tecla Enter.
- "<Escape>" para limpiar el formulario y la selección.

Objetivo del proyecto

Desarrollar una aplicación para un restaurante que permita:

- Iniciar sesión.
- Identificar al usuario autenticado.
- Trabajar con diferentes roles.
- Consultar productos.
- Consultar ventas.
- Administrar usuarios.
- Registrar usuarios.
- Actualizar usuarios.
- Eliminar usuarios.
- Guardar la información en archivos JSON.
- Aplicar eventos de Tkinter mediante callbacks.

Roles del sistema

El sistema maneja tres tipos de usuarios:

Administrador

Puede acceder a la administración de usuarios.

Puede gestionar usuarios de tipo:

- Empleado
- Cliente

Empleado

Puede utilizar las funciones disponibles para el personal del restaurante, pero no puede acceder a la administración de usuarios.

Cliente

Puede utilizar las funciones disponibles para el cliente, pero no puede acceder a la administración de usuarios.

Usuario inicial

El proyecto incluye un usuario administrador inicial:

Usuario: admin
Contraseña: admin123
Rol: Administrador

Este usuario se encuentra almacenado en:

datos/usuarios.json

Arquitectura del proyecto

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
│
├── main.py
└── README.md

Descripción de las carpetas

datos/

Contiene los archivos JSON utilizados para guardar la información de la aplicación.

- "usuarios.json": almacena los usuarios.
- "productos.json": almacena los productos.
- "ventas.json": almacena las ventas.

modelos/

Contiene las clases principales del sistema.

- "Usuario"
- "Producto"
- "Venta"

Cada modelo permite convertir los datos entre objetos Python y diccionarios mediante los métodos "to_dict()" y "from_dict()".

servicios/

Contiene la lógica del sistema.

"archivo_servicio.py" se encarga de leer y guardar archivos JSON.

"restaurante_servicio.py" contiene las operaciones relacionadas con:

- Usuarios.
- Productos.
- Ventas.
- Inicio de sesión.
- Validaciones.
- Persistencia de información.

La interfaz gráfica no realiza directamente operaciones sobre los archivos JSON.

ui/

Contiene las ventanas y componentes gráficos desarrollados con Tkinter.

- "login_view.py": pantalla de inicio de sesión.
- "main_view.py": ventana principal de la aplicación.

assets/

Contiene los recursos visuales de la aplicación, como:

- Iconos.
- Logotipo.
- Imágenes.
- Otros recursos gráficos.

Manejo de usuarios

La administración de usuarios utiliza un formulario y un "Treeview".

El formulario permite trabajar con:

- Nombre.
- Usuario.
- Contraseña.
- Rol.

El "Treeview" muestra información no sensible del usuario:

- ID.
- Nombre.
- Usuario.
- Rol.

La contraseña no se muestra en el "Treeview".

Eventos utilizados

Botones

Las acciones principales utilizan "command=":

ttk.Button(
    ventana,
    text="Registrar",
    command=self.registrar_usuario
)

De esta manera, el botón ejecuta el callback correspondiente.

Selección del Treeview

Se utiliza:

self.tree_usuarios.bind(
    "<<TreeviewSelect>>",
    self.seleccionar_usuario
)

Cuando el usuario selecciona un registro, el callback obtiene el ID seleccionado y consulta nuevamente el usuario mediante "RestauranteServicio".

Esto evita guardar información sensible directamente en el "Treeview".

Combobox

El selector de rol utiliza el evento:

self.combo_rol.bind(
    "<<ComboboxSelected>>",
    self.evento_rol
)

Este evento permite detectar cuando el usuario cambia el rol seleccionado.

Tecla Enter

La tecla Enter se utiliza para registrar el usuario:

self.formulario.bind(
    "<Return>",
    self.evento_return
)

El callback reutiliza el método de registro existente.

Tecla Escape

La tecla Escape permite limpiar el formulario y quitar la selección:

self.formulario.bind(
    "<Escape>",
    self.evento_escape
)

El callback reutiliza el método encargado de limpiar el formulario.

CRUD de usuarios

La aplicación implementa las operaciones principales:

Registrar

Permite crear un nuevo usuario.

Antes de guardar se validan los campos obligatorios y el nombre de usuario.

Consultar

Los usuarios se muestran en un "Treeview".

Actualizar

Al seleccionar un usuario, sus datos se cargan en el formulario para poder modificarlos.

Eliminar

Permite eliminar usuarios después de confirmar la acción.

El sistema protege al usuario actualmente autenticado para evitar su eliminación accidental.

También se garantiza que exista al menos un Administrador.

Persistencia con JSON

La información se almacena utilizando archivos JSON.

La aplicación utiliza una clase de servicio para centralizar las operaciones de lectura y escritura.

Esto permite mantener separada la interfaz gráfica de la persistencia de datos.

Tecnologías utilizadas

- Python
- Tkinter
- JSON
- Programación Orientada a Objetos
- Arquitectura modular
- Git
- GitHub

Requisitos

Para ejecutar el proyecto se necesita:

- Python 3.x
- Tkinter

Tkinter normalmente viene incluido con las instalaciones estándar de Python para Windows.

Instalación y ejecución

1. Descargar o clonar el proyecto

Obtener el proyecto desde GitHub.

2. Abrir la carpeta

Abrir la carpeta:

restaurante_app

desde Visual Studio Code.

3. Abrir la terminal

En Visual Studio Code seleccionar:

Terminal → Nueva terminal

4. Ejecutar la aplicación

Ejecutar:

python main.py

5. Iniciar sesión

Utilizar las credenciales iniciales:

Usuario: admin
Contraseña: admin123

Evolución del proyecto

El proyecto fue desarrollado de forma progresiva.

Inicialmente se creó una estructura modular para separar:

- Datos.
- Modelos.
- Servicios.
- Interfaz gráfica.

Posteriormente se incorporó el inicio de sesión y la identificación del usuario mediante roles.

En la Semana 16 se incorporó el manejo de eventos en Tkinter para mejorar la interacción con la aplicación.

Entre los eventos implementados se encuentran:

- Selección de registros en "Treeview".
- Selección de opciones en "Combobox".
- Uso de la tecla Enter.
- Uso de la tecla Escape.
- Callbacks asociados a botones.

Buenas prácticas aplicadas

El proyecto busca mantener una separación clara de responsabilidades:

- La interfaz se encarga de mostrar información y capturar eventos.
- Los servicios contienen las reglas de negocio.
- Los modelos representan los datos.
- Los archivos JSON almacenan la información.
- La interfaz no modifica directamente los archivos JSON.

También se evita duplicar la lógica de los callbacks. Los eventos llaman a métodos existentes para realizar las operaciones correspondientes.

Seguridad y validaciones

La aplicación incluye validaciones básicas:

- Campos obligatorios.
- Roles válidos.
- Usuarios únicos.
- Protección del usuario actualmente autenticado.
- Protección para mantener al menos un Administrador.

La contraseña se almacena en el archivo JSON debido al alcance académico del proyecto. No se implementan sistemas avanzados de cifrado, recuperación de contraseñas o bloqueo de cuentas.

Conclusión

El proyecto permite aplicar los conocimientos de programación orientada a objetos, manejo de archivos JSON, interfaces gráficas con Tkinter y programación basada en eventos.

La Semana 16 permite mejorar la interacción de la aplicación mediante eventos de teclado y componentes gráficos, manteniendo una arquitectura modular y organizada.