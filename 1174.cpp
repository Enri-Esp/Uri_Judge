#include<iostream>
using namespace std;

int main()
{
	float arr[10], Nro,temp;
	for(int k=0; k<10 ; k++) 
	{
		cin >> Nro;
		arr[k]=Nro;
	}
	for(int k=0 ; k<10 ; k++)
	{
		temp = arr[k];
		if(temp<=10){printf("A[%d] = %.1f\n",k,temp);}	
	}
	return 0;
}
