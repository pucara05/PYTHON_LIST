#hacer un programa que solicite al usuario que ingrese numeros
#los cuales se bene guardar en una lista.
#finalizar al ingresar el numero 0, el cual no debe guardarse

numeros=[]
num=int(input("digite un numero: "))
while num!=0:
    numeros.append(num)
    num=int(input("digite otro numero: "))
print(numeros)
