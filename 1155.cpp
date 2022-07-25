#include<iostream>
#include<iomanip>
using namespace std;
/*
int main()
{
	double suma=1.0, cont=2;
	while(cont<=40)
	{
		suma = suma + (cont+1)/(cont);
		cont+=2;
	}
	cout << fixed << setprecision(2) << suma << endl;
	return 0;
}*/
int main()
{

    double a,b=1.00,d,S=0;

    for(a=1;a<=39;a+=2)
    {
        d=a/b;
        S+=d;
        b*=2;
    }

    cout<<fixed<<setprecision(2)<<S<<endl;

    return 0;
}
