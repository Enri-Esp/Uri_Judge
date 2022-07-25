#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int N, X, Y;
	cin >> N;
	for(int k=0 ; k<N ; k++)
	{
		int suma = 0;
		int cont = 0;
		cin >> X >> Y;
		while(Y>cont)
		{
			if(abs(X)%2==1)
			{
				suma = suma + X;
				cont++;
			}
			X++;
		}
		cout << suma << endl;
	}
	return 0;
}
