#include <setjmp.h>
#include <stdio.h>

jmp_buf mark;

int Sub_Func()
{
int jmpret, be_modify;

be_modify = 0;

jmpret = setjmp( mark );
if( jmpret == 0 )
{
// ���������ִ��
}
else
{
// ������ģ��
switch (jmpret)
{
case 1:
printf( "Error 1n");
break;
case 2:
printf( "Error 2n");
break;
case 3:
printf( "Error 3n");
break;
default :
printf( "Unknown Error");
break;
}

//ע����һ��䣬�������������˳�
if (be_modify==0) exit(0);
}

return jmpret;
}

int main( void )
{
	Sub_Func();

	// ע�⣬��Ȼlongjmp�ĵ�������setjmp֮�󣬵�����������setjmp�����÷�Χ��
	longjmp(mark, 1);

    return 0 ;
}
