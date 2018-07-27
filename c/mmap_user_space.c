#include <sys/mman.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>

int main()
{
    char *ptr = NULL;
    int fd = open("/dev/mmap0", O_RDWR);
    if (fd < 0) {
        printf("open fail\n");
        return 1;
    }

    ptr = mmap(0, 90, PROT_WRITE|PROT_READ, MAP_SHARED, fd, 0);
    // printf("ptr= [%s]\n", ptr);
    ptr[2] = 'c';
    printf("ptr= [%s]\n", ptr);
}
