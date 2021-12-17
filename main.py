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
    finally:
        excel.save(ruta_excel)
        excel.close()


def leer_pdf(ruta_pdfs):
    with open(ruta_pdfs, "rb") as archivo:
        print(f"\t\t> Leyendo capa texto del pdf...")
        lectura = slate3k.PDF(archivo)
    
    texto = str(lectura[0])
    # print(lectura)
    regex_afiliado = r'(CASA\n\n)([0-9]+/[0-9]{1,2})'
    regex_medicacion = r'([A-Z]+\s\d+)(\s[a-z]{1,2}|[A-Z]{1,3})(.[a-zA-Z0-9+ .]*)'
    try:
        for a in re.findall(regex_afiliado, texto):
            afiliado = a[1]
            
        for m in re.findall(regex_medicacion, texto):
            medicacion = f"{m[0]} {m[1]} {m[2]}"

    except Exception as e:
        return e, ruta_pdfs
    
    if afiliado != None and medicacion != None:
        print(f"\t\t> AFILIADO ENCONTRADO: {afiliado}")
        print(f"\t\t> MEDICACION ENCONTRADA: {medicacion}")
        return afiliado, medicacion
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
