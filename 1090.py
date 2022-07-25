while(True):
	NC = int(input())
	if NC == 0 : break
	arr = []
	dicNro = {"um":1,"dois":2,"tres":3}
	dicFig = {"circulo":1,"circulos":1,"quadrado":2,"quadrados":2,"triangulo":3,"triangulos":3}
	for k in range(NC):
		caso = input().split()
		arr.append([dicNro[caso[0]],dicFig[caso[1]]])
	print(arr)