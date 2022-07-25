#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	float N1,prom;
	int contPos=0;
	for(int k=0;k<6;k++)
	{
		cin >> N1;
		if(N1 > 0)
		{
			contPos+=1;
			prom += N1;
		}		
	}
	cout << contPos << " valores positivos" << endl;
	cout << fixed << setprecision(1) << prom/contPos << endl;
	return 0;
}
