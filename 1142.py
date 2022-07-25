cont=1
X=int(input())
Y=int(input())
while(Y<=X):
	Y = int(input())
suma=X
while(suma<Y):
	X+=1
	suma+=X
	cont+=1
print(cont)