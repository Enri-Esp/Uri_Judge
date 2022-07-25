def Comprobar(cad):
	cond1 = '0' in cad or '1' in cad or '2' in cad or '3' in cad or '4' in cad or '5' in cad or '6' in cad or '7' in cad or '8' in cad or '9' in cad
	cond2 = False
	totPuntos = cad.count('.')
	if(totPuntos==1 and cad[-1:]!='.' or totPuntos>1):
		cond2 = True
	return not(cond1 or cond2)

try:
	while(1):
		arrCad = input().split(' ')
		contT = 0
		contP = 0
		for k in arrCad:
			if(k!='' and Comprobar(k) and k!='.'):
				contT+=len(k) if k[-1:]!='.' else len(k)-1
				contP+=1
		prom = contT//contP if contP!=0 else 0
		if(prom<=3):
			print('250')
		elif(prom==4 or prom==5):
			print('500')
		elif(prom>=6):
			print('1000')
except EOFError: exit()
