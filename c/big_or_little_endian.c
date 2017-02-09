#include <stdio.h>

int checkSystem()
{
    union check {
	int i;
	char ch;
    } c;
    c.i = 1;
    return (c.ch == 1);
}

int main()
{
    int ret=0;
    ret = checkSystem();
    if(1 == ret)
    {
        printf("this machine is little endiam.\n", ret);
    }
    else
    {
        printf("this machine is little endiam.\n", ret);
    }
    return 0;
}
