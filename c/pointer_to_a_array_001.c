#include <stdio.h>

int main()
{
    char a[5] = { 'A', 'B', 'C', 'D' };
    char (*p3)[3] = &a;
    char (*p4)[3] = a;
    int i;

    for(i=0; i<5; i++)
    {
        printf("addr of a[%d]: 0x%lx\n", i, &a[i]);
    }

    printf("p3: 0x%lx\n", (long)p3);
    printf("p3+1: 0x%lx\n", (long)(p3+1));
    printf("p4+1: 0x%lx\n", (long)(p4+1));

    for(i=0; i<3; i++)
    {
        printf("(*p3)[%d]: %c\n", i, (*p3)[i]);
    }

    printf("(*(p3+1))[0]: %c\n", (char)(*(p3+1))[0]);
    printf("(*(p3+1))[1]: %c\n", (char)(*(p3+1))[1]);

    return 0;
}
