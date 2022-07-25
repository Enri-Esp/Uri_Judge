#include<iostream>
using namespace std;

int main()
{
	int arr[20],Nro;
	for(int k=19; k>=0 ; k--)
	{
		cin >> Nro;
		arr[k] = Nro;
	}
	for(int k=0 ; k<20 ; k++){printf("N[%d] = %d\n",k,arr[k]);}
	return 0;
}
