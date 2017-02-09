#include <stdio.h>

int main()
{
    int a=12; 
    int b; 
    int *p; 
    int **ptr; 
    p=&a;//&a的结果是一个指针，类型是int*，指向的类型是int，指向的地址 
    //是a的地址。 
    *p=24;//*p的结果，在这里它的类型是int，它所占用的地址是p所指向的地 
    //址，显然，*p就是变量a。 
    ptr=&p;//&p的结果是个指针，该指针的类型是p的类型加个*，在这里是int 
    //**。该指针所指向的类型是p的类型，这里是int*。该指针所指向的地址就是指针 
    //p自己的地址。 
    *ptr=&b;//*ptr是个指针，&b的结果也是个指针，且这两个指针的类型和所 
    //指向的类型是一样的，所以用&b来给*ptr赋值就是毫无问题的了。 
    **ptr=34;//*ptr的结果是ptr所指向的东西，在这里是一个指针，对这个指 
    //针再做一次*运算，结果就是一个int类型的变量。 

    printf("a is: %d\n", a);
    printf("b is: %d\n", b);
    printf("*p is: %d\n", *p);
    printf("**ptr is: %d\n", **ptr);

    return 0;
}
