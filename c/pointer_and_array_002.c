
#include <stdio.h>

int main(void)
{
    int a[10] = {10,20,30,40,50,60,70,80,90,100};
    int (*p)[3];  // p is a pointer to an array of three integers
    p = a;
    printf("%u\n", a);    // prints starting address of an array (Say 1000)
    printf("%u, %u\n", p, p+1);    // prints 1000, 1012
    printf("%u, %d\n", *p, **p);  // prints 1000, 10
    printf("%d, %d, %d\n", *p[0], *p[1], *p[2]);       // prints 10, 40, 70
    printf("%d, %d, %d\n", **(p+0), **(p+1), **(p+2)); // prints 10, 40, 70
    printf("%d, %d, %d\n", p[0][0], p[1][0], p[2][0]); // prints 10, 40, 70
    printf("%d, %d, %d\n", (*p)[0], (*p)[1], (*p)[2]); // prints 10, 20, 30
    printf("%d, %d, %d\n", p[0][0], p[0][1], p[0][2]); // prints 10, 20, 30
    return 0;
}

