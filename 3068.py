case=1
while(1):
	cont=0 
	X1,Y2,X2,Y1 = input().split()
	X1=int(X1)
	Y1=int(Y1)
	X2=int(X2)
	Y2=int(Y2)
	if(X1+X2+Y2+X1==0): break
	NroMet = int(input())
	for i in range(NroMet):
		X,Y = input().split()
		X=int(X)
		Y=int(Y)
		if(X1<=X<=X2 and Y1<=Y<=Y2): cont+=1
	print("Teste {}".format(case))
	print(cont)
	case+=1