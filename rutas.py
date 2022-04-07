import os
from getpass import getuser

#USUARIO LOCAL
usuario = getuser()

# --> obtenemos la ruta del directorio actual.
# directorio_raiz = r"C:\Users\aalarcon\Documents\Clientes Carga Automatica\CASA"
directorio_raiz = r"\\192.168.1.32\Scienza_fs\Gerencia_Comercial\Administracion_Ventas\ventas\OTROS CONVENIOS\AUTOMATIZACION 2021\CASA"

# --> Armamos la ruta del directorio de archivos.
directorio_archivos = directorio_raiz + "/" + "ARCHIVOS"

# --> Armamos la ruta del Excel.
archivo_excel_trabajo = directorio_archivos + "/" + "casa.xlsx"
archivo_excel = directorio_archivos + "/" + "padre.xlsx"

# --> Ruta carpeta de pdfs.
# carpeta_pdfs = os.path.join(directorio_raiz, "pdfs")
carpeta_pdfs = os.path.join(directorio_raiz, "PDFS")



