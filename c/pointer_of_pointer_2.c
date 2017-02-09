#include <stdio.h>
#include <unistd.h>

void change_val(int **p)
{
    //static int new_val[3] = { 4, 5, 6 };	// [2] static is 局部静态变量, store in .data  
    printf("p: %x, *p: %x", (int)p, (int)*p);
    int new_val[3] = { 4, 5, 6 };	// [2]  
    *p = new_val;
    printf("p: %x, *p: %x", (int)p, (int)*p);
}

int main()
{
    int i;
    int val[3] = { 1, 2, 3 };
    int *p = val;		// [1]  
    for (i = 0; i < 3; i++, p++)
    {
        printf("*p:%u ", *p);
    }
    change_val(&p);
    sleep(100); //没有sleep的话，立即读取，可能是正常的值，但sleep之后，读取的就变化了，说明那块地址被做别的用了。
    printf("----");
    for (i = 0; i < 3; i++, p++)
    {
        printf("*p:%u ", *p);
    }
    printf("\n");
    return 0;
}
