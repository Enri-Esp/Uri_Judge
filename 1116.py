NC = int(input())
for k in range(NC):
	X,Y = input().split()
	X = float(X)
	Y = float(Y)
	if(Y==0): print("divisao impossivel")
	else: print("{:.1f}".format(X/Y))