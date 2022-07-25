NC = int(input())
for k in range(NC):
	a, b = input().split()
	men = len(a) if len(a)<len(b) else len(b)
	recorte = a[men:] + b[men:]
	newArr = ''
	for i in range(men):
		newArr = newArr + a[i] + b[i]
	print(newArr+recorte)