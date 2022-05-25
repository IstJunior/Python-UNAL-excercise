string1=input("")
string2=input("")
invitados=input("")
j1 = 0
j2 = 0
for c in invitados:   
  if c in string1:
    j1 += 1
  if c in string2:
    j2 += 1
  if j1 > j2:
    print("1",end="")
  if j1 < j2:
    print("2",end="")
  if j1 == j2:
    print("*",end="")