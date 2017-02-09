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
// 其它代码的执行
}
else
{
// 错误处理模块
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

//注意这一语句，程序有条件地退出
if (be_modify==0) exit(0);
}

return jmpret;
}

int main( void )
{
	Sub_Func();

	// 注意，虽然longjmp的调用是在setjmp之后，但是它超出了setjmp的作用范围。
	longjmp(mark, 1);

    return 0 ;
}
