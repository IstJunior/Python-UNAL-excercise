def Productos(A): 
    ListaVaciaA = []
    for juguete in A:
        if juguete not in ListaVaciaA:
            ListaVaciaA.append(juguete)
    return(ListaVaciaA)
    
def Faltante (L, M, N): 
    Posicion = []
    for i in L:
        if M[i] == N:
            Posicion.append(i)
    return(Posicion)
    
def TeFaltan (L1, L2):
    LD =[]
    for juguete in L1:
        if juguete not in L2:
            LD.append(juguete)
    return(LD)


def Intercambiemos(L1,L2):
    SinRep_L1=0
    SinRep_L2=0
    for Juguete in L1:
        if Juguete not in L2:
            SinRep_L1+=1
            
    for Juguete in L2:
        if Juguete not in L1:
            SinRep_L2+=1
    return(min(SinRep_L1, SinRep_L2))

             