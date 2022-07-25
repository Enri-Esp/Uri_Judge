while(True):
	A,C = input().split()
	if(int(A)+int(C)==0):
		break
	arr = [int(x) for x in input().split(" ")]
	cont = 0
	for k in range(1,int(A)+1):
		cont += arr.count(k)
	print(cont)