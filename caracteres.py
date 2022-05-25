
c = 0 
entrada =input("Escriba una cadena: ")

for x in entrada:
    if x in "01233456789":
        c+=1
print("cantidad de numeros",  c)