F1 = "`1234567890-="
F2 = "QWERTYUIOP[]\\"
F3 = "ASDFGHJKL;'"
F4 = "ZXCVBNM,./"
try:
	while(True):
		st = str(input())
		if(st==""): break
		st1 = ""
		for k in st:
			if(k == " "): st1+=" " 
			elif(k in F1): st1+= F1[F1.index(k)-1]
			elif(k in F2): st1+= F2[F2.index(k)-1]
			elif(k in F3): st1+= F3[F3.index(k)-1]
			else: st1+= F4[F4.index(k)-1]
		print(st1)
except EOFError: exit()