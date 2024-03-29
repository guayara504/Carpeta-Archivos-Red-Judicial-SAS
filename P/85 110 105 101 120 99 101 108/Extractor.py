from UnixExcel import *
import msvcrt
from re import L
import shutil
import sys
import time
import os
from datetime import datetime
from webbrowser import Chrome
import pyexcel
import xlwt
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Consultor import *
from Driver import *

class Extractor_1(object):
    
    #Extrae los datos del proceso
    def extraer_datos(datos,driver):
        WebDriverWait(driver,timeout=4).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/div/tr/th/tr[1]/th')))
        datos["fecha"] = (driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/div/tr/th[1]/tr[1]/td').text)
        datos["despacho"] = (driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/div/tr/th/tr[2]/td').text)
        datos["ponente"] = (driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/div/tr/th/tr[3]/td').text)
        datos["tipo_proceso"] = (driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/div/tr/th/tr[4]/td').text)
        datos["clase_proceso"] = (driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/div/tr/th/tr[5]/td').text)
    
    #Extrae las partes del proceso
    def extraer_partes(datos,driver):
        driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[3]').click()
        WebDriverWait(driver,timeout=4).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[2]')))
        datos["demandante"] = (driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]').text)
        datos["demandado"] = (driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[2]').text)    
    
    #Extrae las actuaciones del proceso
    def extraer_actuaciones(actuaciones,driver):
        driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div[5]').click()
        WebDriverWait(driver,timeout=2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[1]/div[2]/div/table/tbody')))
        table_actos = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[1]/div[2]/div/table/tbody')
       
        allrows = table_actos.find_elements(By.TAG_NAME,"tr")[:]
        for tr in allrows:
            lista_td = []
            allcols = tr.find_elements(By.TAG_NAME,"td")[:3]
            for j in range(len(allcols)):
                lista_td.append(allcols[j].text)
            actuaciones.append(lista_td)
        