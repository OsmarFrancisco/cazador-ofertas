import sqlite3
from datetime import datetime
from cazador.tiendas import tiendas


DB = "database/productos.db"


def guardar_oferta(producto, precio, tienda, link):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO productos
            (producto, precio, tienda, fecha, link)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                producto,
                precio,
                tienda,
                datetime.now().strftime("%Y-%m-%d"),
                link
            )
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()



def buscar_ofertas():

    print("🕵️‍♂️ Buscando ofertas...")

    ofertas = [
        {
            "producto":"Mouse Gamer Logitech",
            "precio":"S/79",
            "tienda":"Mercado Libre Perú",
            "link":"https://www.mercadolibre.com.pe"
        },

        {
            "producto":"Audifonos Sony",
            "precio":"S/89",
            "tienda":"Ripley Perú",
            "link":"https://simple.ripley.com.pe"
        },

        {
            "producto":"Teclado Gamer RGB",
            "precio":"S/129",
            "tienda":"Falabella Perú",
            "link":"https://www.falabella.com.pe"
        },

        {
            "producto":"Celular Xiaomi Redmi",
            "precio":"S/399",
            "tienda":"Oechsle",
            "link":"https://www.oechsle.pe"
        }
    ]


    for oferta in ofertas:

        guardado = guardar_oferta(
            oferta["producto"],
            oferta["precio"],
            oferta["tienda"],
            oferta["link"]
        )

        if guardado:
            print("✅ Oferta guardada:", oferta["producto"])


    print("✅ Búsqueda terminada")



if __name__ == "__main__":
    buscar_ofertas()