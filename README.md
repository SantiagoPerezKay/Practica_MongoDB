# Programa de Práctica - Operaciones Básicas en MongoDB con PyMongo

Este programa es un ejercicio práctico que utiliza funciones básicas como ingresar, buscar, actualizar, borrar, indexar, contar, etc., en un registro de una base de datos MongoDB utilizando la biblioteca PyMongo.

## Nota
Sugerencia de Mejora:
Para mejorar la modularidad y reutilización del código, te sugiero la creación de funciones y módulos específicos para cada operación, como ingresar, buscar, actualizar, borrar, etc.Ya que este es un programa para practicar las operaciones de mongoDB y no esta pensando para su uso "REAL".

## Propósito del Programa

El objetivo de este código es proporcionar ejemplos de cómo realizar operaciones básicas en una base de datos MongoDB. Es un ejercicio de práctica para comprender el uso de PyMongo y las operaciones comunes en una base de datos NoSQL.

## Código en Lenguaje Imperativo

```python
from pymongo import MongoClient
import datetime

try:
    # Instancio un objeto de MongoClient con parámetros por defecto 'localhost', 27017
    client = MongoClient()

    # Creo conexión a la base de datos con nombre "personas"
    db = client['personasDB']
    tablaPersonas = db["personas"]

    # Elimino todos los registros en la colección
    tablaPersonas.delete_many({})

    # Agrego una persona
    tablaPersonas.insert_one({
        "_id": 1,
        "nombre": "santiago",
        "apellido": "My first blog post!",
        "edad": 25,
        "date": datetime.datetime.utcnow()
    })

    persona2 = {"_id": 2,
                "nombre": "santiagoaaaaaaaaaaaaaaaaaaaaa",
                "apellido": "My seconds blog post!",
                "edad": 35,
                "date": datetime.datetime.utcnow()}
    persona3 = {"_id": 3,
                "nombre": "robertototo",
                "apellido": "juarez",
                "edad": 27,
                "date": datetime.datetime.utcnow()}
    persona4 = {"_id": 4,
                "nombre": "gaston",
                "apellido": "gimenez",
                "edad": 35,
                "date": datetime.datetime.utcnow()}

    # Ejemplos de inserción de datos
    # ...

    # Muestro cantidad de registros
    print("La colección contiene: ", tablaPersonas.count_documents({}), "registros\n")

    # Ejemplos de búsqueda
    # ...

    # Ejemplos de actualización
    # ...

    # Ejemplos de eliminación
    # ...

except Exception as e:
    print(f"Ocurrió un error: {e}")

