import re


ruta_txt = "Archivos/prueba_regex.txt"

with open(ruta_txt, "rt") as file:
     
     texto = file.read()

     print(texto)

     for t in re.findall(r'(\s[0-9]{1,2})', texto):
          print(t)