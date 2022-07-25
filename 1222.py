try:
	while(1):
		NP, NL, NC = input().split()
		NP = int(NP)
		NL = int(NL)
		NC = int(NC)
		cadena = [str(x) for x in input().split(" ")]
		contPalabras = 1
		contLineas = 1
		contCaracteres = len(cadena[0])
		while(contPalabras<NP):
			contCaracteres += len(cadena[contPalabras])+1
			if(contCaracteres>NC):
				contCaracteres = len(cadena[contPalabras])
				contLineas+=1
			contPalabras+=1
		print(contLineas//NL + (contLineas%NL!=0))
		
except EOFError: exit()
"""
NP, NL, NC = input().split()
NP = int(NP)
NL = int(NL)
NC = int(NC)
cadena = [str(x) for x in input().split(" ")]
contPalabras = 1
contLineas = 1
contCaracteres = len(cadena[0])
while(contPalabras<NP):
	contCaracteres += len(cadena[contPalabras])+1
	if(contCaracteres>NC):
		contCaracteres = len(cadena[contPalabras])
		contLineas+=1
	contPalabras+=1
print(contLineas//NL + (contLineas%NL!=0))
"""


