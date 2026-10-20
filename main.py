import sqlite3
import matplotlib.pyplot as plt

def crear_base_datos():
    conexion = sqlite3.connect('cinebot.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS peliculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            calificacion INTEGER
        )
    ''')
    conexion.commit()
    conexion.close()

def agregar_pelicula():
    titulo = input("Ingrese el titulo de la pelicula: ")
    genero = input("Ingrese el genero: ")
    try:
        calificacion = int(input("Calificacion del 1 al 5: "))
        if calificacion < 1 or calificacion > 5:
            print("La calificacion debe estar entre 1 y 5.")
            return
    except ValueError:
        print("Error: Debe ingresar un numero entero.")
        return

    conexion = sqlite3.connect('cinebot.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO peliculas (titulo, genero, calificacion) VALUES (?, ?, ?)", (titulo, genero, calificacion))
    conexion.commit()
    conexion.close()
    print(f"Pelicula '{titulo}' guardada con exito!")

def mostrar_estadisticas():
    conexion = sqlite3.connect('cinebot.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT genero, COUNT(*) FROM peliculas GROUP BY genero")
    datos = cursor.fetchall()
    conexion.close()

    if not datos:
        print("No hay peliculas registradas aun.")
        return

    generos = [dato[0] for dato in datos]
    cantidades = [dato[1] for dato in datos]

    plt.figure(figsize=(8, 5))
    plt.bar(generos, cantidades, color='skyblue')
    plt.title('Peliculas registradas por Genero')
    plt.xlabel('Genero')
    plt.ylabel('Cantidad')
    plt.show()

def menu():
    crear_base_datos()
    while True:
        print("\n--- BIENVENIDO A CINEBOT ---")
        print("1. Registrar nueva pelicula")
        print("2. Ver estadisticas (Grafico)")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            agregar_pelicula()
        elif opcion == '2':
            mostrar_estadisticas()
        elif opcion == '3':
            print("Saliendo de CINEBOT...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
