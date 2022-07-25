#include<iostream>
#include <cmath>
using namespace std;

int main()
{
	int r1, x1, y1, r2, x2, y2;
	long long int disc; 
	int a, b, c;
	int C;
	long long int comp, comp1;
	
	while(scanf("%d %d %d %d %d %d",&r1,&x1,&y1,&r2,&x2,&y2) != EOF)
	{
		int cont = 0;
		a = 2 * (x2 - x1); b = 2 * (y2 - y1); c = r1 * r1 - x1 * x1 - y1 * y1 - r2 * r2 + x2 * x2 + y2 * y2; 
		C = c - a * x1 - b * y1;
		comp = pow(r1, 2) * (pow(a, 2) + pow(b, 2));
		comp1 = pow(C, 2); disc = comp - pow(C, 2);
		if (disc > 0)
		{
			cont=1;
		}
		if(cont || r1<r2)
			cout << "MORTO" << endl;
		else
			cout << "RICO" << endl;
	}
		
	return 0;
}
