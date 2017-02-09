#include <stdio.h>

typedef unsigned char UCH;
typedef signed char CH;


int main1()
{
    UCH uch;
    CH ch;

    uch = -1;
    ch  = 255;

    printf("uch: %d.\n", uch);
    printf("ch: %d.\n", ch);

    if(uch > ch)
        printf("uch > ch.\n");
    else if(uch < ch)
        printf("uch < ch.\n");
    else
        printf("uch = ch.\n");

    return 0;
}

int main()
{
    unsigned int allF1 = -1;
    unsigned int allF2 = 4294967293;
    unsigned int nonnegative = 3;

    printf("size of int is: %d.\n", sizeof(int));

    printf("allF1 value is %d(d).\n", allF1);
    printf("allF1 value is %u(u).\n", allF1);
    printf("sum of allF1 and nonnegative is:%d(d).\n", allF1+nonnegative);

    printf("allF2 value is %d(d).\n", allF2);

    return 0;
}
