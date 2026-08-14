Proyecto Restaurante App – Semana 9

Datos del estudiante

Nombre: Joel

Descripción del sistema

El proyecto "restaurante_app" es un sistema básico de administración para un restaurante desarrollado en Python aplicando los principios de Programación Orientada a Objetos.

Esta versión corresponde a la Semana 9 y representa una evolución del proyecto desarrollado en semanas anteriores. En esta etapa se incorporan las principales estructuras de datos de Python: listas, tuplas, diccionarios y conjuntos.

El sistema permite administrar productos y usuarios mediante un menú interactivo ejecutado desde la consola. La lógica de administración se encuentra organizada en la clase "Restaurante", mientras que "main.py" se encarga de la interacción con el usuario.

Estructura del proyecto

restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md

Responsabilidad de los componentes

modelos/producto.py

Contiene la clase "Producto", encargada de representar los productos disponibles en el restaurante.

Cada producto contiene:

- Código.
- Nombre.
- Categoría.
- Precio.

modelos/usuario.py

Contiene la clase "Usuario", que representa a las personas registradas en el sistema.

Cada usuario contiene:

- Identificación.
- Nombre.
- Correo electrónico.

servicios/restaurante.py

Contiene la clase "Restaurante", encargada de administrar las colecciones de productos y usuarios.

Entre sus principales operaciones se encuentran:

- Registrar productos.
- Buscar productos.
- Actualizar productos.
- Eliminar productos.
- Listar productos.
- Registrar usuarios.
- Buscar usuarios.
- Listar usuarios.
- Obtener categorías sin duplicados.

main.py

Es el punto de entrada del programa. Presenta el menú interactivo, solicita los datos mediante "input()" y utiliza los métodos proporcionados por la clase "Restaurante".

README.md

Contiene la documentación del proyecto, su estructura, funcionamiento y explicación de las estructuras de datos utilizadas.

Estructuras de datos utilizadas

Lista ("list")

Las listas se utilizan para almacenar las colecciones dinámicas de objetos del sistema.

En la clase "Restaurante" se utilizan:

self.productos: list[Producto] = []
self.usuarios: list[Usuario] = []

La lista de productos permite registrar, buscar, actualizar, eliminar y listar productos.

La lista de usuarios permite registrar y listar las personas que forman parte del sistema.

Tupla ("tuple")

La tupla se utiliza para representar información que se mantiene estable durante la ejecución del sistema.

También se utiliza en "main.py" para almacenar las opciones válidas del menú:

opciones_menu: tuple[str, ...] = (
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9"
)

Al tratarse de opciones que no necesitan modificarse durante la ejecución, la tupla resulta adecuada.

Diccionario ("dict")

El diccionario se utiliza en "main.py" para establecer una relación entre cada opción del menú y la función que debe ejecutarse.

acciones: dict[str, callable] = {
    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    "4": eliminar_producto,
    "5": listar_productos,
    "6": registrar_usuario,
    "7": listar_usuarios,
    "8": mostrar_categorias,
    "9": salir
}

Esta organización permite evitar una cadena extensa de condiciones y facilita la ejecución de la función correspondiente.

Conjunto ("set")

El conjunto se utiliza para obtener las categorías de los productos sin elementos duplicados.

return {producto.categoria for producto in self.productos}

De esta manera, si existen varios productos de una misma categoría, dicha categoría solamente se muestra una vez.

Funcionalidades del sistema

El programa dispone de las siguientes opciones:

1. Registrar producto.
2. Buscar producto.
3. Actualizar producto.
4. Eliminar producto.
5. Listar productos.
6. Registrar usuario.
7. Listar usuarios.
8. Mostrar categorías.
9. Salir.

Además, el sistema evita registrar productos con códigos repetidos y usuarios con identificaciones repetidas.

Validaciones

El sistema incorpora validaciones básicas para evitar errores durante la ejecución.

Entre ellas se encuentran:

- Validación de precios numéricos.
- Evitar precios negativos.
- Evitar códigos de productos duplicados.
- Evitar identificaciones de usuarios duplicadas.
- Verificación de opciones válidas del menú.
- Manejo de búsquedas cuando un producto o usuario no existe.

Instrucciones para ejecutar

Para ejecutar el programa se debe contar con Python instalado.

Primero se debe abrir una terminal dentro de la carpeta "restaurante_app".

Después se ejecuta:

python main.py

Al ejecutar el programa aparecerá el menú principal y el usuario podrá seleccionar las diferentes opciones mediante la consola.

Reflexión

La utilización adecuada de las estructuras de datos permite organizar la información de una manera más eficiente y comprensible. En este proyecto, las listas son apropiadas para almacenar colecciones que pueden crecer o disminuir durante la ejecución, mientras que las tuplas permiten conservar información estable.

Por otro lado, los diccionarios permiten establecer relaciones directas entre claves y valores, facilitando la organización de las opciones del menú. Finalmente, los conjuntos son útiles cuando se necesita obtener información sin elementos repetidos, como ocurre con las categorías de los productos.

Considero que seleccionar correctamente una estructura de datos es importante porque cada una responde a una necesidad diferente. No se trata solamente de utilizar las estructuras por cumplir un requisito, sino de elegir la que permita resolver de mejor manera el problema planteado y mantener un código organizado, claro y fácil de mantener.