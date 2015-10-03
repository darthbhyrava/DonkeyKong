#include<stdio.h>
int main()
{
	int i,j;
	for(i=0; i<80; i++)
		printf("'*',");
	for(i=0; i<28; i++)
	{
		printf("['*',");
		for(j=0; j<80; j++)
			printf("' ',");
		printf("'*'],\n");
	}
	for(i=0; i<80; i++)
		printf("'*',");
	return 0;
}

