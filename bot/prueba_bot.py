import sys
import os
import sqlite3

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from config import TOKEN_TELEGRAM

from cazador.buscador import buscar_ofertas



CHAT_ID = 8952756452




async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 Cazador de Precios Perú activo"
    )



async def ofertas(update: Update, context: ContextTypes.DEFAULT_TYPE):

    conexion = sqlite3.connect("precios.db")
    cursor = conexion.cursor()


    cursor.execute("""
    SELECT producto, precio, tienda, fecha, link
    FROM productos
    ORDER BY id DESC
    LIMIT 5
    """)


    productos = cursor.fetchall()

    conexion.close()


    mensaje = "🔥 Últimas ofertas encontradas:\n\n"


    for p in productos:

        link = p[4] if p[4] else "Sin link"


        mensaje += f"""
📦 Producto: {p[0]}
💰 Precio: {p[1]}
🏪 Tienda: {p[2]}
📅 Fecha: {p[3]}
🔗 Link: {link}

"""


    await update.message.reply_text(mensaje)





async def agregar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = " ".join(context.args)


    try:

        producto, precio, tienda, link = texto.split("|")


        conexion = sqlite3.connect("precios.db")
        cursor = conexion.cursor()


        cursor.execute(
            """
            INSERT INTO productos
            (producto, precio, tienda, fecha, link)
            VALUES (?, ?, ?, date('now'), ?)
            """,
            (
                producto.strip(),
                precio.strip(),
                tienda.strip(),
                link.strip()
            )
        )


        conexion.commit()
        conexion.close()


        await update.message.reply_text(
            "✅ Oferta guardada"
        )


    except:

        await update.message.reply_text(
            "Formato:\n/agregar Producto | Precio | Tienda | Link"
        )





async def buscar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🕵️‍♂️ Buscando ofertas..."
    )


    nuevas = buscar_ofertas()


    await update.message.reply_text(
        "✅ Nuevas ofertas guardadas"
    )





async def auto_buscar(context):

    nuevas = buscar_ofertas()


    if nuevas:


        mensaje = "🔥 NUEVAS OFERTAS ENCONTRADAS:\n\n"


        for oferta in nuevas:

            mensaje += f"""
📦 Producto: {oferta[0]}
💰 Precio: {oferta[1]}
🏪 Tienda: {oferta[2]}
🔗 Link: {oferta[3]}

"""


        await context.bot.send_message(
            chat_id=CHAT_ID,
            text=mensaje
        )


    print("🔄 Búsqueda automática ejecutada")






app = (
    Application.builder()
    .token(TOKEN_TELEGRAM)
    .build()
)



app.add_handler(
    CommandHandler("start", inicio)
)


app.add_handler(
    CommandHandler("ofertas", ofertas)
)


app.add_handler(
    CommandHandler("agregar", agregar)
)


app.add_handler(
    CommandHandler("buscar", buscar)
)



app.job_queue.run_repeating(
    auto_buscar,
    interval=300,
    first=10
)



print("Bot iniciado...")


app.run_polling()