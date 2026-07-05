import sqlite3


conn = sqlite3.connect("database/productos.db")

cur = conn.cursor()


try:

    cur.execute(
    """
    ALTER TABLE productos
    ADD COLUMN actualizado TEXT
    """
    )

    print("✅ Campo actualizado agregado")

except:

    print("⚠️ Ya existe")


conn.commit()
conn.close()