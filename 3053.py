NroC = int(input())
car=str(input())
for k in range(NroC):
	TipoMov = int(input())
	if(TipoMov==1):
		car="B"*(car=="A")+"A"*(car=="B")+"C"*(car=="C")
	elif(TipoMov==2):
		car="B"*(car=="C")+"C"*(car=="B")+"A"*(car=="A")
	else:
		car="A"*(car=="C")+"C"*(car=="A")+"B"*(car=="B")
print(car)