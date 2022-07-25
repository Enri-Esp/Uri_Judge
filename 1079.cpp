#include<iostream>
using namespace std;

int main()
{
	int NroC;
	cin >> NroC;
	float a,b,c,Rpta;
	for(int k=0 ; k<NroC ; k++)
	{
		cin >> a >> b >> c ;
		Rpta = (a*2.0+b*3.0+c*5.0)/10.0;
		printf("%.1f\n",Rpta);
	}
	return 0;
}
