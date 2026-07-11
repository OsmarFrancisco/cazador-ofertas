import requests
import json
import os

TELEGRAM_TOKEN = "8952756452:AAGfe1S9fs1ACHFn5BuPBEJ2Pix5LvdPEJw"
CHAT_ID = "5267810291"

def limpiar_precio(valor):

    texto = str(valor)

    texto = texto.replace("S/", "")
    texto = texto.replace(",", "")
    texto = texto.strip()

    if "-" in texto:

        texto = texto.split("-")[0].strip()

    try:
        return float(texto)

    except:
        return 0

def enviar_telegram(mensaje):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    respuesta = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensaje
    })

    print("Telegram:", respuesta.text)

def analizar_compra(producto):

    precio = limpiar_precio(producto.get("precio",0))
    minimo = float(producto.get("precio_minimo", precio))
    maximo = float(producto.get("precio_maximo", precio))
    descuento = producto.get("descuento", 0)
    puntaje = producto.get("puntaje", 0)

    historial = producto.get("historial_precios", [])

    tendencia = "➖ Estable"
    bajadas = 0
    subidas = 0

    if len(historial) >= 3:
        precios = [p.get("precio", 0) for p in historial[-7:]]

        for i in range(1, len(precios)):
            if precios[i] < precios[i - 1]:
                bajadas += 1
            elif precios[i] > precios[i - 1]:
                subidas += 1

        if bajadas > subidas:
            tendencia = "📉 Bajando"
        elif subidas > bajadas:
            tendencia = "📈 Subiendo"

    cerca_minimo = ""
    if minimo > 0:
        diferencia_min = ((precio - minimo) / minimo) * 100

        if diferencia_min <= 5:
            cerca_minimo = "💎 Muy cerca del mínimo histórico"
        elif diferencia_min <= 15:
            cerca_minimo = "🟢 Cerca del mínimo histórico"

    impacto = ""

    if len(historial) >= 2:
        ultimo = historial[-1].get("precio", precio)
        anterior = historial[-2].get("precio", precio)

        cambio = ultimo - anterior

        if cambio < 0:
            impacto = f"📉 Cayó {round(abs(cambio),2)} en el último registro"
        elif cambio > 0:
            impacto = f"📈 Subió {round(cambio,2)} en el último registro"
        else:
            impacto = "⚖ Sin cambios recientes"

    confianza = 50

    if descuento >= 50:
        confianza += 25
    elif descuento >= 30:
        confianza += 15

    if tendencia == "📉 Bajando":
        confianza += 10
    elif tendencia == "📈 Subiendo":
        confianza -= 10

    if cerca_minimo:
        confianza += 15

    if puntaje >= 80:
        confianza += 10

    confianza = min(max(confianza, 0), 100)

    if confianza >= 80:
        decision = "💎 COMPRA FUERTE"
    elif confianza >= 65:
        decision = "🔥 BUENA OPORTUNIDAD"
    elif confianza >= 50:
        decision = "⭐ POSIBLE COMPRA"
    else:
        decision = "⚠ MEJOR ESPERAR"

    razones = []

    if descuento > 0:
        razones.append(f"Descuento del {descuento}%")

    if cerca_minimo:
        razones.append(cerca_minimo)

    if tendencia:
        razones.append(f"Tendencia: {tendencia}")

    if impacto:
        razones.append(impacto)

    if puntaje >= 70:
        razones.append("Producto bien valorado")

    return {
        "decision": decision,
        "confianza": confianza,
        "tendencia": tendencia,
        "razones": razones
    }


def calcular_puntaje(producto):

    puntos = 0

    titulo = producto.get(
        "titulo",
        ""
    ).upper()


    marcas = [
        "LOGITECH",
        "RAZER",
        "APPLE",
        "REDRAGON",
        "LENOVO",
        "PHILIPS"
    ]


    for marca in marcas:

        if marca in titulo:

            puntos += 20
            break



    palabras = [

        "GAMER",
        "GAMING",
        "INALAMBRICO",
        "INALÁMBRICO",
        "WIRELESS",
        "BLUETOOTH",
        "RGB",
        "PRO",
        "MASTER",
        "LIGHTSPEED"

    ]


    for palabra in palabras:

        if palabra in titulo:

            puntos += 5




    precio = limpiar_precio(
        producto.get("precio",9999)
    )



    if precio <= 80:

        puntos += 35


    elif precio <= 150:

        puntos += 30


    elif precio <= 250:

        puntos += 20


    elif precio <= 400:

        puntos += 5


    else:

        puntos += 0





    descuento = producto.get(
        "descuento",
        0
    )


    if descuento >= 70:

        puntos += 60


    elif descuento >= 50:

        puntos += 45


    elif descuento >= 30:

        puntos += 30





    especiales = [

        "G502",
        "G304",
        "G305",
        "MX MASTER",
        "BASILISK"

    ]


    for producto_especial in especiales:

        if producto_especial in titulo:

            puntos += 15
            break



    return puntos

def procesar_ofertas(ofertas, historial):

    for producto in ofertas:
          
        if producto.get("ya_enviado"):
            continue 
         
        if "historial_precios" not in producto:
            producto["historial_precios"] = []

        producto["puntaje"] = calcular_puntaje(producto)

        analisis = analizar_compra(producto)
        producto["analisis"] = analisis

        producto["tendencia_texto"] = analisis["tendencia"]
        producto["decision_compra"] = analisis["decision"]
        producto["confianza_compra"] = analisis["confianza"]

        producto["score_ai"] = (
            producto.get("puntaje", 0) * 0.4 +
            producto.get("confianza_compra", 0) * 0.6
        )
        
        descuento = producto.get("descuento", 0)
        puntaje = producto.get("puntaje", 0)
        precio = limpiar_precio(producto.get("precio",0))
        titulo = producto.get("titulo", "")
        precio_habitual = producto.get(
            "precio_maximo",
            precio
        )

        link = producto.get("link", "")
         
        # =====================================
        # 🚨 DETECTOR DE OFERTAS REALES
        # =====================================

        if descuento >= 90:

            nivel_alerta = "⚠️ ERROR EXTREMO"

        elif descuento >= 70:

            nivel_alerta = "🚨 POSIBLE ERROR DE PRECIO"

        elif descuento >= 50:

            nivel_alerta = "🔥 GANGA REAL"

        elif descuento >= 0:

            nivel_alerta = "🟢 BUENA OPORTUNIDAD"

        else:

            nivel_alerta = ""

        producto["nivel_alerta"] = nivel_alerta

        # 🚨 TELEGRAM (SOLO GANGAS REALES)
        if nivel_alerta:

            mensaje = f"""
        {titulo}

        {nivel_alerta}

        💰 Ahora:
        S/ {precio}

        💵 Habitual:
        S/ {precio_habitual}

        📉 Caída real:
        {descuento}%
           
        🛒 Comprar: 
        {link}
        """

            enviar_telegram(mensaje)

            producto["ya_enviado"] = True

    return ofertas