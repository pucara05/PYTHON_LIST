#lista=variable pero diferencia se pueden almacenar muchos valores
#ejemplo tripulantes=["ana,"mildrey","liseth","cesar"]
#ejemplo notas[3.5,4.8,3.2,2.8,3.5]
datos=["carlos",40,"20/05/2022","eduardo",45,85]
#podemos tener numeros,string,listas,booleanos.
#estructuras de datos=variable,listas,tuplas,dicionarios.
a=[23.56,59,12,-85]
vehiculos=["carro","moto","camioneta","barco"]
animales=["perro","gato","conejo"]
print(a)
print(2*animales)
print(vehiculos+animales)
print("*******************")
#join() se usa para agregar elementos para separar o entre los valores

subcadena=(" y ")
print(subcadena.join(vehiculos))

# append añadimos elementos al final de la lista
animales.append("caballo")
print(animales)

# insert --> añadimos elementos en una posicion especifica
animales.insert(0,"vaca")
print(animales)

animales.insert(5,"leon")
print(animales)

# extend --> puede añadir elementos a la lista pero de forma iterativa
animales.extend("lagartija")
print(animales)

#len --> contar la longitud de la lista

n=len(animales)
print(n)

#pop --> quita 1 elemento de la lista

print(vehiculos.pop(2))
vehiculos.pop(2)
#la otra formaabajo
print(vehiculos)

print("+******+")


# remove --> quita un elemento de la lista por el nombre

animales.remove("vaca")
print(animales)



