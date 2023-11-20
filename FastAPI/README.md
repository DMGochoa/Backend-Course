## Métodos HTTP en Nuestra API

### ¿Qué es HTTP?

<p align="justify">
HTTP, o Protocolo de Transferencia de Hipertexto, es un sistema que define cómo se envían y reciben mensajes a través de la web. En nuestra API, usaremos HTTP para comunicarnos con el servidor y realizar diferentes acciones sobre los datos, como crear, obtener, modificar o eliminar información.
</p>

### Métodos HTTP Básicos

<p align="justify">
Existen varios métodos HTTP, pero nos centraremos en los más importantes para construir nuestra API:
</p>

- **POST**: Se usa para crear un nuevo recurso. Por ejemplo, agregar una nueva película a nuestra base de datos.
- **GET**: Se usa para consultar información. Con él, podemos obtener la lista de películas o detalles de una película específica.
- **PUT**: Se usa para modificar un recurso existente. Si necesitamos cambiar la información de una película, usaremos este método.
- **DELETE**: Como su nombre indica, se usa para eliminar un recurso. Si queremos quitar una película de nuestra base de datos, utilizaremos DELETE.

### Nuestra API de Películas

<p align="justify">
A lo largo del curso, construiremos una API que proporcionará información sobre películas. Aquí hay algunas cosas que haremos:
</p>

- **Consulta de Todas las Películas**: Utilizando el método GET, solicitaremos datos de todas las películas disponibles.
- **Filtrado de Películas**: Podremos buscar películas por su ID o categoría, usando GET junto con parámetros específicos.
- **Registro de Películas**: Para añadir nuevas películas a nuestra base de datos, usaremos el método POST.
- **Modificación y Eliminación**: Completaremos nuestra API con la capacidad de modificar (con PUT) y eliminar películas (con DELETE).

