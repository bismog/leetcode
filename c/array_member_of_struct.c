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

    printf("&i = 0x%x\n", &pt->i);    //��Ϊ���������ȼ�����û��д��&(pt->i)
    printf("&c = 0x%x\n", &pt->c);
    printf("&p = 0x%x\n", &pt->p);
    printf("&s = 0x%x\n", pt->s); //�ȼ��� printf("%x\n", &(pt->s) );

    return 0;
}
