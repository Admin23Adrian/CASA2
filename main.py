import slate3k #La libreria para sacar la capa texto.
import re
import openpyxl
import os
import time
import rutas #importacion de modulo donde defino las rutas.
import regex



# Limpiar y unir los datos que vienen el tuplas.
def limpiar_grupos(lista_medicacion):
    """LA FUNCION SE ENCARGA DE LIMPIAR Y ARMAR LAS LISTAS FINALES DE CANTIDADES
    Y DE CADA POSICION DE MATERIAL"""
    lista = []
    cantidades = []
    lista_final_cantidades = []
    lista_codigo_troquel = []

    
    # DESARMAR TUPLAS Y ARMAR LISTAS PARA PODER MODIFICARLAS Y LIMPIAR LOS ESPACIOS EN BLANCO.
    k = 1
    for grupo in lista_medicacion:
        palabras = []
        if k < len(lista_medicacion):
            for elem in grupo:
                if elem != "" and elem != "Productos " and elem != "Observ: ":
                    palabras.append(elem.rstrip())
            lista.append(palabras)
            # print(palabras)
            
        # Por este camino entraria si es el ultimo grupo (grupo de cantidades)
        else:
            for cant in grupo:
                if cant != "" and cant != "Productos " and cant != "Observ: ":
                    palabras.append(cant.rstrip())
            cantidades.append(palabras)
            
        k = k + 1

    # MANIPULAR LAS LISTAS
    for el in cantidades[0]:
        nuevo_el = el.split(' ')
        lista_final_cantidades = lista_final_cantidades + nuevo_el
    
    # ELIMINAMOS CADENAS EN LA ULTIMA POSIC DE LA LISTA DE CANTIDADES.
    cadena_en_cantidades = lista_final_cantidades[-1]
    try:
        int(cadena_en_cantidades)
    except:
        lista_final_cantidades.pop(lista_final_cantidades.index(cadena_en_cantidades))
    
    # EXTRAER CODIGO DE TROQUEL SI EXISTIESE Y MOSTRAR RESULTADO FINAL
    for t in range(len(lista)):
        codigo_troquel = lista[t][0]
        try:
            lista_codigo_troquel.append(int(codigo_troquel))
            lista[t].pop(lista[t].index(codigo_troquel))
        except:
            lista_codigo_troquel.append(999999)
        finally:
            print(f"MEDICACION: {' '.join(lista[t])} | CANTIDAD: {lista_final_cantidades[t]} | CODIGO TROQUEL: {lista_codigo_troquel[t]}")

    return lista, lista_final_cantidades, lista_codigo_troquel



# Funcion que limpia los caracteres "\n" del texto del pdf:
def limpiar_caracteres(texto_lista):
    if texto_lista != []:
        lista = texto_lista.split("\n")
        nueva_lista = [x for x in lista if x != '']
        return " ".join(nueva_lista)
    else:
        return False



# Pegar datos a Excel. Parametro fl = (fila excel)
def excel(ruta_excel, afiliado, medicacion_lista, cantidades, fl):
    print(f"\t\t# INTENTANDO ACCEDER AL EXCEL...")
    excel = openpyxl.load_workbook(ruta_excel)
    hoja = excel["inicio"]
    codigo_afiliado = afiliado[0][0] + afiliado[0][1]
    
    try:
        print(f"\t\t> Se accedio correctamente.")
        posic = 0
        for i in range(len(medicacion_lista)):
            posic = posic + fl
            hoja[f"B{posic}"].value = codigo_afiliado
            hoja[f"C{posic}"].value = medicacion_lista[i]
            hoja[f"D{posic}"].value = cantidades[i]

        # # Verificamos si el valor se pego correctamente en las celdas.
        # if hoja[f"B{fl}"].value != None:
        #     print(f"\t\t> El afiliado {afiliado} se pego correctamente al Excel.")
        # else:
        #     print(f"\t\t> El afiliado {afiliado} NO SE HA PODIDO PEGAR EN EL EXCEL. Se deja LOG.")
        
        # if hoja[f"C{fl}"].value != None:
        #     print(f"\t\t> La medicacion {afiliado} se pego correctamente al Excel.")
        # else:
        #     print(f"\t\t> La medicacion {afiliado} NO SE HA PODIDO PEGAR EN EL EXCEL. Se deja LOG.")
    except:
        print("Ha ocurrido una excepcion. Posiblemente hay un error con el EXCEL.")
    # Guardamos y cerramos el excel.
    finally:
        excel.save(ruta_excel)
        excel.close()

    return posic


