def valorHoras(ht,vh):
    valorHoras_normal = 0
    valorHoras_extra = 0
    if ht < 40:
        valorHoras_normal = ht * vh
    else:
        valorHoras_normal = 40 * vh
        valorHoras_extra = ((ht-40) )* (1.5*vh)
    return (valorHoras_normal,valorHoras_extra)
 
def defsueldoBruto(x):
    sueldoB = x[0] + x [1]
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
