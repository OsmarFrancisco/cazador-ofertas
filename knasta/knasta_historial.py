"""
knasta_historial.py

Procesa el historial de precios entregado por Knasta.

Convierte dprices en información útil:

- precio mínimo histórico
- precio máximo histórico
- promedio histórico
- historial limpio
- diferencia contra mínimo
- porcentaje sobre mínimo
"""


def analizar_historial(dprices, precio_actual=None):

    # Filtrar solamente precios reales
    historial_limpio = []

    for item in dprices:

        precio = item.get("price")

        if precio is not None:

            historial_limpio.append(
                {
                    "fecha": item.get("date"),
                    "precio": precio
                }
            )


    # Si no hay historial válido
    if not historial_limpio:

        return {
            "precio_minimo_knasta": None,
            "precio_maximo_knasta": None,
            "promedio_historico": None,
            "historial_precios": [],
            "registros_validos": 0
        }


    precios = [
        x["precio"]
        for x in historial_limpio
    ]


    minimo = min(precios)

    maximo = max(precios)

    promedio = round(
        sum(precios) / len(precios),
        2
    )


    resultado = {

        "precio_minimo_knasta": minimo,

        "precio_maximo_knasta": maximo,

        "promedio_historico": promedio,

        "historial_precios":
            historial_limpio,

        "registros_validos":
            len(historial_limpio)
    }


    # Comparación con precio actual
    if precio_actual and minimo:

        diferencia = precio_actual - minimo

        porcentaje = round(
            (diferencia / minimo) * 100,
            2
        )

        resultado["diferencia_minimo"] = diferencia

        resultado["porcentaje_sobre_minimo"] = porcentaje


    return resultado



if __name__ == "__main__":


    ejemplo = [

        {
            "date":"01-06-2026",
            "price":2000
        },

        {
            "date":"02-06-2026",
            "price":1800
        },

        {
            "date":"03-06-2026",
            "price":1900
        },

        {
            "date":"04-06-2026",
            "price":None
        }

    ]


    from pprint import pprint


    pprint(
        analizar_historial(
            ejemplo,
            1900
        )
    )