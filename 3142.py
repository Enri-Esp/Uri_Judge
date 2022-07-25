try:
	while(1):
		arr = input()
		if(len(arr)==1): print(ord(arr[0])-64)
		elif(len(arr)==2): print((ord(arr[0])-64)*26+ord(arr[1])-64)
		elif(len(arr)==3):
			caso = (ord(arr[0])-64)*26*26 + (ord(arr[1])-64)*26 + ord(arr[2])-64
			print("Essa coluna nao existe Tobias!"*(caso>16384)+str(caso)*(caso<=16384))
		else: print("Essa coluna nao existe Tobias!")
except EOFError: exit()