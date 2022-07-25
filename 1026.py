def bina(Num):
	temp = ""
	if(Num==0):
		return 0
	while(Num>0):
		temp = str(Num%2) + temp
		Num = Num//2
	return int(temp)

def BinaInt(arr):
	arr.reverse()
	Sum=0
	for k in range(len(arr)):
		Sum = Sum + int(arr[k])*(2**k)
	return Sum

while(1):
	Num1, Num2 = [int(x) for x in input().split(" ")]
	tot = bina(Num1) + bina(Num2)
	arr = list(str(tot).replace("2","0"))
	print(BinaInt(arr))
	
a=bin(23)
b=a[2:]
