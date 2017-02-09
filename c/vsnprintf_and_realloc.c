#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
char *make_message(const char *fmt, ...)
{
    /* 初始時假設我們只需要不超過100字節大小的空間 */
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
        /* 嘗試在申請的空間中進行打印操作 */
        va_start(ap, fmt);
        n = vsnprintf(p, size, fmt, ap);
        va_end(ap);
        /* 如果vsnprintf調用成功，返回該字符串 */
        if(n > -1 && n < size)
            return p;
        /* vsnprintf調用失敗(n<0)或者p的空間不足夠容納size大小的字符串(n>=size)，嘗試申請更大的空間 */
        //size *= 2;      /* 兩倍原來大小的空間 */
        size += 2;
        if((p = (char *)realloc(p, size)) == NULL)
            return NULL;
    }
}

int main()
{
    /* 調用上面的函數 */
    char *str = make_message("%d,%d,%d,%d", 5, 6, 7, 8);

    printf("%s", str);

    printf("we will go...");
    return 0;
}
