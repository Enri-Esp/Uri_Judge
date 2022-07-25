#include<iostream>
using namespace std;

long long int Fib(int Nro)
{
	int NroTer=Nro+1;
	long long int a=0,b=1,x,rpta;
	while(NroTer>0)
	{
		rpta=a;
		x = b;
		b = b+a;
		a = x;
		NroTer--;
	}
	return rpta;
}

int main()
{
	int NroC,NroSerie;
	cin >> NroC;
	for(int k=0 ; k<NroC ; k++)
	{
		cin >> NroSerie;
		printf("Fib(%d) = %lld\n",NroSerie,Fib(NroSerie));
	}
	return 0;
}
	
