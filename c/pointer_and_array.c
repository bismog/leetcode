
#include <stdio.h>

int main(void)
{
    int p1[10];
    int *p2[10];
    int (*p3)[10];

    printf("sizeof(int)   = %d\n", (int)sizeof(int));
    printf("sizeof(int *) = %d\n", (int)sizeof(int *));
    printf("sizeof(p1)    = %d\n", (int)sizeof(p1));    //40
    printf("sizeof(*p1)   = %d\n", (int)sizeof(*p1));   //4
    printf("sizeof(p2)    = %d\n", (int)sizeof(p2));    //80
    printf("sizeof(*p2)   = %d\n", (int)sizeof(*p2));   //8
    printf("sizeof(p3)    = %d\n", (int)sizeof(p3));    //8
    printf("sizeof(*p3)   = %d\n", (int)sizeof(*p3));   //40

    int arr[7] = {1,2,3,4,5,6,7};
    void *q = &arr;
    void *q1 = arr;

    void *t;
    t = &arr;
    void *x;
    x = arr;        // Here q / q1 / t / x are the same

    printf("addr of q: 0x%lx\n", q);
    printf("addr of q: 0x%lx\n", (q+1));
    printf("addr of q1: 0x%lx\n", (q1+1));
    printf("addr of t: 0x%lx\n", (t+1));
    printf("addr of x: 0x%lx\n", (x+1));

    return 0;
}

