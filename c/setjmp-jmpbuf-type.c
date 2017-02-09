#include <stdio.h>
#include <setjmp.h>
 
int funca()
{
    jmp_buf BUFFER;
    int err_code = setjmp(BUFFER);
    if(err_code != 0)
    {
        printf("Error code: %d\n", err_code);
        return 1;
    }

    
    longjmp(BUFFER, err_code);

    return 0;
}

int main()
{
    funca();
    return 0;
}
