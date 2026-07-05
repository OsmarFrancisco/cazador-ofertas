import sqlite3


DB="database/productos.db"


def mostrar_huancayo():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT * FROM productos
        WHERE tienda LIKE '%Falabella%'
        OR tienda LIKE '%Oechsle%'
        OR tienda LIKE '%Mercado%'
        """
    )


    productos = cursor.fetchall()


    print("🔥 OFERTAS DISPONIBLES PARA HUANCAYO")
    print("")


    for p in productos:

        print("📦",p[1])
        print("💰",p[2])
        print("🏪",p[3])
        print("🔗",p[5])
        print("-------------------")


    conn.close()



if __name__=="__main__":
    mostrar_huancayo()