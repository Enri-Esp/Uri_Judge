while(True):
	H1,M1,H2,M2 = [int(x) for x in input().split(" ")]
	A = H2*60+M2 - (H1*60+M1)
	if(A==0):
		break
	elif(A<0):
		print(((H2+24)*60+M2)-(H1*60+M1))
	else:
		print(A)