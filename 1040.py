N1,N2,N3,N4 = [float(x) for x in input().split(" ")]
Med = (2*N1+3*N2+4*N3+N4)/10
print("Media: {:.1f}".format(Med))
if(Med>=7.0):
	print("Aluno aprovado.")
elif(Med<=5.0):
	print("Aluno reprovado.")
else:
	print("Aluno em exame.")
	NewN = float(input())
	Med = (Med + NewN)/2
	print("Nota do exame: {:.1f}".format(NewN))
	print("Aluno aprovado."*(Med>=5.0)+"Aluno reprovado."*(Med<5.0))
	print("Media final: {:.1f}".format(Med))