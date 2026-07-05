import sqlite3





def buscar_ofertas():



    producto = {

        "nombre": "Audifonos Bluetooth",

        "precio": "S/ 49",

        "tienda": "Tienda prueba",

        "fecha": "27/06/2026"

    }



    return producto







def guardar_producto(producto):



    conexion = sqlite3.connect("precios.db")

    cursor = conexion.cursor()



    cursor.execute("""

    INSERT INTO productos (producto, precio, tienda, fecha)

    VALUES (?, ?, ?, ?)

    """,

    (

        producto["nombre"],

        producto["precio"],

        producto["tienda"],

        producto["fecha"]

    ))



    conexion.commit()

    conexion.close()





oferta = buscar_ofertas()



guardar_producto(oferta)



print("Oferta guardada:")

print(oferta)