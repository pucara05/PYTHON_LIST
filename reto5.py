import json
with open("lista/paquetes.json")
empresa=json.load(file)

def calcularCosto(alto,ancho,profundo):
    volumen=alto*ancho*profundo
    costo=volumen*5
    if alto>30:
        costo=costo+2000
    if costo>10000:
        iva=costo*0.19
        costo=costo+iva
        return costo
    
def costoTotal(listaPaquetes,descuento):
    total=0
    for i in listaPaquetes:
        alto=i["ALTO"]
        ancho=i["ANCHO"]
        profundo=i["PROFUNDO"]
        costo=calcularCosto(alto,ancho,profundo)
        total=total+costo
    descue=(total*descuento)/100
    total=total-descue
    return total
print(costoTotal(empresa["paquetes"],10))
        
