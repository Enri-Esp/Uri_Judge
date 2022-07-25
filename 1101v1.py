while(True):
	M,N = input().split()
	M = int(M)
	N = int(N)
	if(M<=0 or N<=0): break
	arrN = []
	suma = 0
	if(M-N>0): M,N = N,M
	for k in range(M,N+1):
		arrN.append(k)
		suma += k
	arrN.append("Sum="+str(suma))
	print(*arrN)