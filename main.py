import slate3k
import re
import openpyxl
import os

import rutas
import regex


# Funcion que va a pegar los datos al excel y los guarda. Parametro fl = (fila excel)
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

# Funcion que se encarga de leer el texto del pdf y extraer afiliad y medicacion.
def leer_pdf(ruta_pdfs):

    # Usamos la libreria Slate3k para extraer el texto del pdf.
    with open(ruta_pdfs, "rb") as archivo:
        print(f"\t\t> Leyendo capa texto del pdf...")
        # Se devuelve el texto como un string dentro de una lista.
        lectura = slate3k.PDF(archivo)
    
    # Seleccionar el texto dentro de la lista
    texto = str(lectura[0])
    
    # Declaramos las expresiones para encontrar el AFILIADO y MEDICACION dentro del texto.
    regex_afiliado = r'(CASA\n\n)([0-9]+/[0-9]{1,2})'
    regex_medicacion = r'([A-Z]+\s\d+)(\s[a-z]{1,2}|[A-Z]{1,3})(.[a-zA-Z0-9+ .]*)'
    
    # Intentamos encontrar la expresion dentro del texto.
    try:
        # Buscamos afiliado.
        for a in re.findall(regex_afiliado, texto):
            # El resultado devuelto son dos tuplas(por tener dos grupos) y seleccionamos la del indice 1.
            afiliado = a[1]

        # Buscamos la medicacion.  
        for m in re.findall(regex_medicacion, texto):
            medicacion = f"{m[0]} {m[1]} {m[2]}"
    # Caso no se encuentre nada, devolvemos la ruta del pdf para saber con cual no se pudo extraer el texto.
    except Exception as e:
        return e, ruta_pdfs
    
    # Validamos afiliado y medicacion.
    if afiliado != None and medicacion != None:
        print(f"\t\t> AFILIADO ENCONTRADO: {afiliado}") # Mostramos que se encontro el afiliado
        print(f"\t\t> MEDICACION ENCONTRADA: {medicacion}") # Mostramos que se encontro la medicacion
        return afiliado, medicacion # Devolvemos los valores en la funcion.
    else:
        print("\t\tNo se pudo encontrar el dato de afiliado o el medicamento dentro del pdf.")
        return


# --- ARRANQUE DEL PROCESO PRINCIPAL --- 
if __name__ == "__main__":
    try:
        fila = 9
        # Se recorre la ca arpeta de los pdf y se envia la lectura.
        print(">>> Ingresando a la carpeta de PDFS.")
        for pdf in os.listdir(rutas.carpeta_pdfs):
            print("---------------------------------------------------")
            print("\tListando PDF:")
            if pdf.endswith(".pdf"):
                print(f"\t\t* {pdf}")
                afiliado, medicacion = leer_pdf(os.path.join(rutas.carpeta_pdfs, pdf))
                excel(rutas.archivo_excel, afiliado, medicacion, fila)
                fila = fila + 1

    except Exception as e:
        print("***** Nada que listar en la carpeta de PDFS! *****")
        print(e)
