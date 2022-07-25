arr = [6,2,5,5,4,5,6,3,7,6]
NC = int(input())
for k in range(NC):
	Nro = str(input())
	cont=0
	for i in Nro:
		cont+=arr[int(i)]
	print("{} leds".format(cont))