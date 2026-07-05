import sqlite3


conn = sqlite3.connect("database/productos.db")

cursor = conn.cursor()


cursor.execute(
    """
    SELECT 
    producto,
    precio,
    tienda,
    huancayo,
    entrega,
    link
    FROM productos
    """
)


for producto in cursor.fetchall():
    print("")
    print("📦 Producto:", producto[0])
    print("💰 Precio:", producto[1])
    print("🏪 Tienda:", producto[2])
    print("📍 Huancayo:", producto[3])
    print("🚚 Entrega:", producto[4])
    print("🔗 Link:", producto[5])
    print("--------------------")


conn.close()