#include <stdio.h>

struct test {
    int i;
    short c;
    char *p;
    char s[10];
};

int main()
{
    struct test t1;
    //struct test *pt = &t1;
    struct test *pt = NULL;

    printf("&i = 0x%x\n", &pt->i);    //因为操作符优先级，我没有写成&(pt->i)
    printf("&c = 0x%x\n", &pt->c);
    printf("&p = 0x%x\n", &pt->p);
    printf("&s = 0x%x\n", pt->s); //等价于 printf("%x\n", &(pt->s) );

    return 0;
}
