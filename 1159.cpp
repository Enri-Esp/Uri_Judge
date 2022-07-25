#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int Nro, temp1, temp2;
	while(true)
	{
		int suma=0;
		cin >> Nro;
		if(Nro==0) break;
		Nro = Nro + (abs(Nro%2));
		temp1 = Nro+8;
		while(Nro<=temp1)
		{
			suma = suma + Nro;
			Nro = Nro + 2;
		}
		cout << suma << endl;
	}
	return 0;
}
