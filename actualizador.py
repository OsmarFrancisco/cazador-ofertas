from scrapers import falabella
from scrapers import lacuracao
from scrapers import oechsle
from scrapers import plazavea
from scrapers import tottus
from scrapers import promart
from scrapers import coolbox


from analizador import procesar_ofertas

from knasta.knasta_integrador import integrar_lista_knasta
from knasta.llenar_knasta_url import llenar_knasta_urls

import json
import os
from datetime import datetime


ARCHIVO = "ofertas.json"
HISTORIAL = "historial.json"


def guardar_json(nombre, data):

    with open(
        nombre,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


def cargar_historial():

    if os.path.exists(HISTORIAL):

        with open(
            HISTORIAL,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    return []


def limpiar_precio(precio):

    try:

        return float(
            str(precio)
            .replace("S/", "")
            .replace(",", "")
            .strip()
        )

    except:

        return 0


def calcular_nivel(descuento):

    if descuento >= 70:
        return "🔥🔥 OFERTA EXTREMA"

    if descuento >= 50:
        return "🔥 OFERTA REAL"

    if descuento >= 30:
        return "⭐ BUENA OPORTUNIDAD"

    return "📦 Oferta"


def actualizar_historial(ofertas):

    historial = cargar_historial()

    for producto in ofertas:

        titulo = producto.get(
            "titulo",
            ""
        ).strip()

        tienda = producto.get(
            "tienda",
            ""
        ).strip()

        link = producto.get(
            "link",
            ""
        ).strip()

        precio = limpiar_precio(
            producto.get(
                "precio",
                0
            )
        )

        # ============================
        # ID ÚNICO DEL PRODUCTO
        # ============================

        if link:
            producto_id = f"{tienda}|{link}"
        else:
            producto_id = f"{tienda}|{titulo.lower()}"

        producto["id"] = producto_id

        encontrado = None

        for viejo in historial:

            if viejo.get("id") == producto_id:

                encontrado = viejo

                break

        if encontrado:

            # completar datos antiguos

            if "precio_minimo" not in encontrado:
                encontrado["precio_minimo"] = encontrado.get(
                    "precio",
                    precio
                )

            if "veces_visto" not in encontrado:
                encontrado["veces_visto"] = 1

            if "fecha_primera" not in encontrado:
                encontrado["fecha_primera"] = encontrado.get(
                    "fecha",
                    str(datetime.now())
                )

            if "fecha_ultima" not in encontrado:
                encontrado["fecha_ultima"] = encontrado.get(
                    "fecha",
                    str(datetime.now())
                )

            maximo = encontrado.get(
                "precio_maximo",
                encontrado["precio"]
            )


            minimo = encontrado.get(
                "precio_minimo",
                encontrado["precio"]
            )


            if precio > maximo:

                maximo = precio



            if precio < minimo:

                minimo = precio




            descuento = 0



            if maximo > 0 and precio < maximo:


                descuento = (
                    (maximo - precio)
                    /
                    maximo
                    *
                    100
                )




            producto["precio_anterior"] = maximo


            producto["precio_minimo"] = minimo


            producto["descuento"] = round(
                descuento,
                1
            )


            producto["nivel"] = calcular_nivel(
                descuento
            )

            encontrado["precio_anterior"] = encontrado.get(
                "precio",
                precio
            )

            encontrado["precio"] = precio


            if precio < encontrado.get(
                "precio_minimo",
                precio
            ):

                encontrado["precio_minimo"] = precio


            encontrado["precio_maximo"] = maximo


            encontrado["veces_visto"] = encontrado.get(
                "veces_visto",
                1
            ) + 1


            encontrado["fecha_ultima"] = str(
                datetime.now()
            )

        else:

            historial.append(

                {

                    "id": producto_id,

                    "titulo": titulo,

                    "tienda": tienda,

                    "precio": precio,

                    "precio_maximo": precio,
                    
                    "precio_minimo": precio,

                    "veces_visto": 1,
                    
                    "fecha_primera": str(
                        datetime.now()
                    ),

                    "fecha_ultima": str(
                        datetime.now()
                    )

                }

            )
         
    guardar_json(
        HISTORIAL,
        historial
    )


print("🔄 Actualizando ofertas...")

ofertas = []


# FALABELLA

try:

    f = falabella.guardar()

    print(
        "✔ Falabella:",
        len(f)
    )

    if f:

        ofertas.extend(f)

except Exception as e:

    print(
        "❌ Falabella error:",
        e
    )
# ==========================
# LA CURACAO
# ==========================

print("\n🔎 Buscando La Curacao...")


try:

    productos_lacuracao = lacuracao.guardar()


    print(
        "✔ La Curacao:",
        len(productos_lacuracao)
    )


    if productos_lacuracao:

        ofertas.extend(productos_lacuracao)
        print("DEBUG LA CURACAO:")
        for p in productos_lacuracao[:5]:
            print(
                p.get("titulo"),
                "|",
                p.get("tienda"),
                "|",
                p.get("precio")
            )

except Exception as e:

    print(
        "❌ La Curacao error:",
        e
    )

# ==========================
# OECHSLE
# ==========================

print("\n🔎 Buscando Oechsle...")

try:

    productos_oechsle = oechsle.guardar()

    print(
        "✔ Oechsle:",
        len(productos_oechsle)
    )

    if productos_oechsle:

        ofertas.extend(productos_oechsle)

except Exception as e:

    print(
        "❌ Oechsle error:",
        e
    )

# ==========================
# PLAZAVEA
# ==========================

print("\n🔎 Buscando PlazaVea...")


try:

    productos_plazavea = plazavea.guardar()


    print(
        "✔ PlazaVea:",
        len(productos_plazavea)
    )


    if productos_plazavea:

        ofertas.extend(productos_plazavea)


except Exception as e:

    print(
        "❌ PlazaVea error:",
        e
    )

# ==========================
# TOTTUS
# ==========================

print("\n🔎 Buscando Tottus...")


try:

    productos_tottus = tottus.guardar()


    print(
        "✔ Tottus:",
        len(productos_tottus)
    )


    if productos_tottus:

        ofertas.extend(productos_tottus)


except Exception as e:

    print(
        "❌ Tottus error:",
        e
    )

# ==========================
# TOTTUS
# ==========================

print("\n🔎 Buscando Tottus...")


try:

    productos_tottus = tottus.guardar()


    print(
        "✔ Tottus:",
        len(productos_tottus)
    )


    if productos_tottus:

        ofertas.extend(productos_tottus)


except Exception as e:

    print(
        "❌ Tottus error:",
        e
    )

# ==========================
# PROMART
# ==========================

print("\n🔎 Buscando Promart...")


try:

    productos_promart = promart.obtener_promart()


    print(
        "✔ Promart:",
        len(productos_promart)
    )


    if productos_promart:

        ofertas.extend(productos_promart)


except Exception as e:

    print(
        "❌ Promart error:",
        e
    )


# ==========================
# COOLBOX
# ==========================

print("\n🔎 Buscando Coolbox...")


try:

    productos_coolbox = coolbox.guardar()


    print(
        "✔ Coolbox:",
        len(productos_coolbox)
    )


    if productos_coolbox:

        ofertas.extend(productos_coolbox)


except Exception as e:

    print(
        "❌ Coolbox error:",
        e
    )
    
# MERCADO LIBRE DESACTIVADO
#
# try:
#
#     m = mercadolibre.guardar()
#
#     if m:
#         ofertas.extend(m)
#
# except Exception as e:
#
#     print(e)

# ====================================
# ELIMINAR DUPLICADOS (SEGURO)
# ====================================

ofertas_unicas = {}
duplicados = 0

for producto in ofertas:

    tienda = producto.get("tienda", "").strip()

    link = producto.get("link", "").strip()

    titulo = producto.get("titulo", "").strip().lower()

    if link:
        clave = f"{tienda}|{link}"
    else:
        clave = f"{tienda}|{titulo}"

    if clave not in ofertas_unicas:
        ofertas_unicas[clave] = producto
    else:
        duplicados += 1

ofertas = list(ofertas_unicas.values())

print("🧹 Duplicados eliminados:", duplicados)
print("📦 Productos únicos:", len(ofertas))

print("🔎 Buscando URLs Knasta...")

ofertas = llenar_knasta_urls(
    ofertas
)

actualizar_historial(
    ofertas
)


print("🔎 Integrando historial Knasta...")


ofertas = integrar_lista_knasta(
    ofertas
)


ofertas = procesar_ofertas(
    ofertas,
    cargar_historial()
)

guardar_json(
    ARCHIVO,
    ofertas
)


print(
    "TOTAL FINAL:",
    len(ofertas)
)

print(
    "📈 Historial actualizado"
)

print(
    "🔥 Cazador listo"
)