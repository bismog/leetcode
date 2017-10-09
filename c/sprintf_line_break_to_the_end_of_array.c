# include <stdio.h>
# include <string.h>

int main()
{
    char buf[20];
    int len = strlen(buf);
    //int len = 0;
    int rlen = 0;
    int i = 0;

    for(i=0; i<20; i=i+1) {
        rlen = sprintf(&buf[strlen(buf)], "%s", "\r\n");
        printf("%d: rlen is %d.\n", i, rlen);
    }

    return 0;
}
