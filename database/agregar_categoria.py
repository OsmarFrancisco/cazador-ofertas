import sqlite3


conn = sqlite3.connect(
    "database/productos.db"
)

cursor = conn.cursor()


try:

    cursor.execute(
    """
    ALTER TABLE productos
    ADD COLUMN categoria TEXT
    """
    )

    print("✅ Categoria agregada")


except:

    print("ℹ️ Ya existe")


conn.commit()
conn.close()