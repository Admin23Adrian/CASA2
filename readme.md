# FACTURACION AUTOMATICA CON LECTURA DE PDFS


POR FAVOR ACTUALIZAR LOS AVANZES DEL DESARROLLO EN ESTE ARCHIVO. ES IMPORTANTE A MODO DE ARMAR BUENAS PRACTICAS EN LOS DESARROLLOS.

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
2. Esta seria al expresion para extraer afiliados del pdf de CASA:
```
([a-zA-Z]{2})|([0-9]{5,13})([/][0-9]{1,2})*
```

# 17/12/2021
1. Ayer se avanzo con la expresion regular para extraer el nombre del medicamento del PDF.
2. Obtuvimos el listado de materiales disponibles que el cliente tiene a disposicion en sap.
3. La expresion regular construida hasta el momento para el medicamento:
 ```
 ([A-Z]+\s\d+)(\s[a-z]{1,2}|[A-Z]{1,3})
 ```

## 14/01/2022
1. La expresion regular anteriormente publicada no funcionaba del todo bien para encontrar todas las posiciones de medicacion dentro del pdf.
2. Paso a dejar la Regex con la que tuve resultado.
```
r'(Productos\s)([0-9]*\s*)([A-Z]*\s*)([a-zA-Z0-9./+]*\s*)([(a-zA-Z0-9/+).+]*\s*)([(a-z0-9/+).+]*\s*)([a-z0-9./+ ]*)|(Observ:\s)([0-9]*\s*)([A-Z]*\s*)([a-zA-Z0-9.]*\s*)([(a-zA-Z).+]*\s*)([(a-zA-z0-9).+]*\s*)([a-z0-9+. ]*)'
```