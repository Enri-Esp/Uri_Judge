try:
	while(1):
		anio = int(input())
		print((anio-1)//100+1)
except EOFError: exit()

'''
		if(anio-1<100): print("1")
		else: print((anio-1)//100+1)'''