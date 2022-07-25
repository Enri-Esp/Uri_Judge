NroC = int(input())
cont = 0
for k in range(NroC):
	L,V = input().split()
	cont += int(V)*(int(L)>int(V))
print(cont)