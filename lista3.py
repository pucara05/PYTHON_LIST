#tupla es inmutable no se puede cambiar como una constante
numeros=(1,2,3,4,5)
#array,lista,vectores se pueden cambiar sus valores
edades=[20,32,11,15,17,48]

print(numeros[2])

#dicionario se habren con llaves y se cieran con llaves
#tienen una clave y un valor
#1.clave
#2.valor

#clave:valor

tripulantes={"nombre":"david","edad":25,"genero":"masculino"}

print(tripulantes["edad"])

print("-------------------------------------")
tripulantes["estado_civil"]="soltero"
print(tripulantes)

tripulantes["edad"]=28
print(tripulantes)


tripulantes.pop("genero")
print(tripulantes)
print("---------------------------")

