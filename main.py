import slate3k
import re
import openpyxl
import os

import rutas
import regex

# Limpiar y unir los datos que vienen el tuplas.
def armar_descripcion_medicamento(lista):
    pass



# Funcion que limpia los caracteres "\n" del texto del pdf:
def limpiar_caracteres(texto_lista):
    if texto_lista != []:
        lista = texto_lista.split("\n")
        nueva_lista = [x for x in lista if x != '']
        return " ".join(nueva_lista)
    else:
        return False



# Pegar datos a Excel. Parametro fl = (fila excel)
def excel(ruta_excel, afiliado, medicacion, fl):
    print(f"\t\t# INTENTANDO ACCEDER AL EXCEL...")
    excel = openpyxl.load_workbook(ruta_excel)
    hoja = excel["inicio"]
    try:
        print(f"\t\t> Se accedio correctamente.")
        hoja[f"B{fl}"].value = afiliado
        hoja[f"C{fl}"].value = medicacion

        # Verificamos si el valor se pego correctamente en las celdas.
        if hoja[f"B{fl}"].value != None:
            print(f"\t\t> El afiliado {afiliado} se pego correctamente al Excel.")
        else:
            print(f"\t\t> El afiliado {afiliado} NO SE HA PODIDO PEGAR EN EL EXCEL. Se deja LOG.")
        
        if hoja[f"C{fl}"].value != None:
            print(f"\t\t> La medicacion {afiliado} se pego correctamente al Excel.")
        else:
            print(f"\t\t> La medicacion {afiliado} NO SE HA PODIDO PEGAR EN EL EXCEL. Se deja LOG.")
    except:
        print("Ha ocurrido una excepcion. Posiblemente hay un error con el EXCEL.")
    # Guardamos y cerramos el excel.
    finally:
        excel.save(ruta_excel)
        excel.close()



# Leer pdf y sacar medicacion
def leer_pdf(ruta_pdfs):

    # -- VARIABLES -- #
    juego_tuplas_medicamentos = []
    lista_afiliado = []
    

    # Usamos la libreria Slate3k para extraer el texto del pdf.
    with open(ruta_pdfs, "rb") as archivo:
        print(f"\t\t> Leyendo capa texto del pdf...")
        lectura = slate3k.PDF(archivo)  # Se devuelve el texto como un string dentro de una lista.  
    
    nuevo_texto = limpiar_caracteres(lectura[0])
    
    # == EXPRESIONES REGULARES == #
    regex_codigo_medicacion = r'(Productos\s)([0-9]*\s*)([A-Z]*\s*)([a-zA-Z0-9./+]*\s*)([(a-zA-Z0-9/+).+]*\s*)([(a-z0-9/+).+]*\s*)([a-z0-9./+ ]*)|(Observ:\s)([0-9]*\s*)([A-Z]*\s*)([a-zA-Z0-9.]*\s*)([(a-zA-Z).+]*\s*)([(a-zA-z0-9).+]*\s*)([a-z0-9+. ]*)'
    regex_afiliado = r'([0-9]{5,13})([\/]\d{1,2}\s)([A-Z, ]+)'
    

    try:
        # AFILIADO
        for a in re.findall(regex_afiliado, nuevo_texto):
            lista_afiliado.append(a)

        # MEDICACION y CANTIDADES
        for m in re.findall(regex_codigo_medicacion, nuevo_texto):
            juego_tuplas_medicamentos.append(m)
        
    
    except Exception as e:
        return e, ruta_pdfs
    
    # # Validamos afiliado y medicacion.
    if lista_afiliado != []:
        return lista_afiliado, 
    else:
        return False



# --- ARRANQUE DEL PROCESO PRINCIPAL --- #
if __name__ == "__main__":
    try:
        fila = 9
        # Se recorre la carpeta de los pdf y se envia la lectura.
        print(">>> Ingresando a la carpeta de PDFS.")
        for pdf in os.listdir(rutas.carpeta_pdfs):
            print("---------------------------------------------------")
            print("\tListando PDF:")
            if pdf.endswith(".pdf"):
                print(f"\t\t* {pdf}")
                # afiliado, medicacion = leer_pdf(os.path.join(rutas.carpeta_pdfs, pdf))
                leer_pdf(os.path.join(rutas.carpeta_pdfs, pdf))
                # excel(rutas.archivo_excel, afiliado, medicacion, fila)
                fila = fila + 1

    except Exception as e:
        print("***** Nada que listar en la carpeta de PDFS! *****")
        print(e)
