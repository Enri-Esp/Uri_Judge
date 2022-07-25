#include<iostream>
using namespace std;

int main()
{
	int NC, CA, CB;
	double pA, pB;
	cin >> NC;
	for(int k=0 ; k<NC ; k++)
	{
		int cont = 0;
		cin >> CA >> CB >> pA >> pB;
		while(CA<=CB)
		{
			if(cont>100) break;
			CA = CA + int(CA*(pA/100));
			CB = CB + int(CB*(pB/100));
			cont++;
		}
		if(cont<101) cout << cont << " anos." << endl;
		else cout << "Mais de 1 seculo." << endl;
	}
	return 0;
}
