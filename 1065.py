contPar = 0
contImp = 0
contPos = 0
contNeg = 0
for k in range(5):
	Nro = int(input())
	if(Nro%2 == 0):
		contPar += 1
	else:
		contImp += 1
	if(Nro > 0):
		contPos += 1
	elif(Nro == 0):
		pass
	else:
		contNeg += 1
print("{} valor(es) par(es)".format(contPar))
print("{} valor(es) impar(es)".format(contImp))
print("{} valor(es) positivo(s)".format(contPos))
print("{} valor(es) negativo(s)".format(contNeg))