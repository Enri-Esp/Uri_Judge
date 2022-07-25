try:
	while(1):
		Num1, Num2 = input().split()
		Num1=int(Num1)
		Num2=int(Num2)
		tot = int(bin(Num1)[2:]) + int(bin(Num2)[2:])
		arr = '0b'+str(tot).replace("2","0")
		print(int(arr,2))
except EOFError: exit()