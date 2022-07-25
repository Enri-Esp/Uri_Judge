Nro = int(input())
x = [int(i) for i in input().split()]
arrT = sorted(x)
print("Menor valor: {}".format(arrT[0]))
print("Posicao: {}".format(x.index(arrT[0])))