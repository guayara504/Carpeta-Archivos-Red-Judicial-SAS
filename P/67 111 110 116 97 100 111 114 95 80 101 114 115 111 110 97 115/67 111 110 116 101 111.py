from ast import Return
import msvcrt
import time
import os
from unicodedata import name
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector as sql
import glob,time

#ano= input("Ingrese año: ")
#mes= input("Ingrese mes: ")
#dia= input("Ingrese dia: ")
#os.system ("cls")
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

mes = dife_fecha()
dia = time.strftime("%d") 
ano = time.strftime("%Y")

ruta = f"\\\TRUENAS\RedjudicialN1\\Redjudicial_estados\\{ano}\\{mes}\\{dia}\\"
Guayara=".\\Documentos\\Guayara.txt"
Jose=".\\Documentos\\Jose.txt"
Nini=".\\Documentos\\Nini.txt"
Camila=".\\Documentos\\Camila.txt"
Alexis=".\\Documentos\\Alexis.txt"
Daniela=".\\Documentos\\Daniela.txt"
Stefany=".\\Documentos\\Stefany.txt"
Neyber=".\\Documentos\\Neyber.txt"
Diego=".\\Documentos\\Diego.txt"

digitadores = [Guayara,Jose,Nini,Camila,Alexis,Daniela,Stefany,Neyber,Diego]

def crear_carpetas():
    carpetaAno= ano
    try:
            os.mkdir(f'.\\Resultados\\{carpetaAno}')
    except:
            pass

    carpetaMes= mes
    try:
            os.mkdir(f'.\\Resultados\\{carpetaAno}\\{carpetaMes}')
    except:
            pass

    carpetaDia= dia
    try:
            os.mkdir(f'.\\Resultados\\{carpetaAno}\\{carpetaMes}\\{carpetaDia}')
    except:
            pass


def estados():
    Estados = []
    Nh = []
    for digitador in digitadores[:-1]:
            persona=[]
            with open(digitador,'r') as archivo:
                    for n in archivo.read().split("\n"):
                            persona.append(n)
            estados = 0
            nh = 0
            if digitador[:-4].split("\\")[2] == "Guayara" or digitador[:-4].split("\\")[2] == "Camila":
                    estados = 15

            for archivo in glob.glob(ruta+"\\**", recursive=True):
                    if (".pdf" in archivo or ".xls" in archivo or ".PDF" in archivo or ".XLS" in archivo):
                            for n in persona:
                                    if n in archivo:
                                            estados+=1
                    if (".PNG" in archivo or ".png" in archivo or ".jpg" in archivo or ".jpeg" in archivo or ".gif" 
                    in archivo or ".JPG" in archivo or ".JPEG"  in archivo or ".GIF" in archivo or ".BMP" in archivo or ".bmp" in archivo):
                            
                            for n in persona:
                                    if n in archivo:
                                            nh+=1
            Estados.append(estados)
            Nh.append(nh)
            print("-------------\n"+digitador[:-4].split("\\")[2]+": \nESTADOS: ",estados,"\nNO HUBOS: ",nh,"\n-------------\n")
    #Obtenemos la posicion de cada etiqueta en el eje de X
    x = np.arange(len(digitadores)-1)
    #tamaño de cada barra
    width = 0.35

    fig, ax = plt.subplots()

    #Generamos las barras para el conjunto de hombres
    rects1 = ax.bar(x - width/2, Estados, width, label='Estados')
    #Generamos las barras para el conjunto de mujeres
    rects2 = ax.bar(x + width/2, Nh, width, label='No hubo')

    #Añadimos las etiquetas de identificacion de valores en el grafico
    ax.set_ylabel('Cantidad')
    ax.set_title('Estados y No hubo')
    ax.set_xticks(x)
    ax.set_xticklabels(digitador[:-4].split("\\")[2] for digitador in digitadores[:-1])
    #Añadimos un legen() esto permite mmostrar con colores a que pertence cada valor.
    ax.legend()

    def autolabel(rects):
        """Funcion para agregar una etiqueta con el valor en cada barra"""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2),  # 2 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    #Añadimos las etiquetas para cada barra
    autolabel(rects1)
    autolabel(rects2)
    plt.tight_layout()
    nombreEstados = "Estados.png"
    plt.savefig(f'.\\Resultados\\{ano}\\{mes}\\{dia}\\{nombreEstados}')   
    #Mostramos la grafica con el metodo show()
    
def lineas():
    conexion = sql.connect(
                host = "192.168.0.19", 
                user = "jfsarmiento", 
                passwd = "Jfs_red07$14",
                database = "zortekv3")

    
    try: 
        cursor = conexion.cursor()
        conteo = []
        cursor.execute('SELECT digitador FROM z04_estado  WHERE digitador LIKE "%%" AND fecha_notificacion = CURDATE()')
        consulta  = [item[0] for item in cursor.fetchall()]
        for dig in digitadores:
                dig = dig[:-4].split("\\")[2]
                if dig == 'Guayara':
                        dig = 'Victor Guayara'
                if dig == 'Jose':
                        dig = 'Jose Sarmiento'
                if dig == 'Nini':
                        dig = 'Johana Madrid'
                if dig == 'Camila':
                        dig = 'Camila Riveros'
                if dig == 'Alexis':
                        dig = 'Alexis Abello'
                if dig == 'Daniela':
                        dig = 'Daniela Yusti'
                if dig == 'Stefany':
                        dig = 'Stefany Osorio'
                if dig == 'Diego':
                        dig = 'Diego Rosero'
                if dig == 'Neyber':
                        dig = 'Neyber Arciniegas'
                persona = consulta.count(dig)
                conteo.append(persona)
        print("--Lineas Digitadas extraidas con exito--")
    except:
            print("No Hubo conexion con la base de datos...")
    #Obtenemos la posicion de cada etiqueta en el eje de X
    x = np.arange(len(digitadores))
    #tamaño de cada barra
    width = 0.35
    fig,ax = plt.subplots()
    #Generamos las barras para el conjunto de hombres
    rects1 = ax.bar(x - width/12, conteo, width, label='Líneas')
    #Añadimos las etiquetas de identificacion de valores en el grafico
    ax.set_ylabel('Cantidad')
    ax.set_title('Líneas Digitadas')
    ax.set_xticks(x)
    ax.set_xticklabels(digitador[:-4].split("\\")[2] for digitador in digitadores)
    #Añadimos un legen() esto permite mmostrar con colores a que pertence cada valor.
    ax.legend()
    def autolabel(rects):
        """Funcion para agregar una etiqueta con el valor en cada barra"""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2),  # 2 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    #Añadimos las etiquetas para cada barra
    autolabel(rects1)
    plt.tight_layout()
    nombreLineas = "Lineas.png"
    plt.savefig(f'.\\Resultados\\{ano}\\{mes}\\{dia}\\{nombreLineas}')  
    #Mostramos la grafica con el metodo show()

if __name__ == "__main__":
    print("\n---------Red-Judicial---------\n")
    opcion = int(input("1. Ejecutar\n2. Cerrar\nOpcion: "))
    os.system ("cls")
    if opcion == 1:
        crear_carpetas()
        estados()
        lineas()
        print("\nPULSE UNA TECLA PARA CERRAR...")
        msvcrt.getch()
    else:
        print("\nPULSE UNA TECLA PARA CERRAR...")
        msvcrt.getch()       