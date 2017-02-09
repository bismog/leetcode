#include "stdio.h"

int main()
{
    unsigned int uit;
    unsigned long ult;
    unsigned long int ulit;
    unsigned long long ullt;
    
    printf("sizeof(uit): %u\t", sizeof(uit));
    printf("sizeof(ult): %u\t", sizeof(ult));
    printf("sizeof(ulit): %u\t", sizeof(ulit));
    printf("sizeof(ullt): %u\t", sizeof(ullt));
}
