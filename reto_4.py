import json
Datos_Bebidas=input("")
Datos_Bebidas = json.loads(Datos_Bebidas)
Orden = input(" ")
Bebidas=Orden.split(" ")
Total_Orden=0
Bebidas_found=[]
for Bebida in Bebidas:
   Precio = Datos_Bebidas.get(Bebida)
   if (Precio is not None):
       Total_Orden += Precio
       Bebidas_found.append(Bebida)
print(Total_Orden)
print(" ".join(Bebidas_found))