# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cCCsTVGCNZkJJXP4P_OflYW8DeJD0yi9
"""

#realizar un programa en Phyton que lea un valor entero (que representa el diametro de un círculo), el programa debe calcular
#el área del círculo a través de una función, y escribir dicho resultado en el programa principal.
def area_circulo(rr) :
  pi = 3.1416
  ac = pi*r*r
  return ac

#iniciar Programa principal
d = int(input("Digite el diametro del círculo: "))
r = d/2
ac = area_circulo(r)
print("El círculo de radio ", r, "cms tiene un área = ", ac, "cms")
print("Fin")

#Arreglos Vectoriales y Matriciales
#Ejemplo de  un vector EQ. una Lista
def Promedio_edad(listaedad) :
  se = 0
  ce = 0
  prom = 0
  for k in listaedad :
    se = se + k
    ce = ce+1
  prom = se/ce
  return prom

#programa principal
edades = [15,23,18,35,42,12,21]
#Imprimir la lista de edades
for k in edades :
  print(k)
#print(edades)
prmedad = Promedio_edad(edades)
print("Edad promedio = ", prmedad)

#Realizar un programa en Phyton que teniendo una lista de números en el programa principal llame tres funciones: 
#1. que arroje el mayor valor de la lista
#2. que arroje el menor valor de la lista
#3. que arroje el promedio de los valores de la lista
#4. que escriba la lista ordenada
def promediolista(lista) :
  ce = 0
  se = 0
  pe = 0
  for k in lista :
    ce = ce+1
    se = se+k
  pe = se/ce
  return pe

def mayorlista(lista) :
  return max(lista)

def menorlista(lista) :
  menor = lista[0]
  for x in lista :
    if x < menor :
      menor = x
  return menor


#Programa principal
listanum =[]
x = int(input("digite un número <Para terminar 0>: "))
while x != 0 :
  listanum.append(x)
  x = int(input("digite un número <Para terminar 0): "))
prom = promediolista(listanum)
may = mayorlista(listanum)
men = menorlista(listanum)
print("Lista Original: ")
print(listanum)
print("Promedio = ", prom)
print("Mayor = ", may)
print("Menor = ", men)
print("lista Ordenada: ")
print(sorted(listanum))

L=['hola',"Carlos","Jose", "Adriana"]
print(L)
print(sorted(L))
print(len(L))

#Reto 3: 
Tmi = int(input("Digite Temperatura Mínima del día <0 para terminar>: "))
Tma = int(input("Digite Temperatura Máxima del dia <0 para terminar>: "))
cd = 0
cdc = 0
cmie = 0
cmae = 0
cmamie = 0
ttmi = 0
ttma = 0
while Tmi != 0 and Tma != 0 :
  cd = cd+1
  if Tmi >= 5 and Tma < 36 :
    cdc = cdc+1
    ttmi = ttmi+Tmi 
    ttma = ttma+Tma
  if Tmi < 5 :
    cmie = cmie+1
  if Tma > 35 :
    cmae = cmae+1
  if Tmi<5 and Tma>35 :
    cmamie = cmamie+1
  Tmi = int(input("Digite Temperatura Mínima del día <0 para terminar>: "))
  Tma = int(input("Digite Temperatura Máxima del dia <0 para terminar>: "))
print("Resultados: ")
print("Total días salida: ", cd)
print("Total días Registro Correcto: ",cdc)
print("Promedio Temperatura Mínima: ", ttmi/cdc)
print("Promedio Temperatura Máxima: ", ttma/cdc)
print("Diars registrados con temperatura mínima erronea: ", cmie)
print("Dias registrados con temeperatira máxima erronea: ", cmae)

Nom = input("Digite Nombre: ")
print(Nom)
Empresa = "Esta es una empresa de cadena"
print(Empresa)
apellido = str(input("Digite Apellido: "))
print(apellido)