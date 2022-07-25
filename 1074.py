Tot = int(input())
for k in range(Tot):
	st = ""
	Nro = int(input())
	if(Nro==0):
		st = "NULL"
	elif(Nro%2==0):
		st += "EVEN"
	else:
		st += "ODD"
	if(Nro==0):
		pass
	elif(Nro>0):
		st += " POSITIVE"
	else:
		st += " NEGATIVE"
	print(st)