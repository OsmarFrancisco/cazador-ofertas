def calcular_oportunidad(precio_actual, precio_anterior):

    descuento = ((precio_anterior - precio_actual) / precio_anterior) * 100

    if descuento >= 50:
        nivel = "ALTA"

    elif descuento >= 20:
        nivel = "MEDIA"

    else:
        nivel = "BAJA"

    return descuento, nivel