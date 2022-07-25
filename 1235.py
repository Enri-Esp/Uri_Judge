NC =  int(input())
for k in range(NC):
	cadena = str(input())
	mit = int(len(cadena)/2)
	print(cadena[:mit][::-1]+cadena[mit:][::-1])