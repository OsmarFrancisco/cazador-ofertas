import sqlite3

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto TEXT,
    precio TEXT,
    tienda TEXT,
    fecha TEXT,
    link TEXT,
    UNIQUE(producto, precio, tienda)
)
""")

conexion.commit()
conexion.close()

print("✅ Base creada correctamente")