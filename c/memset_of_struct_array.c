#include <stdio.h>
#include <string.h>

typedef struct {
    int a;
    int b;
    int c;
}T_abc;

#define ALEN  5

int main()
{
    T_abc t1[ALEN], t2[ALEN];
    int i; 

    memset(t1, 0x5a, sizeof(T_abc)*ALEN);
    memset(t2, 0x3c, ALEN);

    for(i=0; i<ALEN; i++) {
        printf("t1.%d.a: 0x%x\n", i, t1[i].a);
        printf("t1.%d.b: 0x%x\n", i, t1[i].b);
        printf("t1.%d.c: 0x%x\n", i, t1[i].c);
    }
    for(i=0; i<ALEN; i++) {
        printf("t2.%d.a: 0x%x\n", i, t2[i].a);
        printf("t2.%d.b: 0x%x\n", i, t2[i].b);
        printf("t2.%d.c: 0x%x\n", i, t2[i].c);
    }
    return ;
}
