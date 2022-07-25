#include<iostream>
using namespace std;

int main()
{
	int NroImp, NroFinal, st=1, cont=0;
	cin >> NroImp >> NroFinal;
	while(st<=NroFinal)
	{
		if(cont<NroImp-1) 
		{
			printf("%d ",st);
			cont++;
		}
		else
		{
			printf("%d\n",st);
			cont=0;
		}
		st++;
	}
	return 0;
}

