#include <stdio.h>

int array[20]; 

int main()
{
    int i;
    int *ptr; 

    for(i=0; i<20; i++)
    {
        array[i] = 2;
    }

    ptr=array;

    //此处略去为整型数组赋值的代码。 
    for(i=0;i<20;i++) 
    { 
        (*ptr)++;
        ptr++;
    } 

    for(i=0; i<20; i++)
    {
        printf("array[i]: %d\t", array[i]);
    }

    return 0;
}
