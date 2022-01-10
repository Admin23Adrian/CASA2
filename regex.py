import re

# Aprovada
regex_afiliado = r'([a-zA-Z]{2})|([0-9]{5,13})([/][0-9]{1,2})*'
# Aprovada
medicacion = r'([A-Z]+\s\d+)(\s[a-z]{1,2}|[A-Z]{1,3})(.[a-zA-Z0-9+ .]*)'
# Aprovada??
cantidad_medicacion = r'(n\d{1}\\)|(n\d{2}\\n)[^\\]'

