#include <stdio.h>  
#include <string.h> 
  
#define P(A) printf("%s:%d\n",#A,A);  
  
int main(int argc, char **argv)  
{  
    int a = 1, b = 2;  
    P(a);  
    P(b);  
    P(a+b);  
    system("pause");  

    return 0;
}  



