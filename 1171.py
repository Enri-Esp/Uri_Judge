Nro = int(input())
dic ={}
for k in range(Nro):
	Nro = int(input())
	if(Nro not in dic): dic[Nro] = 1
	else: dic[Nro] += 1
arr = sorted(dic)
for k in arr:
	print("{0} aparece {1} vez(es)".format(k,dic[k]))