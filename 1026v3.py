try:
	while(1):
		N1,N2=input().split()
		N1=int(N1)
		N2=int(N2)
		cont = 0
		suma = 0
		while(N1+N2!=0):
			temp = 1*(N1%2 != N2%2)
			suma += temp*(2**cont)
			cont += 1
			N1 = N1//2
			N2 = N2//2
		print(suma)
except EOFError: exit()