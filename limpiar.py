import sqlite3

conexion = sqlite3.connect("precios.db")
cursor = conexion.cursor()


cursor.execute("""
DELETE FROM productos
WHERE id NOT IN (
    SELECT MIN(id)
    FROM productos
    GROUP BY producto, precio, tienda
)
""")


conexion.commit()

print("Duplicados eliminados")

cursor.execute("SELECT * FROM productos")

for fila in cursor.fetchall():
    print(fila)


conexion.close()