#include<stdio.h>
int main()
{
	int g(char *ch) { return printf(ch); }
    	int (*f)(char *ch)=g; f("hello");
	return 0;
}

