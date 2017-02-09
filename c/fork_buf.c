#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
 
int main(void)
{
    int i;
    for(i=0; i<2; i++){
        //   printf("|");
        pid_t pid = fork();
        //pid_t pid = vfork();
        if(0 == pid) {
            printf("this is child process!\n");
        } 
        else {
            printf("this is parent process!\n");
        }
        printf("-\n");
    }

    _exit(0);
    return 0;
}
