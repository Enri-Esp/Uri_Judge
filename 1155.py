suma = 1.0
cont = 2
while(cont<=40):
	suma += float(cont+1)/float(cont)
	cont+=2
print("{:.2f}".format(suma))