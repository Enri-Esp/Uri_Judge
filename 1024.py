N = int(input())
abc = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
for k in range(N):
	cad1 = str(input())
	cad = list(cad1)
	T = len(cad)
	for i in range(T):
		if(cad[i] in abc):
			cad[i] = str(chr(ord(cad[i])+3))
	cad.reverse()
	mit = int((T - (T%2))/2 - 1)
	for j in range(mit+1, T):
		if(cad[j] != " "):
			cad[j] = str(chr(ord(cad[j])-1))
	print("".join(cad))