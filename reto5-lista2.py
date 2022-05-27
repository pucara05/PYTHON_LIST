def calcularCosto(alto,ancho,profundo):
    volumen=(alto*ancho*profundo)
    costo=(volumen*5)
    if alto>30:
        costo=costo+2000
    if costo>10000:
        iva=costo*0.19
        costo=costo+iva
    return costo

def costoTotal(listaPaquetes,descuento):
    nuevocostoTotal=0
    for i in listaPaquetes:
        alto=i["ALTO"]
        ancho=i["ANCHO"]
        profundo=i["PROFUNDO"]
        nuevocostoTotal=nuevocostoTotal+calcularCosto(alto,ancho,profundo)
    descuento=(descuento*nuevocostoTotal)/100
    nuevocostoTotal=nuevocostoTotal-descuento
    return nuevocostoTotal
        
