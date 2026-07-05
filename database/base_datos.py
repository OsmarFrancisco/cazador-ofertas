import sqlite3

conexion = sqlite3.connect("precios.db")
cursor = conexion.cursor()

try:
    cursor.execute(
        "ALTER TABLE productos ADD COLUMN link TEXT"
    )
    print("Columna link agregada")
except:
    print("La columna link ya existe")

conexion.commit()
conexion.close()