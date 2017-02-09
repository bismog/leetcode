/* foo.c */
#include <stdio.h>
#include "c_trap_h.h"
 
struct {
   char a;
   int b;
} b = { 2, 4 };
 
int main();
 
void foo()
{
    printf("foo:\t(&a)=0x%08x\n\t(&b)=0x%08x\n\tsizeof(b)=%d\n\tb.a=%d\n\tb.b=%d\n\tmain:0x%08x\n",
        &a, &b, sizeof b, b.a, b.b, main);
}
