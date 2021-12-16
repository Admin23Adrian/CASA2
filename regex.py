import re

regex_afiliado = r'([a-zA-Z]{2})|([0-9]{5,13})([/][0-9]{1,2})*'

producto = r'^Productos\n\n(([0-9]*\n\n[A-Z]+)|[A-Z]*)\s([0-9]+)'

medicacion = r'[A-Z]+\s\d+(\s[a-z]+|[A-Z]+)'

