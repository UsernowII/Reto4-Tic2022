#Jhon Erick Santos Gonzalez
#Mintic 2022 G46
#Reto 4 Nomina
#cesantias = {}
employee = []
valortotalhoras = []
H_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
valor_Hora = int(input("Ingrese el valor por hora: "))
name = input("Ingrese su nombre completo: ")
employee.append(name)

import nomina as fan

valortotalhoras = fan.valorHoras(H_trabajadas,valor_Hora)
sueldobruto = fan.defsueldoBruto(valortotalhoras)
des_para = fan.parfuncion(sueldobruto)
des_eps = fan.epsfuncion(sueldobruto)
des_pension = fan.penfuncion(sueldobruto)
totalDescuentos = des_eps + des_para + des_pension
primas = fan.primafuncion(sueldobruto)
cesantias = fan.cesantiasfuncion(sueldobruto)
intcesantias = fan.intCesfuncion(sueldobruto)
vacaciones = fan.vacfuncion(sueldobruto)
print(valortotalhoras[0])
print(valortotalhoras[1])
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