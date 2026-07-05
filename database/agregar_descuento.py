import sqlite3


conn = sqlite3.connect(
    "database/productos.db"
)

cursor = conn.cursor()


for columna in [
    "precio_anterior",
    "descuento"
]:

    try:

        cursor.execute(
        f"""
        ALTER TABLE productos
        ADD COLUMN {columna} TEXT
        """
        )

        print("✅ Agregado:", columna)


    except:

        print("ℹ️ Ya existe:", columna)



conn.commit()
conn.close()