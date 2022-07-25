while(True):
	X,Y = input().split()
	X = int(X)
	Y = int(Y)
	if(X==Y): break
	print("Decrescente"*(X>Y)+"Crescente"*(X<Y))