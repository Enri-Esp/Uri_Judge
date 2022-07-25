#include<iostream>
using namespace std;

int main()
{
	int NroImp, st=0, cont=0;
	int arr[1000];
	cin >> NroImp;
	while(st<1000)
	{
		if(cont<NroImp-1){arr[st]=cont; cont++;}
		else{arr[st]=cont; cont=0;}
		st++;
	}
	for(int k=0 ; k<1000 ; k++){printf("N[%d] = %d\n",k,arr[k]);}
	return 0;
}

