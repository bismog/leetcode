/* main.c */
#include <stdio.h>
#include "c_trap_h.h"
 
//int b = 5555;
int b;
int c;
 
int main()
{
    foo();
    printf("main:\t(&a)=0x%08x\n\t(&b)=0x%08x\n\t(&c)=0x%08x\n\tsize(b)=%d\n\tb=%d\n\tc=%d\n",
        &a, &b, &c, sizeof b, b, c);
    return 0;
}
