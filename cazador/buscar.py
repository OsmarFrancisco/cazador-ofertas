import sqlite3


DB = "database/productos.db"


def buscar_producto():

    texto = input("🔎 ¿Qué producto buscas?: ")


    conn = sqlite3.connect(DB)
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT producto, precio, tienda, huancayo, entrega, link
        FROM productos
        WHERE producto LIKE ?
        """,
        ("%"+texto+"%",)
    )


    resultados = cursor.fetchall()


    print("\n🔥 MEJORES OFERTAS\n")


    if resultados:


        for r in resultados:


            print("📦 Producto:", r[0])
            print("💰 Precio:", r[1])
            print("🏪 Tienda:", r[2])
            print("📍 Huancayo:", r[3])
            print("🚚 Entrega:", r[4])
            print("🔗 Link:", r[5])

            print("--------------------")


    else:

        print("❌ No hay ofertas")


    conn.close()



if __name__ == "__main__":

    buscar_producto()