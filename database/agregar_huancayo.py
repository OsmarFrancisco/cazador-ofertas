import sqlite3

conn = sqlite3.connect("database/productos.db")

cursor = conn.cursor()

try:
    cursor.execute(
        "ALTER TABLE productos ADD COLUMN huancayo TEXT"
    )

    cursor.execute(
        "ALTER TABLE productos ADD COLUMN entrega TEXT"
    )

    print("✅ Columnas agregadas")

except Exception as e:
    print("Ya existen o error:",e)


conn.commit()
conn.close()