import slate3k


def leer_pdf(ruta_pdfs):
    archivo_pdf = "CASA1.pdf"

    with open(f"{ruta_pdfs}/{archivo_pdf}", "rb") as archivo:
        lectura = slate3k.PDF(archivo)
    
    print(lectura[0])

ruta = "C:\\Users\\aalarcon\\Desktop\\OyP\\CASA\\pdfs"
leer_pdf(ruta)