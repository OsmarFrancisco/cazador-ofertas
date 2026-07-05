from telegram import Update
from telegram.ext import ContextTypes

import sqlite3


async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 Cazador de Precios Perú activo"
    )


async def ofertas(update: Update, context: ContextTypes.DEFAULT_TYPE):

    conexion = sqlite3.connect("database/productos.db")
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT nombre, precio, tienda, fecha
    FROM productos
    ORDER BY id DESC
    LIMIT 5
    """)

    productos = cursor.fetchall()

    conexion.close()


    if not productos:
        await update.message.reply_text(
            "No hay ofertas todavía"
        )
        return


    mensaje = "🔥 Últimas ofertas encontradas:\n\n"


    for producto in productos:

        mensaje += f"""
📦 Producto: {producto[0]}
💰 Precio: {producto[1]}
🏪 Tienda: {producto[2]}
📅 Fecha: {producto[3]}

"""


    await update.message.reply_text(mensaje)