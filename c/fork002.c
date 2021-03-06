#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>

int glob = 0;
int main(void)
{
    int val = 8;
    pid_t pid;

    if((pid=fork())<0)
        printf("fork error!\n");
    else if(pid==0) //child
    {
        glob++;
        val++;
    }
    else   //parent
    {
        sleep(2);//wait child process
    }

    printf("pid=%d,glob=%d,val=%d\n",getpid(),glob,val);
    exit(0);
}
