dic = {1:0,2:0,3:0}
while(True):
	Nro = int(input())
	if(Nro==4): break
	if(Nro>4): pass
	else: dic[Nro]=dic[Nro]+1
print("MUITO OBRIGADO")
print("Alcool: {}".format(dic[1]))
print("Gasolina: {}".format(dic[2]))
print("Diesel: {}".format(dic[3]))