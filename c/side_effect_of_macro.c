//i cann't find what side-effect leaved in this code
#include <stdio.h>

#define  MIN(A,B)   ((A) <= (B) ? (A) : (B))

int main()
{
    int a[4],b;
    int *p;
    int least = 0;

    a[0] = 1;
    a[1] = 2;
    a[2] = 3;
    a[3] = 4;
    b    = 6;
    p = &a[0];

    least = MIN(*p++, b);
    printf("the least value is: %u\n", least);
    return 0;
}
