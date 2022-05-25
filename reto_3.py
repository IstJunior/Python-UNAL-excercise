cadena = input("")
lista = cadena.split()
element = lista[0]
lista_temp = []
count_dict = []

lista_temp.append(element)
i = 0
for el in lista:
    if(el != element):
        element = el
        lista_temp.append(element)
        count_dict.append(str(i))
        i = 1
    else:
        i += 1
count_dict.append(str(i))
print(' '.join(lista_temp))
print(' '.join(count_dict))