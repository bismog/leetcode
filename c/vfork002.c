#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>

int glob = 0;
int main(void)
{
    int val = 8;
    pid_t pid;

    if((pid=vfork())<0)
        printf("vfork error!\n");
    else if(pid==0)
    {
        glob++;
        val++;
    }

    printf("pid=%d,glob=%d,val=%d\n",getpid(),glob,val);
    exit(0);
}
