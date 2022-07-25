while(True):
	A,B=input().split()
	if((int(A)+int(B))==0):
		break
	else:
		X = [int(x) for x in input().split(" ")]
		Y = [int(y) for y in input().split(" ")]
		X=set(X)
		Y=set(Y)
		X1 = X-Y
		Y1= Y-X
		if(len(X1)>len(Y1)):
			print(len(Y1))
		else:
			print(len(X1))