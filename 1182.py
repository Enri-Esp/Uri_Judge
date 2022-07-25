Colunm = int(input())
Op = str(input())
res = 0
for k in range(144):
	Nro = float(input())
	if(k%12==Colunm):
		res += Nro
print("{:.1f}".format(res/12)*(Op == 'M') + "{:.1f}".format(res)*(Op == 'S'))
