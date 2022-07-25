contI = 0
contG = 0
contEm = 0
contPar = 0
while(True):
	I,G = input().split()
	I = int(I)
	G = int(G)
	if(I>G): contI+=1
	elif(I<G): contG+=1
	else: contEm+=1
	contPar+=1
	print("Novo grenal (1-sim 2-nao)")
	op = int(input())
	if(op==2): break
print("{} grenais".format(contPar))
print("Inter:{}".format(contI))
print("Gremio:{}".format(contG))
print("Empates:{}".format(contEm))
print("Inter venceu mais"*(contI>contG)+"Gremio venceu mais"*(contI<contG)
	+"Não houve vencedor"*(contG==contI))