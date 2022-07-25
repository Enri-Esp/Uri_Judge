NroC = int(input())
arr=[]
total = 0
for i in range(NroC):
	Costo=float(input())
	total+=Costo
	arrK = [str(x) for x in input().split(" ")]
	arr.append(len(arrK))
for i in range(NroC):
	print("day {0}: {1} kg".format(i+1,arr[i]))
print("{:.2f} kg by day".format(sum(arr)/NroC))
print("R$ {:.2f} by day".format(total/NroC))