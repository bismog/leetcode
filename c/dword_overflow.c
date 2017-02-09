#include "stdio.h"

int main()
{
    int x=431200874;
    
    int xo=0;
    xo = x*10+6;
    if(xo < x)
        printf("overflow");
    else
        printf("ok");
}
