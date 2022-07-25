#include<iostream>
using namespace std;

int main()
{
	int temp1 = 0, temp2 = 1, temp;
	int Nro;
	cin >> Nro;
	while(Nro-1>0)
	{
		temp = temp2;
		cout << temp1 << " ";
		temp2 = temp1 + temp2;
		temp1 = temp;
		Nro = Nro - 1;
	}
	cout << temp1 <<"\n";
	return 0;
}
