Dic = {0:"A",1:"B",2:"C",3:"D",4:"E"}
while(True):
	N = int(input())
	if(N==0):
		break
	for k in range(N):
		arr = [int(x) for x in input().split(" ")]
		arr1 = [x for x in arr if(x in range(0,128))]
		if(len(arr1)==1):
			print(Dic[arr.index(arr1[0])])
		else:
			print("*")