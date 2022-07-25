NC = int(input())
for k in range(NC):
	dieta = str(input())
	des = str(input())
	alm = str(input())
	comida = des+alm
	control = 0
	for k in comida:
		if(k not in dieta):
			print("CHEATER")
			control=1
			break
		dieta = dieta.replace(k,'')
	if(control == 0):
		arr = list(dieta)
		arr.sort()
		print(''.join(arr))
