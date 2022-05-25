def maximo(a, b, c)

""" a = float(input("INGRESE UN NUMERO: "))
b = float(input("INGRESE OTRO NUMERO: "))
c = float(input("INGRESE OTRO NUMERO: ")) """


if (a > b) and (a > c):
    mayor = a
elif (b > a) and (b > c):
    mayor = b
elif (c > a)and(c > b):
    mayor = c
    return  mayor