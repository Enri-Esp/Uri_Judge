#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
	int Nro, cont = 0;
	double Prom;
	while(true)
	{
		cin >> Nro;
		if(Nro<0) break;
		Prom = Prom + Nro;
		cont++;
	}
	cout << fixed << setprecision(2) << Prom/cont << endl;
	return 0;
}
