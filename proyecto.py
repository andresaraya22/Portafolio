from pymongo import MongoClient
from bson.objectid import ObjectId

cliente = MongoClient('mongodb+srv://andresaraya222005:dPYFZmP7xbTELaDf@proyectojosearaya.ilvlcwr.mongodb.net/')
base_datos = cliente['notes_app']
coleccion = base_datos['notes']

def crear_nota():
    titulo = input("Ingrese el título de la nota: ")
    contenido = input("Ingrese el contenido de la nota: ")
    nota = {
        'title': titulo,
        'content': contenido
    }
    resultado = coleccion.insert_one(nota)
    print(f"Nota creada con ID: {resultado.inserted_id}")

def ver_todas_notas():
    notas = coleccion.find()
    for nota in notas:
        print(f"ID: {nota['_id']}, Título: {nota['title']}, Contenido: {nota['content']}")

def ver_nota_por_id(id_nota):
    try:
        nota = coleccion.find_one({'_id': ObjectId(id_nota)})
        if nota:
            print(f"ID: {nota['_id']}, Título: {nota['title']}, Contenido: {nota['content']}")
        else:
            print("Nota no encontrada.")
    except Exception as e:
        print(f"Error: {e}")

def actualizar_nota(id_nota):
    try:
        nuevo_titulo = input("Ingrese el nuevo título de la nota: ")
        nuevo_contenido = input("Ingrese el nuevo contenido de la nota: ")
        resultado = coleccion.update_one(
            {'_id': ObjectId(id_nota)},
            {'$set': {'title': nuevo_titulo, 'content': nuevo_contenido}}
        )
        if resultado.modified_count > 0:
            print("Nota actualizada con éxito.")
        else:
            print("No se encontró ninguna nota para actualizar.")
    except Exception as e:
        print(f"Error: {e}")

def borrar_nota(id_nota):
    try:
        resultado = coleccion.delete_one({'_id': ObjectId(id_nota)})
        if resultado.deleted_count > 0:
            print("Nota eliminada con éxito.")
        else:
            print("No se encontró ninguna nota para eliminar.")
    except Exception as e:
        print(f"Error: {e}")

def principal():
    while True:
        print("\n1. Crear una nota")
        print("2. Ver todas las notas")
        print("3. Ver nota por ID")
        print("4. Actualizar nota")
        print("5. Eliminar nota")
        print("6. Salir")
        opcion = input("Ingrese su opción: ")
        
        if opcion == '1':
            crear_nota()
        elif opcion == '2':
            ver_todas_notas()
        elif opcion == '3':
            id_nota = input("Ingrese el ID de la nota: ")
            ver_nota_por_id(id_nota)
        elif opcion == '4':
            id_nota = input("Ingrese el ID de la nota a actualizar: ")
            actualizar_nota(id_nota)
        elif opcion == '5':
            id_nota = input("Ingrese el ID de la nota a eliminar: ")
            borrar_nota(id_nota)
        elif opcion == '6':
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    principal()
