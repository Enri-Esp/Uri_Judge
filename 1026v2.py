def BinaInt(arr):
	arr.reverse()
	Sum=0
	for k in range(len(arr)):
		Sum = Sum + int(arr[k])*(2**k)
	return Sum

while(1):
	Num1,Num2 = input().split()
	Num1 = int(Num1)
	Num2 = int(Num2)
	tot = int(bin(Num1)[2:]) + int(bin(Num2)[2:])
	arr = list(str(tot).replace("2","0"))
	print(BinaInt(arr))