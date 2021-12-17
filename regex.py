import re

regex_afiliado = r'([a-zA-Z]{2})|([0-9]{5,13})([/][0-9]{1,2})*'

producto = r'^Productos\n\n(([0-9]*\n\n[A-Z]+)|[A-Z]*)\s([0-9]+)'

## BUENA ##
medicacion = r'([A-Z]+\s\d+)(\s[a-z]{1,2}|[A-Z]{1,3})(.[a-zA-Z0-9+ .]*)'

modelo_medicacion_1 = r'([A-Z]*)(.[0-9A-Za-z /.+-]*)'

