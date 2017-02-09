#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
char *make_message(const char *fmt, ...)
{
    /* ��ʼ�r���O�҂�ֻ��Ҫ�����^100�ֹ���С�Ŀ��g */
    //cause size is 0, even if p has not malloc(initialized),function vsnprintf will not trigger signal exception
    int n, size = 3;
    char *p;
    //char *ar[1];
    
    //p = &ar[0];

    p = NULL;
    //ar[0] = NULL;

    va_list ap;
    //if((p = (char *)malloc(size)) == NULL)
    //    return NULL;
    while(1) {
        /* �Lԇ����Ո�Ŀ��g���M�д�ӡ���� */
        va_start(ap, fmt);
        n = vsnprintf(p, size, fmt, ap);
        va_end(ap);
        /* ���vsnprintf�{�óɹ�������ԓ�ַ��� */
        if(n > -1 && n < size)
            return p;
        /* vsnprintf�{��ʧ��(n<0)����p�Ŀ��g������ݼ{size��С���ַ���(n>=size)���Lԇ��Ո����Ŀ��g */
        //size *= 2;      /* �ɱ�ԭ���С�Ŀ��g */
        size += 2;
        if((p = (char *)realloc(p, size)) == NULL)
            return NULL;
    }
}

int main()
{
    /* �{������ĺ��� */
    char *str = make_message("%d,%d,%d,%d", 5, 6, 7, 8);

    printf("%s", str);

    printf("we will go...");
    return 0;
}
