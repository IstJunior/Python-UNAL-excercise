print("****************CALCULADORA**************")
print("Elija una opción")

print("1. suma\n2. resta\n3. Multiplicación\n4. División")

opcion = float(input("Seleccione una opción: "))

if opcion == 1:

    a = float(input("ingrese el primer numero a sumar: "))
    b = float(input("ingrese el segundo numero a sumar: "))
    operacion = a+b
    print("La suma de los numeros es", suma)
elif opcion == 2:
    a = float(input("ingrese el primer numero a restar: "))
    b = float(input("ingrese el segundo numero a restar: "))
    operacion = a-b
    print("La suma de los numeros es", operacion)
elif opcion == 3:
    a = float(input("ingrese el primer numero a multiplicar: "))
    b = float(input("ingrese el segundo numero a multiplicar: "))
    operacion = a*b
    print("La suma de los numeros es", operacion)
elif opcion == 4:
    a = float(input("ingrese el primer numero a dividir: "))
    b = float(input("ingrese el segundo numero a dividir: "))
    operacion = a/b
    print("La division de los numeros es", operacion)
else:
    print("Opcion no valida")
    

