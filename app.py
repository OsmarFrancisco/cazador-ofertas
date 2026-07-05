from flask import Flask, render_template, redirect
import json
import os

from analizador import procesar_ofertas

app = Flask(__name__)


def cargar_json(archivo):
    if not os.path.exists(archivo):
        return []

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


@app.route("/")
def home():
    ofertas = cargar_json("ofertas.json")
    historial = cargar_json("historial.json")


    ofertas = sorted(
        ofertas,
        key=lambda x: x.get("score_ai", 0),
        reverse=True
    )

    top_ofertas = ofertas[:5]

    return render_template(
        "index.html",
        ofertas=ofertas[5:],
        top_ofertas=top_ofertas,
        mejor_oferta=top_ofertas[0] if top_ofertas else None
    )


@app.route("/actualizar")
def actualizar():
    os.system("python actualizador.py")
    return redirect("/")


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))

    app.run(host="0.0.0.0", port=port)