while(True):
	A,B = input().split()
	if(int(A)+int(B)==0):break
	B=str(B)
	A=str(A)
	B = B.replace(A,"")
	if(B==""): print("0")
	else: print(int(B))