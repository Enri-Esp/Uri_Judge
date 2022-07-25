arr = []
sum
while(True):
	M, N = [int(k) for k in input().split(" ")]
	if(M <=0 or N <=0):
		break
	if(M > N):
		M, N = N, M
	while(M <= N):
