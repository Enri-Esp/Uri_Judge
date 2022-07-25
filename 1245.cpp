#include <iostream>

using namespace std;
int find(int arr[], char arr2[], int total)
{
	int cont = 0;
	for(int i = 0 ; i<total ; i++)
	{
		for(int j = 0 ; j<total ; j++)
		{
			if(arr[i] == arr[j])
			{
				if(arr2[i] == 'E' && arr2[j] == 'D')
				{
					arr2[i] = arr2[j] = 'N';
					cont++;
				}
			}
		}
	}
	
	return cont;
}

int main()
{
	int nroT,par;
	
	while(scanf("%d", &nroT) != EOF)
	{
		int num[nroT];
		char lado[nroT];
		for(int i=0 ; i<nroT ; i++)
		{
			scanf("%d %c", &num[i], &lado[i]);
		}
		
		par = find(num, lado, nroT);
		cout << par << endl;
	}
}



















