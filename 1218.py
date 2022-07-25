NroCaso=1
try:
	while(1):
		NroI = str(input())
		contF=0
		contM=0
		arr = [str(x) for x in input().split(" ")]
		if(NroCaso>1): print("")
		contT=arr.count(NroI)
		while(contT!=contF+contM):
			val = arr.index(NroI)
			contF+=(arr[val+1]=="F")
			contM+=(arr[val+1]=="M")
			arr.remove(NroI)
		print("Caso {}:".format(NroCaso))
		print("Pares Iguais: {}".format(contT))
		print("F: {}".format(contF))
		print("M: {}".format(contM))
		NroCaso+=1
except EOFError: exit()