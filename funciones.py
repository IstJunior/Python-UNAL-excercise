'''Funcion que calcula la potencia de un numero'''
def potencia(x):
    return x**2
n = potencia(5)
print("El cuadrado del numero", 5, "es", n)

'''Funcion que calcula el promedio de cuatro notas'''
def promedio(n1, n2, n3, n4):
    pro = (n1+n2+n3+n4)/4
    return pro

n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))
n4 = float(input("Nota 4:"))

prome = print(n1+n2+n3+n4/4)