while(1):
	NC = int(input())
	if(NC==0): break
	arr=[]
	t=2
	cont=0
	for i in range(NC):
		L,C,R = input().split()
		arrT=[int(L),int(C),int(R)]
		arr.append(arrT)
	for k in range(NC):
		A,B,C=arr[k][0],arr[k][1],arr[k][2]
		if(A+B+C==0): pass
		if(t==1):
			if(A==1):
				if(B==1):
					t=3
					cont+=2
				else:
					t=2
					cont+=1
		elif(t==2):
			if(B==1):
				cont+=1
				if(A==1): t=3
				if(C==1): t=1
		else:
			if(C==1):
				if(B==1):
					t=1
					cont+=2
				else:
					t=2
					cont+=1
	print(cont)