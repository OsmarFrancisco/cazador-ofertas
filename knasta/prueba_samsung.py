from knasta.knasta_integrador import integrar_knasta


producto = {
    "titulo": "Samsung Galaxy S24 FE",
    "precio": "S/ 1899",
    "tienda": "Plazavea",
    "knasta_url": "https://knasta.pe/detail/plazavea/20472497/smartphone-samsung-galaxy-s24-fe-67-8gb-128gb-50mp-12mp-8mp-negro?q=Samsung+Galaxy+S24"
}


resultado = integrar_knasta(producto)

print("\n====================")
print("RESULTADO KNasta")
print("====================")

for clave, valor in resultado.items():
    print(clave, ":", valor)