def SAM(str1, str2, p, r):
	if(p==r):
		return 1 if str1[p] in str2 else 0
	else:
		q = (p+r)//2
		x1 = SAM(str1, str2,p,q)
		x2 = SAM(str1, str2,q+1,r)
		y1 = 1 if str1[q] in str2 else 0
		s = str1[q]
		arr1 = 0
		for k in range(q-1,p-1,-1):
			s = str1[k] + s
			if(s in str2 and len(s)>y1):
				y1=len(s)
				arr1=k
		y2 = 1 if str1[q+1] in str2 else 0
		s = str1[q+1]
		arr2 = 0
		for k in range(q+2,r+1):
			s = s + str1[k] 
			if(s in str2 and len(s)>y2):
				y2 = len(s)
				arr2=k	
		arrT = len(str1[arr1:arr2+1]) if str1[arr1:arr2+1] in str2 else 0
		return max(x1,x2,arrT) 
try:
	while(1):
		str1 = str(input())
		str2 = str(input())
		print(SAM(str1,str2,0,len(str1)-1))
except EOFError: exit()
