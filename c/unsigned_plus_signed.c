#include <stdio.h>

int main()
{
    unsigned int a;
    int b;
    int c;
    unsigned int s1;
    int s2;

    a = 8;
    b = -10;
    c = -5;
    s1 = b+a;
    s2 = b+a;

    printf("sum of a+b is %ld. \n", (a+b));
    printf("sum of b+a is %ld. \n", (b+a));
    printf("sum of a+c is %ld. \n", (a+c));
    printf("s1 is %ld. \n", s1);
    printf("s2 is %ld. \n", s2);

    return 0;
}
