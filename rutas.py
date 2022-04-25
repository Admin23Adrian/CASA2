import os
from getpass import getuser

#USUARIO LOCAL
usuario = getuser()

# --> obtenemos la ruta del directorio actual.
directorio_raiz = f"C:/Users/{usuario}/Desktop/CASA"

# --> Armamos la ruta del directorio de archivos.
directorio_archivos = directorio_raiz + "/" + "archivos"

# --> Armamos la ruta del Excel.
archivo_excel_trabajo = directorio_archivos + "/" + "casa.xlsx"
archivo_excel = directorio_archivos + "/" + "padre.xlsx"

# --> Ruta carpeta de pdfs.
# carpeta_pdfs = os.path.join(directorio_raiz, "pdfs")
carpeta_pdfs = os.path.join(directorio_raiz, "pdfs")



