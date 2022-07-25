while(True):
	arr = [str(x) for x in input().split(" ")]
	a=set([])
	if(arr[0] == "*"):
		break
	for k in arr:
		a.add(k[0].lower())
	if(len(a)==1):
		print("Y")
	else:
		print("N")