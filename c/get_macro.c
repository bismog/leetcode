#include <stdlib.h>
#include <stdio.h>

#define STR(x) #x
#define PRINT(expr) (fprintf(stdout, "%s -> %d\n", STR(expr), (expr)))

#define GLOBAL_FLOATING_IP   0x0a141e26

int main(void)
{
    int xxx_xxx = 7;

    PRINT(xxx_xxx);
    PRINT(GLOBAL_FLOATING_IP);
    printf("%s\n", STR(GLOBAL_FLOATING_IP));
    return EXIT_SUCCESS;
}
