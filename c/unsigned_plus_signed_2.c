#include <stdio.h>

int main()
{
    int i,j;
    unsigned int x,y,z;
    i = -5;
    z = 2;
    x = i+z; //unsigned result
    j = i+z; //signed result
    printf("\033[31m  i=-5;\n  z=2;\n  x=i+z;\n  j=i+z;  \033[0m\n");
    //the follow 3 lines mean result store in machine always same, no matter signed or unsigned format
    printf("i+z=%d  \n",i+z);
    printf("x=%d  \n",x);
    printf("j=%d  \n",j);

    //the follow 4 lines mean that the default type of result is unsigned(while one unsigned plus one signed)
    if(i+z>2)
        printf("i+z>2  \n");
    else 
        printf("i+z<2  \n"); 

    if((int)(i+z)>2)
        printf("i+z>2  \n");
    else 
        printf("i+z<2  \n"); 

    return 0;
}
