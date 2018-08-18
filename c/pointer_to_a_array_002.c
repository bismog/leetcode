#include <stdio.h>

int main()
{
    int i;
    int c[4]={1,2,3,4};
    int *a[4]; //指针数组   array of pointers
    int (*b)[4]; //数组指针 pointer to an array
    int *b0;
    b0 = c;
    printf("%d  ", *b0);   // The first element of array
    printf("%d  ", *(b0+1));    // The second one
    printf("%d  ", *(b0+2));    // The third one
    printf("\n");
    b=&c;
    printf("0x%lx  ", *b);  //The same as array name(c), address of the first element
    printf("%d  ", **b);    //The first element of array
    printf("%d  ", **(b+1));   // unknown area
    printf("%d  ", **(b+2));   // unknown area
    printf("\n");
    //将数组c中元素赋给数组a
    for(i=0;i<4;i++)
    {
        a[i]=&c[i];
        printf("a[%d] is: 0x%lx\n", i, a[i]);
    }
    //输出看下结果
    printf("*a[1]: %u\n", *a[1]);
    printf("(*b)[2]: %u\n",(*b)[2]);

    printf("size of a:%d\n", sizeof(a));  //32  8(pointer len) * [4]
    printf("size of *a:%d\n", sizeof(*a)); //?
    printf("size of b:%d\n", sizeof(b));  //8(pointer len)
    printf("size of *b:%d\n", sizeof(*b)); //16  sizeof(int) * [4]
    
    printf("*a is: 0x%lx\n", (long)*a); //*a is same with a[0]

    return 0;
}
