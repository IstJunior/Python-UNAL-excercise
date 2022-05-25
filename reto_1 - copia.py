peso_Chavo = 60
peso_Quico = peso_Chavo*2+4
peso_Nono = peso_Quico+peso_Chavo//5

print(peso_Chavo, peso_Quico, peso_Nono)

if peso_Nono >= 0 and peso_Nono  <= 20:
    print('Ñoño se encuentra en la Etapa uno') 
elif peso_Nono >= 21 and peso_Nono  <= 40:
    print('Ñoño se encuentra en la Etapa dos')
elif peso_Nono >= 41 and peso_Nono  <= 80:
    print('Ñoño se encuentra en la Etapa tres')    
elif peso_Nono >= 80:
    print('Ñoño se encuentra en la Etapa cuatro')  
    


