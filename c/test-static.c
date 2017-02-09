#include "share.h"
#include "static.h"
#include "stdio.h"

int test_add(int x, int y) 
{ 
    // 调用static里面的方法 
    return add(x, y); 
}

int main()
{
    int a=5;
    int b=3;
    int c;

    c = test_add(a,b);
    printf("result: %d ", c);
    return 0;
}
