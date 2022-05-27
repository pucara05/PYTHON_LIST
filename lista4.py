# hacer un programa que utilice dos funciones y que cargue un dicionario con los productos
# de una venta,por medio de las funciones calcule el precio unitario
#y el valor a pagar

import json
with open("productos.json") as file:
    tienda=json.load(file)
    


#funciones
    def precioUnitario(nombre,precio,cantidad)
    valor=precio*cantidad
    return valor
def valorPagar(listaProductos,descuento):
    total=0
    for i in listaProductos:
        nombre=i["nombre"]
        precio=i["precio"]
        cantidad=i["cantidad"]
        total=total+precioUnitario(nombre,precio,cantidad)
     descuento=(total*descuento)/100
     total=total-descuento
     return total
        




#cuerpo del programa
    print("el valor a pagar por la compra es: ", valorPagar(tienda["producto"],10)))
