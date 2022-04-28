from Consultor import *
from Driver import *
from Extractor import *
from Excel import *

#Clase principal   
if __name__ == "__main__":
    browser =Driver_1()
    consulta =Consultor_1
    extractor = Extractor_1
    actuaciones = []
    datos = {"fecha": "","despacho":"","ponente":"","tipo_proceso":"","clase_proceso":"","demandante":"","demandado":""}
    wout = xlwt.Workbook()
    Excel_1.crear_xls(wout)
    consulta.iniciar_busqueda((browser.driver))
    consulta.ingresar_radicado((browser.driver))
    consulta.click_Proceso((browser.driver))
    extractor.extraer_datos(datos,(browser.driver))
    extractor.extraer_partes(datos,(browser.driver))
    extractor.extraer_actuaciones(actuaciones,(browser.driver))
    
    for dato in datos:
        print(dato+":",datos[dato])
    for act in actuaciones:
        print(act)
    
