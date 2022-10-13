# Hacer el diagrama de flujo y el programa en python que lance un dado n veces y cuente e imprima cuantas veces aparecio cada cara
from random import random
import random
print("\n----------------------------------------------------")
print("---- Programa para contar las caras de un dado -----")
print("----------------------------------------------------")

#input
n=int(input("\n Ingrese la cantidad de veces a tirar el dado: "))

#processing
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0

for i in range(n):
    l=random.randint(1,6)
    if l==1:
        c1=c1+1
    elif l==2:
        c2=c2+1
    elif l==3:
        c3=c3+1
    elif l==4:
        c4=c4+1
    elif l==5:
        c5=c5+1
    elif l==6:
        c6=c6+1

#output
print("\nLa cara 1 aparecio: "+str(c1)+" veces")
print("La cara 2 aparecio: "+str(c2)+" veces")
print("La cara 3 aparecio: "+str(c3)+" veces")
print("La cara 4 aparecio: "+str(c4)+" veces")
print("La cara 5 aparecio: "+str(c5)+" veces")
print("La cara 6 aparecio: "+str(c6)+" veces")
print(" ")

