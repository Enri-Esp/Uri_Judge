"""cadena = str(input())
cadenaD = ''
cont = 1
for k in cadena:
	if(k!=" "):
		cadenaD += k.upper()*(cont%2==1) + k.lower()*(cont%2==0)
		cont+=1
	else: cadenaD += " "
print(cadenaD)
"""
try:
	while(1):
		cadena = str(input())
		cadenaD = ''
		cont = 1
		for k in cadena:
			if(k!=" "):
				cadenaD += k.upper()*(cont%2==1) + k.lower()*(cont%2==0)
				cont+=1
			else: cadenaD += " "
		print(cadenaD)
except EOFError: exit()