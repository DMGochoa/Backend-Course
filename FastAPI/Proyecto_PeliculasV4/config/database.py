import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Nombre del archivo de la base de datos SQLite.
sqlite_file_name = "../database.sqlite"

# Obtenemos la ruta absoluta del directorio actual donde se encuentra este archivo.
# Esto es necesario para construir la ruta completa a la base de datos SQLite.
base_dir = os.path.dirname(os.path.realpath(__file__))

# Construimos la ruta absoluta al archivo de la base de datos combinando el 
# directorio base y el nombre del archivo.
path_file_database = os.path.join(base_dir, sqlite_file_name)

# Creamos la cadena de conexión a la base de datos SQLite utilizando la ruta del archivo.
# El prefijo 'sqlite:///' indica que se trata de una base de datos SQLite.
database_url = f"sqlite:///{path_file_database}"

# Creamos un 'engine' de SQLAlchemy, que es el punto de entrada a la base de datos.
# Este 'engine' se usará para interactuar con la base de datos. 
# El argumento 'echo=True' activa el logging de SQL, lo que es útil para depuración.
engine = create_engine(database_url, echo=True)

# Creamos una fábrica de sesiones de SQLAlchemy.
# Cada sesión creada a partir de esta fábrica estará vinculada al 'engine' creado 
# anteriormente, lo que permite realizar operaciones en la base de datos.
Session = sessionmaker(bind=engine)

# Declarative Base: Sirve como clase base para todas las clases de modelos en SQLAlchemy.
# Permite definir la estructura de las tablas y sus relaciones en forma de clases de Python.
Base = declarative_base()
