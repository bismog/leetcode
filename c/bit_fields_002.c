#include <stdio.h>

int main()
{
    union {
        struct {
            unsigned short s1:3;
            unsigned short s2:3;
            unsigned short s3:3;
        } x;
        char c;
    } v;

    v.c = 100;
    printf("%d\n", v.x.s3);

    return 0;
}
