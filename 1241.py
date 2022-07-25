NC = int(input())
for k in range(NC):
	Nro1, Nro2 = input().split()
	Long1 = len(Nro1)
	Long2 = len(Nro2)
	if(Long1>=Long2):
		if(Nro2 == Nro1[Long1-Long2:]):
			print('encaixa')
		else: print('nao encaixa')
	else: print('nao encaixa')

