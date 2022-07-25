#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int Nro, imp[5], par[5];
	int contImp=0,contPar=0;
	for(int k=0; k<15 ; k++)
	{
		cin >> Nro;
		if(abs(Nro)%2==0)
		{
			if(contPar<5) {par[contPar]=Nro;contPar++;}
			else 
			{
				for(int i=0; i<5 ; i++)
				{
					printf("par[%d] = %d\n",i,par[i]);
					contPar=0;		
					int par[5];
				}
				par[contPar]=Nro; 
				contPar++;	
			}
		}
		else
		{
			if(contImp<5) 
			{
				imp[contImp]=Nro;
				contImp++;
			}
			else 
			{
				for(int i=0; i<5 ; i++)
				{
					printf("impar[%d] = %d\n",i,imp[i]);
					contImp=0;
					int imp[5];
				}
				imp[contImp]=Nro; contImp++;
			}
		}
	}
	if(contImp!=0)
	{
		for(int k=0 ; k<contImp ; k++) printf("impar[%d] = %d\n",k,imp[k]);	
	}
	if(contPar!=0)
	{
		for(int k=0 ; k<contPar ; k++) printf("par[%d] = %d\n",k,par[k]);	
	}
	return 0;
}
