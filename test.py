lista = ['1', '9', '2', '7', '4 7', "RICARDO"]
# print(f"Lista Original: {lista}")

lista_n = []

for e in lista:
     el = e.split(' ')
     lista_n = lista_n + el

# print(f"Lista Modificada: {lista_n}")

for el in lista_n:
     try:
          int(el)
     except:
          pos = lista_n.index(el)
          lista_n.pop(pos)

# print(lista_n)


def ejemplo(n):
     if n == 5:
          return [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]
     else:
          return False

result = ejemplo(4)

if result != False:
     print("OK")
else:
     print()
