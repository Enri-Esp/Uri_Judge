import math
while(True):
	N,B = input().split()
	N=int(N)
	B=int(B)
	if(N+B==0):
		break
	arr = [int(x) for x in input().split(" ")]
	arrtemp = range(1,N+1)
	temp = list(arrtemp)
	for k1 in range(B):
		for k2 in range(k1+1, B):
			val = abs(arr[k1]-arr[k2])
			if(val in temp):
				temp.remove(val)
	if(len(temp)==0):
		print("Y")
	else:
		print("N")