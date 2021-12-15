import os
from getpass import getuser

# --> obtenemos la ruta del directorio actual.
directorio_raiz = os.getcwd()

# --> Armamos la ruta del directorio de archivos.
directorio_archivos = os.path.join(directorio_raiz, "Archivos")

# --> Armamos la ruta del Excel.
archivo_excel = os.path.join(directorio_raiz, "casa.xlsx")

# --> Ruta carpeta de pdfs.
carpeta_pdfs = os.path.join(directorio_raiz, "pdfs")