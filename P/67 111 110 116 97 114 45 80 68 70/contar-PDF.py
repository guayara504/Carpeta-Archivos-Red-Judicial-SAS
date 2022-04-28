import glob,time,msvcrt,operator
from multiprocessing import Condition
from collections import Counter
import os
import time

a = "YA.pdf"
b = "ya.pdf"
c = ".pdf"
d = ".xls"
e = ".XLS"
f = ".PDF"
g = "YA.xls"
h = "ya.xls"
i = "ya.XLS"
j = "YA.XLS"
k = "ya.PDF"
l = "YA.PDF"
m = "Envío Correos"

def dife_fecha():
    mes= time.strftime("%m")    
    if mes == '01':
        mes = 'ENERO'
    if mes == '02':
        mes = 'FEBRERO'
    if mes == '03':
        mes = 'MARZO'
    if mes == '04':
        mes = 'ABRIL'
    if mes == '05':
        mes = 'MAYO'
    if mes == '06':
        mes = 'JUNIO'
    if mes == '07':
        mes = 'JULIO'
    if mes == '08':
        mes = 'AGOSTO'
    if mes == '09':
        mes = 'SEPTIEMBRE'
    if mes == '10':
        mes = 'OCTUBRE'
    if mes == '11':
        mes = 'NOVIEMBRE'
    if mes == '12':
        mes = 'DICIEMBRE'
    return mes

condicion = 1

while condicion == 1:

    ubicacion = int(input("\n1.Dia\n2.Ubicacion Personalizada\n3.Hoy\nIngrese: "))

    if ubicacion == 1:
        ano= input("Ingrese año: ")
        mes= input("Ingrese mes: ")
        dia= input("Ingrese dia: ")
        ruta = "\\\TRUENAS\\RedjudicialN1\\Redjudicial_estados\\"+ano+"\\"+mes+"\\"+dia+"\\"

    elif ubicacion == 2:
        ruta = input("Ingrese la ruta: ")

    elif ubicacion == 3:
        mes = dife_fecha()
        dia = time.strftime("%d") 
        ano = time.strftime("%Y")
        ruta = "\\\TRUENAS\\RedjudicialN1\\Redjudicial_estados\\"+ano+"\\"+mes+"\\"+dia+"\\"
        
    total=0
    departamentos = []


    print("----------------------\nESTADOS\n----------------------")


    for archivo in glob.glob(ruta+"\\**", recursive=True):
        if (a not in archivo and b not in archivo and g not in archivo and h not in archivo and i not in archivo 
            and j not in archivo and k not in archivo and l not in archivo and m not in archivo 
            and(c in archivo or d in archivo or e in archivo or f in archivo)):
            print(archivo[49:])
            departamentos.append(archivo.split("\\")[8])
            total+=1
            
    conteo=Counter(departamentos)

    print("\n----------------------\nARCHIVOS RESTANTES \n----------------------")
    resultado={}
    for clave in conteo:  
        valor=conteo[clave]
        if valor != 0:
            resultado[clave] = valor

    resultado_sort = dict(sorted(resultado.items(),key=operator.itemgetter(1),reverse=True))

    for result in resultado_sort:
        print(result+":",resultado_sort[result])

    print("\n----------------------\nTOTAL:",total,"\n----------------------")
    condicion =int(input("\n1.Reiniciar\n2.Cerrar\nIngrese: "))
    os.system ("cls")


print("\nPULSE UNA TECLA PARA CERRAR...")
msvcrt.getch()
