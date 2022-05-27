#hacer un programa que solicite al usuario que ingrese numeros
#los cuales se bene guardar en una lista.
#finalizar al ingresar el numero 0, el cual no debe guardarse
def sumatoria(lista):
    suma=0
    for i in lista:
        suma=suma+i
    return suma
def numerosMenores(lista,limite):
    nueva=[]
    for j in lista:
        if j <limite:
            nueva.append(n)
        return nueva
numeros=[]
num=int(input("digite un numero: "))
while num!=0:
    numeros.append(num)
    num=int(input("digite otro numero: "))
print(numeros)
print(sorted(numeros))


#a continuacion, solicitar al usuario que ingrese un numero y si el numero esta en la lista
#eliminar su primera ocurrencia. mostrar si no es posible eliminar.

eliminar=int(input("digite numero a eliminar"))
if eliminar in numeros:
    numeros.remove(eliminar)
    print(numeros)
else:
    print("ese numero no esta en la lista")
    print(numeros)
    #imprimir la sumatoria de todos los numeros de la lista
print("-----------------------------------------")
   
print("la sumatoria de los numeros es: ", sumatoria(numeros))
print("++++++++++++++++++++++++++++++")
a=len(numeros)
print("la cantida de elementos de la lista es: ", a)


#solicitar al usuariootro numero y crear una lista con los elementos de la lista original
# que sean menores que el numero digitado. imprimir estanueva lista, iterando por ella

limite=int(input("filtrar numenores menores a: "))
for i in numerosMenores(numeros,limite):
    print(i)
