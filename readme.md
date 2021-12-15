# ******************************************************************* #
#             FACTURACION AUTOMATICA CON LECTURA DE PDFS              #
# ******************************************************************* #

# POR FAVOR ACTUALIZAR LOS AVANZES DEL DESARROLLO EN ESTE ARCHIVO. ES IMPORTANTE A MODO DE ARMAR BUENAS PRACTICAS EN LOS DESARROLLOS.


## 13/12/2021
1. Buscamos opciones sobre como leer pdfs ya que con PyPDF2 no tuvimos resultados.
2. Encontramos una libreria llamada Slate3k que permite la lectura de texto en un archivo pdf.
3. La idea es adaptar el desarrollo de Eurosistemas con este desarrollo para poder facturar 
   mediante la lectura automatica de los archivos pdf que pasan los clientes.
4. Se deja el Script en Asana.

## 14/12/2021
1. Vimos con Facu que podemos extraer con expresiones regulares el numero externo de afiliado
2. Pudimos capturarlo y pintarlo en el excel.
3. Nos queda sacar el nombre del producto/medicamento del mismo pdf.

## 15/12/2021
1. Dejo la pagina que usamos para armar las expresiones regulares [Regex101](https://regex101.com/)