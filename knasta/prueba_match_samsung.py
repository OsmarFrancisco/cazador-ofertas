from knasta.buscar_producto_knasta import buscar_producto_knasta


resultado = buscar_producto_knasta(
    "S24 FE"
)


print("================")
print("TOTAL:", len(resultado))
print("================")


for p in resultado:

    print()
    print("TITULO:", p.get("title"))
    print("TIENDA:", p.get("retail_label"))
    print("PRECIO:", p.get("current_price"))
    print("URL:", p.get("url"))