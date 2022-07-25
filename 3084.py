try:
	while(1):
		N1,N2 = input().split()
		N1=int(N1)
		N2=int(N2)
		if(N1+N2==0): print("00:00")
		else:
			H = int((N1*12)/360)
			M = int((N2*60)/360)
			if(0<=H<10): print("0{0}:0{1}".format(H,M)*(M<10)+"0{0}:{1}".format(H,M)*(M>=10))
			else: print("{0}:0{1}".format(H,M)*(M<10)+"{0}:{1}".format(H,M)*(M>=10))
except EOFError: exit()