import sqlite3


conn = sqlite3.connect("database/productos.db")

cursor = conn.cursor()


try:

    cursor.execute(
        """
        ALTER TABLE productos
        ADD COLUMN imagen TEXT
        """
    )

    conn.commit()

    print("✅ Columna imagen agregada")


except Exception as e:

    print("Ya existe:",e)


conn.close()