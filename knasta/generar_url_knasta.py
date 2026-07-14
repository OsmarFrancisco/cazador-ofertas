def crear_knasta_url(producto):

    retail = producto.get("retail")
    product_id = producto.get("product_id")
    url = producto.get("url","")


    if not retail or not product_id:
        return None


    slug = url.split("/")[-2]


    return (
        "https://knasta.pe/detail/"
        f"{retail}/"
        f"{product_id}/"
        f"{slug}"
    )



if __name__ == "__main__":

    producto = {
        "retail":"plazavea",
        "product_id":"20472497",
        "url":
        "https://www.plazavea.com.pe/"
        "smartphone-samsung-galaxy-s24-fe-6-7--8gb-128gb-50mp12mp8mp-negro-20472497/p"
    }


    print(
        crear_knasta_url(producto)
    )