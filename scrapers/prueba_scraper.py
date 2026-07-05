from bs4 import BeautifulSoup



html = """

<html>

<body>



<h1>Celular Samsung A55</h1>



<p class="precio">S/ 999</p>



</body>

</html>

"""



sopa = BeautifulSoup(html, "html.parser")



producto = sopa.h1.text

precio = sopa.find("p", class_="precio").text



print("Producto:", producto)

print("Precio:", precio)