import sqlite3

DB = "ofertas.db"

conexion = sqlite3.connect(DB)
cursor = conexion.cursor()

try:
    # eliminar duplicados por nombre parecido
    cursor.execute("""
    DELETE FROM productos
    WHERE rowid NOT IN (
        SELECT MIN(rowid)
        FROM productos
        GROUP BY LOWER(REPLACE(REPLACE(nombre,' ',''),
        'mouse',''))
    )
    """)

    conexion.commit()

    # quitar productos basura
    palabras = [
        "patrocinado",
        "publicidad",
        "falabella peru",
        "mira tambien"
    ]

    for palabra in palabras:
        cursor.execute(
            """
            DELETE FROM productos
            WHERE LOWER(nombre) LIKE ?
            """,
            (f"%{palabra}%",)
        )

    conexion.commit()

    # ordenar descuentos altos primero si existe campo descuento
    try:
        cursor.execute("""
        UPDATE productos
        SET descuento = REPLACE(descuento,'%','')
        WHERE descuento IS NOT NULL
        """)

        conexion.commit()

    except:
        pass


    print("✅ Productos limpiados correctamente")
    print("✅ Duplicados eliminados")
    

except Exception as e:
    print("❌ Error limpiando:", e)


conexion.close()