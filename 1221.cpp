#include <iostream>
#include <math.h>

using namespace std;

int primo(int n)
{
	int i = 2;
	while(i<=sqrt(n))
	{
		if(n%i == 0)
			return 0;
		i++;
	}
	return 1;
}

int main()
{
	int nro, val;
	cin >> nro;
	while(nro--)
	{
		cin >> val;
		if(primo(val))
			cout << "Prime" << endl;
		else
			cout << "Not Prime" << endl;
	}
	return 0;
}
