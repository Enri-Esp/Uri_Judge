TC = 0
TR = 0
TS = 0
N = int(input())
for k in range(N):
	Cant, Tipo = [str(k) for k in input().split(" ")]
	Cant = int(Cant)
	if(Tipo == "C"):
		TC += Cant
	elif(Tipo == "R"):
		TR += Cant
	else:
		TS += Cant
T = TS+TR+TC
print("Total: {} cobaias".format(T))
print("Total de coelhos:", TC)
print("Total de ratos:", TR)
print("Total de sapos:", TS)
print("Percentual de coelhos: {:.2f} %".format(TC/T*100))
print("Percentual de ratos: {:.2f} %".format(TR/T*100))
print("Percentual de sapos: {:.2f} %".format(TS/T*100))