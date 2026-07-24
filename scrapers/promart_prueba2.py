from promart import obtener_promart


productos = obtener_promart()


print("TOTAL:")
print(len(productos))


for p in productos[:5]:

    print("----------------")
    print(p)