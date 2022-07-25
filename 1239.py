try:
	while(1):
		cadena = str(input())
		conti = 0
		contb = 0
		cadF = ''
		for k in cadena:
			a=k
			if(a == '_'):
				a = '<i>' if(conti%2==0) else '</i>'
				conti+=1
			elif(a == '*'):
				a = '<b>' if(contb%2==0) else '</b>'
				contb+=1
			cadF+=a
		print(cadF)
except EOFError: exit()