arr = []
cod = 0
while(1):
	st = str(input())
	if("</html>" in st): break
	if(cod): arr.append(st)
	if("<body>" in st): cod=1
	if("</body>" in st): cod=0
for k in range(len(arr)-1):
	print(arr[k]) 