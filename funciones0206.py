#una fucnion que me halle el area de un circulo solictando un diametro
"""
def area (radio):
    pi = 3.1416
    area = pi * radio**2
    return area

diametro = float(input("Ingrese el diametro del circulo"))
radio = diametro / 2
print(area(radio))
"""
#arreglos vectoriales y matriciales
#Realizar un programa en Phyton que teniendo una lista de números en el programa principal llame tres funciones: 
#1. que arroje el mayor valor de la lista
#2. que arroje el menor valor de la lista
#3. que arroje el promedio de los valores de la lista
#4. que escriba la lista ordenada


def promediolista(numbers):
    i=0
    sumaele=0
    for number in numbers :
        i +=1
        sumaele = sumaele+number
        prome = sumaele/i
        return prome

def mayorlista(lista):
    mayor = lista[0]
    for x in lista :
        if x > mayor:
            mayor = x
    return mayor

def menorlista(lista):
    menor = lista[0]
    for x in lista :
        if x < menor :
            menor = x
    return menor


#programa prinicipal
numbers = list(range(1,10))
x = int(input("digite un numero"))
i = 0
while x !=0 :
    numbers.append(x)
    x = int(input("digite un numero <0 para terminar>"))
prom = promediolista(numbers)
may = mayorlista(numbers)
men = menorlista(numbers)
print(numbers)
print("Promedio = ", prom)
print("Mayor =", may)
print("menor", men)
print(numbers.sort())

print(numbers)