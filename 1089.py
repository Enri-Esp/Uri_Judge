while(True):
	N = int(input())
	if(N == 0):
		break
	arr = [int(x) for x in input().split(" ")]
	print(arr)
	cont = 2
	del arr[0]
	print(arr)
	print("len ",len(arr))
	for k in range(len(arr)-1):
		if(arr[k]>(arr[k]-arr[k+1])):
			cont+=1
	print(cont)