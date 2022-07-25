T = True
cont = 0
val = 0
while(T):
	Nro = float(input())
	if(Nro>10 or Nro<0): print("nota invalida")
	else: 
		val += Nro
		cont+=1
	if(cont==2): T = False
print("media = {:.2f}".format(val/2))