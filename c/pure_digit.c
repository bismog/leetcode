#include "stdio.h"

char *s="1234566";

int main()
{

    while(*s && *s>='0' && *s <='9')
        s++;

    if (*s)
        //不是纯数字
        printf("not pure digit.\n");
    else
        printf("It's pure digit.\n");

    return 0;
}
