#Jhon Erick Santos Gonzalez
#Mintic 2022 G46
#Reto 4 Nomina
#cesantias = {}
#employee = []
#valortotalhoras = []
H_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
valor_Hora = int(input("Ingrese el valor por hora: "))
#name = input("Ingrese su nombre completo: ")
#employee.append(name)

#import nomina as fan
#print(fan.horasExtra(10))
"""
def valorHoras(ht,vh):
    valorHoras_normal = 0
    valorHoras_extra = 0
    if ht < 40:
        valorHoras_normal = ht * vh
    else:
        valorHoras_normal = 40 * vh
        valorHoras_extra = ((ht-40) )* (1.5*vh)
    return (valorHoras_normal,valorHoras_extra)"""
def vhn(a,b) :
    if a >40 :
        valorhoraNormal = (40 * b)
        return valorhoraNormal
    else:
        valorhoraNormal = (a * b)
        return valorhoraNormal

def vhe (a,b) :
  if a >40 :
    valorhoraextra = ((a - 40) * (1.5 * b))
    return valorhoraextra
  else:
    valorhoraextra= 0
    return valorhoraextra
 
def defsueldoBruto(a,b):
    sueldoB = a + b
    return sueldoB

def parfuncion(sueldoB):
    parafiscales = sueldoB * 0.09
    return parafiscales

def epsfuncion(sueldoB):
    eps = sueldoB * 0.04
    return eps

def penfuncion(sueldoB):
    pen = sueldoB * 0.04
    return pen

def primafuncion(sueldoB):
    prima = sueldoB * 0.0833
    return prima

def cesantiasfuncion(sueldoB):
    def intCes (cesantias): # funcion anidada 
        intCe = cesantias * 0.12 # calcula el int cesantias tomando las cesantias como base
        return intCe
    cesantias = sueldoB * 0.0833
    intereses = intCes(cesantias)
    return cesantias#interes se peuden retonar los interes a un diccionario
        
def intCesfuncion (sueldoB):
    int = sueldoB * 0.01
    return int

def vacfuncion (sueldoB):
    vac = sueldoB * 0.0417
    return vac

valorHoraExtra = vhe(H_trabajadas,valor_Hora)
valorHoranormal =vhn(H_trabajadas,valor_Hora)
sueldobruto = defsueldoBruto(valorHoranormal, valorHoraExtra)
des_para = parfuncion(sueldobruto)
des_eps = epsfuncion(sueldobruto)
des_pension = penfuncion(sueldobruto)
totalDescuentos = des_eps + des_para + des_pension
primas = primafuncion(sueldobruto)
cesantias = cesantiasfuncion(sueldobruto)
intcesantias = intCesfuncion(sueldobruto)
vacaciones = vacfuncion(sueldobruto)
print(valorHoranormal)
print(valorHoraExtra)
print(sueldobruto)
print(des_para)
print(des_eps)
print(des_pension)
print(totalDescuentos)
print(sueldobruto - totalDescuentos)
print(primas)
print(cesantias)
print(intcesantias)
print(vacaciones)