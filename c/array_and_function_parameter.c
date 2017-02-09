#include <stdio.h>

#define MAX   3

typedef struct{
    int a;
    int b;
    int c;
}T_abc;

void dataHandle(T_abc *pt)
{
    int i; 

    for(i=0; i<MAX; i++) {
        pt[i].a = i*i+1;
        pt[i].b = i*i+2;
        pt[i].c = i*i+3;
    }

    return ;
}

int main()
{
    int i;
    T_abc t1[MAX];

    dataHandle(&t1[0]); 

    for(i=0; i<MAX; i++) {
        printf("%d.a is %d\n", i, t1[i].a);
        printf("%d.b is %d\n", i, t1[i].b);
        printf("%d.c is %d\n", i, t1[i].c);
    }

    return 0;
}
