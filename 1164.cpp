#include<iostream>
using namespace std;

int main()
{
	int Nro,temp1,temp2;
	cin >> Nro;
	for(int k=0 ; k<Nro ; k++)
	{
		int sum = 0;
		cin >> temp1;
		temp2 = temp1-1;
		while(temp2>0)
		{
			if(temp1%temp2==0) sum = sum+temp2;
			temp2--;
		}
		if(sum==temp1) printf("%d eh perfeito\n",temp1);
		else printf("%d nao eh perfeito\n",temp1);
	}
	return 0;
}
