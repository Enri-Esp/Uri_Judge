def sumArr(A,B,n):
	arr =[]
	B.reverse()
	for k in range(n):
		arr.append(A[k]+B[k])
	return sorted(arr)

while(True):
	NroNietos = int(input())
	if(NroNietos==0): break
	arrR = [int(x) for x in input().split(" ")]
	arrT = sumArr(arrR[:NroNietos],arrR[NroNietos:],NroNietos)
	arrT.reverse()
	print("{0} {1}".format(arrT[0],arrT[NroNietos-1]))