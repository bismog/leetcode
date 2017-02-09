
#include <stdio.h>
#include <setjmp.h>
jmp_buf BUFFER;
 
 
void trigger_error(int err_code)
{
	longjmp(BUFFER, err_code);
}
 
int main()
{
	int err_code = setjmp(BUFFER);
	if(err_code != 0)
	{
		printf("Error code: %d\n", err_code);
	}
        else
        {
            printf("ret code is zero.\n");
        }

	trigger_error(1);
	trigger_error(2);
 
	return 0;
}