# Leer pdf y sacar medicacion
def leer_pdf(ruta_pdfs):

    # -- VARIABLES - LISTAS -- #
    juego_tuplas_medicamentos = []
    lista_afiliado = []
    cantidades = []
    

    # Usamos la libreria Slate3k para extraer el texto del pdf.
    with open(ruta_pdfs, "rb") as archivo:
        print(f"\t\t> Leyendo capa texto del pdf...")
        lectura = slate3k.PDF(archivo)  # Se devuelve el texto como un string dentro de una lista.  
    
    nuevo_texto = limpiar_caracteres(lectura[0])
    print(nuevo_texto)
    
    # == EXPRESIONES REGULARES == #
    regex_codigo_medicacion = r'(Productos\s)([0-9]*\s*)([A-Z]*\s*)([a-zA-Z0-9./+]*\s*)([(a-zA-Z0-9/+).+]*\s*)([(a-z0-9/+).+]*\s*)([a-z0-9./+ ]*)|(Observ:\s)([0-9]*\s*)([A-Z]*\s*)([a-zA-Z0-9.]*\s*)([(a-zA-Z).+]*\s*)([(a-zA-z0-9).+]*\s*)([a-z0-9 +.]*)'
    regex_afiliado = r'([0-9]{5,13})([\/]\d{1,2}\s)([A-Z, ]+)'
    regex_cantidades = r'Observ:\s([0-9]+\s)*'
    
    try:
        # AFILIADO
        for a in re.findall(regex_afiliado, nuevo_texto):
            lista_afiliado.append(a)

        # MEDICACION
        for m in re.findall(regex_codigo_medicacion, nuevo_texto):
            juego_tuplas_medicamentos.append(m)

        print(re.findall('(Observ: )([0-9])*\s', nuevo_texto))
        
        # for c in re.findall(r'(Observ: )([0-9])*\s', nuevo_texto):
        #     cantidades.append(c)
        # print(f"{cantidades}")

    except Exception as e:
        return False, False
    
    # # Validamos afiliado y medicacion.
    if lista_afiliado != []:
        return lista_afiliado, juego_tuplas_medicamentos
    else:
        return False, False



# --- ARRANQUE DEL PROCESO PRINCIPAL --- #
if __name__ == "__main__":
    try:
        f = 9
        # Se recorre la carpeta de los pdf y se envia la lectura.
        print(">>> Ingresando a la carpeta de PDFS.")
        for pdf in os.listdir(rutas.carpeta_pdfs):
            print("---------------------------------------------------")
            print("\tListando PDF:")
            if pdf.endswith(".pdf"):
                print(f"\t\t* {pdf}")
                lista_afiliado, lista_tuplas_medicacion = leer_pdf(os.path.join(rutas.carpeta_pdfs, pdf))
                print()
                # print(lista_tuplas_medicacion)
                
                
                # if lista_afiliado != False and lista_tuplas_medicacion != False:
                    
                #     cantidades_limpias, materiales_limpios, codigos_troqueles = limpiar_grupos(lista_tuplas_medicacion)
                #     # fila = excel(rutas.archivo_excel, lista_afiliado, materiales_limpios, cantidades_limpias, f)
                # else:
                #     print(f"\t\t No se pudo encontrar medicacion para el PDF {pdf}")
                #     # f = f + 1
                # # fila = fila + 1

    except Exception as e:
        print("***** Nada que listar en la carpeta de PDFS! *****")
        print(e)
