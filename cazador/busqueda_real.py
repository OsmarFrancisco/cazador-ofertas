import sqlite3
from datetime import datetime


DB = "database/productos.db"


def guardar(producto, precio, tienda, link, imagen):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO productos
        (producto, precio, tienda, fecha, link, huancayo, entrega, imagen)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            producto,
            precio,
            tienda,
            datetime.now().strftime("%Y-%m-%d"),
            link,
            "SI",
            "Recojo tienda / Envio",
            imagen
        )
    )

    conn.commit()
    conn.close()



def buscar():

    print("🕵️ Buscando ofertas Huancayo")


    tiendas = [

        (
            "Falabella Perú",
            "https://www.falabella.com.pe"
        ),

        (
            "Oechsle",
            "https://www.oechsle.pe"
        ),

        (
            "Mercado Libre Perú",
            "https://www.mercadolibre.com.pe"
        )
    ]


    productos = [

        (
            "Mouse Gamer",
            "S/79",
            "https://via.placeholder.com/200?text=Mouse"
        ),

        (
            "Audifonos Bluetooth",
            "S/89",
            "https://via.placeholder.com/200?text=Audifonos"
        ),

        (
            "Teclado Gamer RGB",
            "S/129",
            "https://via.placeholder.com/200?text=Teclado"
        ),

        (
            "Celular Xiaomi Redmi",
            "S/399",
            "https://via.placeholder.com/200?text=Celular"
        )
    ]


    for tienda, url in tiendas:

        for producto, precio, imagen in productos:


            guardar(
                producto,
                precio,
                tienda,
                url,
                imagen
            )


            print(
                "✅ Guardado:",
                producto,
                "-",
                tienda
            )


    print("✅ Búsqueda terminada")



if __name__ == "__main__":

    buscar()