"""
programa donde se utiliza las funciones basicas como ingresar,buscar,actualizar,borrar,indexar,contar,etc a un registro en una BD mongo utilizando la libreria pymongo"
"""

from pymongo import MongoClient
import datetime


try:

    # instancio un objeto de MongoClient con parametros por defecto 'localhost', 27017
    client = MongoClient()

    # creo conexion base de datos con nombre "personas"
    db = client['personasDB']
    tablaPersonas = db["personas"]

    tablaPersonas.delete_many({})

    # Agregamos una persona
    tablaPersonas.insert_one({"_id": 1,
                             "nombre": "santiago",
                              "apellido": "My first blog post!",
                              "edad": 25,
                              "date": datetime.datetime.utcnow()})

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

    # ********************EJEMPLOS DE INSERTAR DATOS***********************#
    # busco el registro por indice, y agrego solo si no existe dicho indice para evitar error.

    bandera = tablaPersonas.find_one(persona2)

    if bandera == None:
        # Inserto un registro ,indicando key y value.

        tablaPersonas.insert_one(persona2)
    else:
        print(
            "\nya existe el registro con el mismo id:,no se pudo agregar")

    # imprimir la lista
    lista_registros = tablaPersonas.find({})
    for element in lista_registros:
        print(element)

    # insertar por collection/lista
    try:
        lista = [persona3, persona4]
        tablaPersonas.insert_many(lista)
    except Exception as a:
        print(a)

    # Muestro cantidad de registros
    print("la coleccion contiene: ",
          tablaPersonas.count_documents({}), "registros\n")

    # Muestro todos registros
    lista_registros = tablaPersonas.find({})
    for element in lista_registros:
        print(element)

    # *************************************EJEMPLOS DE BUSQUEDA****************************#

    print("\nla 1era persona con 35 de edad es:")
    busquedaEdad = tablaPersonas.find_one({"edad": 35})
    # hago una consulta para encontrar 1 solo registro por mas que haya mas campos con el mismo valor
    print(busquedaEdad)
    print("\nregistro con _id 3:")
    # una forma mas rebuscada en ves de usar find_one
    busquedaId = tablaPersonas.find({"_id": 3})
    # hago una consulta para encontrar 1 solo registro ya que el campo "_id" en mongo es el campo clave y solo habra un unico valor en cada registro
    # al devolver un objeto iterable(aunque contenga 1 solo valor) ,especifico la posición 0 para el 1er elemento.
    print(busquedaId[0])
    busquedaId = tablaPersonas.find({"_id": 3})

    # *************************************EJEMPLO DE UPDATE*********************************#
    print("se actualiza una sola persona con ID =2")
    tablaPersonas.update_one({'_id': 2}, {"$set": {'nombre': "julianAlvarez"}})
    # se actuliza un unico registro con _id =2 el campo nombre :"valor",en caso de que no coincida el campo se me crea un nuevo campo
    print("\n", tablaPersonas.find_one({"_id": 2}))

    print("\nse actualiza las personas con edad 35:")
    tablaPersonas.update_one({'edad': 35}, {"$set": {'edad': 88}})
    # se actuliza un unico registro con _id =2 el campo nombre :"valor",en caso de que no coincidiera el campo se  crea un nuevo campo
    listaDeActualizados = tablaPersonas.find({"edad": 88})
    for element in listaDeActualizados:
        print(element)
    print("se incrementa la edad del _id 2: ")
    # con "$inc" se incrementa el valor
    tablaPersonas.update_one({'_id': 2}, {'$inc': {'edad': 10}})
    print("\n", tablaPersonas.find_one({'_id': 2}), "\n")

    # *************************************EJEMPLO DE DELETE*********************************#

    tablaPersonas.delete_one({"_id": 4})
    # se elimina el registro con _id =4 en la coleccion tablaPersonas yse muestra todos los registros
    nuevaTabla = tablaPersonas.find({})
    for persona in nuevaTabla:
        print(persona)


except:
    print("ocurrio un error MongoDB")
