try:
	while(1):
		cont=1
		NroC = int(input())
		arr = [int(x) for x in input().split(" ")]
		if(sum(arr)%NroC!=0): print("-1")
		elif(sum(arr)/NroC==arr[0]): print(cont)
		else:
			prom = int(sum(arr)/NroC)
			while(len(arr)!=0):
				if(arr[0]==prom): 
					arr.pop(0)
				else:
					temp = prom-arr[0]
					arr[len(arr)-1] = arr[len(arr)-1]-temp
					arr.pop(0)
					arr.sort()
					cont+=temp
			print(cont)
except EOFError: exit()