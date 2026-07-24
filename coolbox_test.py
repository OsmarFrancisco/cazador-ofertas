from scrapers import coolbox


productos = coolbox.guardar()


print("TOTAL:")
print(len(productos))


for p in productos[:5]:

    print("----------------")
    print(p)