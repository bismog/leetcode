#include "stdio.h"
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main()
{
    struct in_addr  iaddr;
    int out_ip;
    char *str="128.0.0.1";

    inet_aton(str, &iaddr);
    out_ip = iaddr.s_addr;
    printf("ip:0x%x.\n", out_ip);

    return 0;
}
