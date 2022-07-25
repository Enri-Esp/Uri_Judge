#include<iostream>
using namespace std;

int main()
{
	int arr[10], Nro;
	cin >> Nro;
	arr[0]=Nro;
	for(int k=1; k<10 ; k++) {arr[k]=Nro*2; Nro=Nro*2;}
	for(int k=0 ; k<10 ; k++){printf("N[%d] = %d\n",k,arr[k]);}
	return 0;
}
