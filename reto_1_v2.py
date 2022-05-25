'''Se recibe el valor de la variable A'''
A = float(input('Ingrese la cantidad en gramos (g):'))
B = (A*2)+4
C = A+B//5
'''Se convierte el valor flot a entero'''
A = int(A)
B = int(B)
C = int(C)
'''Se muestran los valores de A, B y C'''
print(A, B, C)
'''Se verifica el valor de C y se muestra el grupo al que pertenece el brebaje'''
if C >= 0 and C <= 20:
    print('El brebaje de tipo uno')
elif C >= 21 and C <= 40:
    print('El brebaje de tipo dos')
elif C >= 41 and C <= 80:
    print('El brebaje de tipo tres')
elif C >= 81:
    print('El brebaje de tipo cuatro')

