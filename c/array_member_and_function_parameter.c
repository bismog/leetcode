#include <stdio.h>

typedef struct
{
    unsigned char ch;
    unsigned short sh;
    unsigned int in;
    unsigned long lo;
}T_xxx;

T_xxx  txxx[20];

void setxxx(unsigned char index, T_xxx *pxxx)
{
    pxxx[index].ch = 0x12+index;
    pxxx[index].sh = 0x1234+index;
    pxxx[index].in = 0x12345678+index;
    pxxx[index].lo = 0x1234567890123456+index;

    return;
}

T_xxx* getxxx(unsigned char index)
{
    return &txxx[index];
}



int main()
{
    T_xxx *plx;
    unsigned char index;

    setxxx(4, txxx);
    setxxx(5, txxx);
    setxxx(6, txxx);

    index = 5;
    plx = getxxx(index);

    printf("ch of %d is 0x%lx\n", index, plx->ch);
    printf("sh of %d is 0x%lx\n", index, plx->sh);
    printf("in of %d is 0x%lx\n", index, plx->in);
    printf("lo of %d is 0x%lx\n", index, plx->lo);

    return 0;
}
