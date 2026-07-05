import sqlite3

db = sqlite3.connect("ofertas.db")

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    precio TEXT,
    descuento INTEGER DEFAULT 0,
    tienda TEXT,
    ubicacion TEXT,
    envio TEXT,
    categoria TEXT,
    fecha TEXT
)
""")

db.commit()
db.close()

print("✅ Tabla productos creada correctamente")