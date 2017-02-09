/* t1.c */
#include <stdio.h>
 
int b = 1;
int c = 1;
 
int main()
{
    int count = 2;
    while (count-- > 0) {
        b = 1;
        c = 1;
        t2();
        foo();
        printf("t1:\t(&b)=0x%08x\n\t(&c)=0x%08x\n\tsizeof(b)=%d\n\tb=%d\n\tc=%d\n",
            &b, &c, sizeof b, b, c);
        sleep(1);
    }
    return 0;
}
