import win32com.client as win32
import pythoncom
import win32com.client
import time
from rutas import archivo_excel_trabajo
import openpyxl

excel = openpyxl.load_workbook(archivo_excel_trabajo)
hoja = excel["inicio"]


print()