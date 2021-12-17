import slate3k
import re
import openpyxl
import os

import rutas
import regex


# Funcion que va a pegar los datos al excel y los guarda. Parametro fl = (fila excel)
def excel(ruta_excel, afiliado, fl):
    print(f"\t\t# INTENTANDO ACCEDER AL EXCEL...")
    try:
        excel = openpyxl.load_workbook(ruta_excel)
        hoja = excel["inicio"]
        print(f"\t\t> Se accedio correctamente.")
        hoja[f"B{fl}"].value = afiliado
        if hoja[f"B{fl}"].value != None:
            print(f"El afiliado {afiliado} se pego correctamente al Excel.")
        else:
            print(f"El afiliado {afiliado} NO SE HA PODIDO PEGAR EN EL EXCEL. Se deja LOG.")
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
    print(lectura)
    regex_afiliado = r'(CASA\n\n)([0-9]+/[0-9]{1,2})'
    regex_medicacion = r"([A-Z]+\s\d+)(\s[a-z]{1,2}|[A-Z]{1,3})"

    # for a in re.findall(regex_afiliado, texto):
        # print(f"\t\tAFILIADO ---> {a[1]}")
        # afiliado = m[1]
        # if afiliado != None:
    #         print(f"\t\t> AFILIADO ENCONTRADO: {afiliado}")
    #         return afiliado
    #     else:
    #         print("\t\tNo se pudo encontrar el dato de afiliado dentro del pdf.")
    #         return
    # for m in re.findall(regex_medicacion, texto):
    #     print(f"\t\tMEDICACION ---> {m[0]} {m[1]}")


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
                afiliado = leer_pdf(os.path.join(rutas.carpeta_pdfs, pdf))

    except:
        print("***** Nada que listar en la carpeta de PDFS! *****")
