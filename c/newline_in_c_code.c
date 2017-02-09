#include <stdlib.h>
#include <stdio.h>
int main(int argc, char **argv)
{
    if (argc != 2) {
        printf("I need a single argument,which must\
                be a dictionary\n");
        exit(1);
    }
    return 0;
}
