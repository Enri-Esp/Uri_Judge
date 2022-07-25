N = int(input())
for k in range(N):
	Sum = 0
	A, B = [int(k) for k in input().split(" ")]
	if(A > B):
		A, B = B, A
	A+=1
	while(A < B):
		if(A%2==1):
			Sum += A
		A+=1
	print(Sum)