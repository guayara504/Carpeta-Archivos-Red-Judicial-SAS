import msvcrt
from re import L
import shutil
import sys
import time
import os
from datetime import datetime
import pyexcel
import xlwt

class Excel_1:

    def __init__(self):
        self.fnametemp = "temp_" + time.strftime("%d%m%Y%H%M%S") + ".xls"   
    
    

    def crear_xls(self,wb):
        data = {'INPUT': ['CIUDAD', 'ENTIDAD/ESPECIALIDAD', 'RADICADO', 'EXITOSO'],
                'DATOS DEL PROCESO': ['FECHA CONSULTA', 'CIUDAD', 'ENTIDAD', 'RADICADO', 'DESPACHO', 'PONENTE', 'TIPO',
                                    'CLASE', 'RECURSO', 'UBICACION', 'DEMANDANTE(S)', 'CONTENIDO'],
                'ACTUACIONES DEL PROCESO': ['RADICADO', 'FECHA ACTUACION', 'ACTUACION', 'ANOTACION', 'FECHA INICIA TERMINO',
                                            'FECHA FIN TERMINO',
                                            'FECHA REGISTRO']}
        for key, nomHoja in enumerate(data):
            ws = wb.add_sheet(nomHoja)
            for clave, valor in enumerate(data[nomHoja]):
                ws.write(0, clave, valor)
        wb.save(self.fnametemp)

    def escribir_xls(self,datosPro, actosPro):
        wb = pyexcel.get_book(file_name=self.fnametemp)
        wb.sheet_by_name('INPUT').row += i
        wb.sheet_by_name('DATOS DEL PROCESO').row += datosPro
        for dats in actosPro:
            wb.sheet_by_name('ACTUACIONES DEL PROCESO').row += dats

        wb.save_as(self.fnametemp)
