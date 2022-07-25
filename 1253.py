NC = int(input())
for k in range(NC):
	cad = str(input())
	NroSalto = int(input())
	nuevaCad = ''
	for k in cad:
		ascK = ord(k)
		ascK-=NroSalto
		if(ascK<65): ascK+=26
		nuevaCad+=chr(ascK)
	print(nuevaCad)