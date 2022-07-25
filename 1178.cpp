#include<iostream>
using namespace std;

int main()
{
	double Nro, arr[100];
	cin >> Nro;
	arr[0]=Nro;
	for(int k=1 ; k<100 ; k++){arr[k]=Nro/2; Nro=Nro/2;}
	for(int i=0 ; i<100 ; i++){printf("N[%d] = %.4f\n",i,arr[i]);}
	return 0;
}
