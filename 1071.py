Nro1 = int(input())
Nro2 = int(input())
suma = 0
if(Nro2 > Nro1):
	Nro1,Nro2 = Nro2,Nro1
Nro2+=1
while(Nro2 < Nro1):
	if(Nro2%2==1):
		suma += Nro2
	Nro2+=1
print(suma)