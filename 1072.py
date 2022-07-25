Tot = int(input())
cont = 0
for k in range(Tot):
	Nro = int(input())
	if(Nro>=10 and Nro<=20):
		cont += 1
print("{} in".format(cont))
print("{} out".format(Tot - cont))