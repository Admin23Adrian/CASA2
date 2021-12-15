import slate3k
import re
import openpyxl


def excel(ruta_excel, afiliado):
    try:
        excel = openpyxl.load_workbook(ruta_excel)
        hoja = excel["inicio"]
        hoja["B9"].value = str(afiliado)
    except:
        print("Ha ocurrido una excepcion.")
    finally:
        excel.save(ruta_excel)
        excel.close()


def leer_pdf(ruta_pdfs):
    # archivo_pdf = "LEGUIZAMON-SCIENZA.pdf"
    archivo_pdf = "NAIRN-SCIENZA.pdf"
    # archivo_pdf = "CASA1.pdf"

    with open(f"{ruta_pdfs}/{archivo_pdf}", "rb") as archivo:
        lectura = slate3k.PDF(archivo)
    
    texto = str(lectura[0])

    regex = r'(CASA\n\n)([0-9]+/[0-9]{1,2})'

    for m in re.findall(regex,texto):
      afiliado = m[1]
      print(afiliado)

    return afiliado


ruta = "C:\\Users\\aalarcon\\Desktop\\OyP\\CASA\\pdfs"
ruta_excel = "C:/Users/aalarcon/Desktop/OyP/CASA/eurosistemas.xlsx"

afiliado = leer_pdf(ruta)
excel(ruta_excel, afiliado)


