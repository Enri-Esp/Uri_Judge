cont = 0
rpta = 0
while(True):
	Nro = float(input())
	if(Nro<0 or Nro>10): print("nota invalida")
	else:
		cont+=1
		rpta+=Nro
	if(cont==2): 
		print("media = {:.2f}".format(rpta/2))
		rpta=0
		cont=0
		print("novo calculo (1-sim 2-nao)")
		op = int(input())
		while(op!=1 and op!=2):
			print("novo calculo (1-sim 2-nao)")
			op = int(input())
		if(op==2):
			break