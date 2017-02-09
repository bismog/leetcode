#include <stdio.h>

int main()
{
    struct bs
     {
        unsigned a:1;
        unsigned b:3;
        unsigned c:4;
    } bit, *PBit;
    bit.a = 1;
    bit.b = 7;
    bit.c = 15;
    printf("%d,%d,%d\n", bit.a, bit.b, bit.c);
    PBit = &bit;
    PBit->a = 0;
    PBit->b &= 3;
    PBit->c |= 1;
    printf("%d,%d,%d\n", PBit->a, PBit->b, PBit->c);

    return 0;
}
