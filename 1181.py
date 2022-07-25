L = int(input())
op = str(input())
arr=[]
for i in range(12):
	arrT=[]
	for i in range(12):
		Nro = float(input())
		arrT.append(Nro)
	arr.append(arrT)

print("{:.1f}".format(sum(arr[L]))*(op=="S")+
	"{:.1f}".format(sum(arr[L])/12)*(op=="M"))