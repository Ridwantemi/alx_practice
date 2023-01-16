#include <stdio.h>
int main()
{
	int c,d,f,g,a;
	c = sizeof(char);
	d = sizeof(int);
	a = sizeof(long int);
	g = sizeof(long long int);
	f = sizeof(float);
	printf("Size of a char: %d byte(s)\nSize of an int: %d byte(s)\nSize of a long int: %d byte(s)\nSize of a long long int: %d byte(s)\nSize of a float: %d byte(s)\n",c,d,a,g,f);
	return 0;
}
