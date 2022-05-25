def evalua_notas(nota1, nota2, nota3, nota4):

    promedio = round((nota1+nota2+nota3+nota4)/4, 1)

    if promedio >= 3.0:
        estado = "Pasó"
    else:
        promedio = "No pasó"
    return estado
    
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
promedio = round((n1+n2+n3+n4)/4, 1)
resultado = evalua_notas(n1, n2, n3, n4)
print("El alumno", resultado, "la materia con un promedio de", promedio)


