arrM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NroC = int(input())
for k in range(NroC):
	st = str(input())
	if(st[0] == st[2]):
		print(int(st[0])*int(st[2]))
	else:
		print((int(st[2])-int(st[0]))*(st[1] in arrM) +
			(int(st[0])+int(st[2]))*(st[1] not in arrM))