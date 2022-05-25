
A = float(input())
B = (A*2)+4
C = (A+B)//5
A = int(A)
B = int(B)
C = int(C)
print(A, B, C)
if C >= 0 and C <= 20:
    print('uno')
elif C >= 21 and C <= 40:
    print('dos')
elif C >= 41 and C <= 80:
    print('tres')
elif C >= 81:
    print('cuatro')
