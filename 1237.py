try:
	while(1):
		str1 = str(input())
		str2 = str(input())
		arrMax = 0
		for k in range(len(str1)):
			for i in range(k+1,len(str1)+1):
				if(str1[k:i] in str2 and len(str1[k:i])>arrMax):
					arrMax = len(str1[k:i])
		print(arrMax)
except EOFError: exit()