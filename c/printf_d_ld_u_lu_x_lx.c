#include <stdio.h>

int main()
{
    unsigned char ucXXX;
    unsigned short usXXX;
    unsigned int uiXXX;
    unsigned long ulXXX;

    ucXXX = 0xfe;
    usXXX = 0xfedc;
    uiXXX = 0xfedcba98;
    ulXXX = 0xfedaba9876543210;

    //printf("sizeof unsigned int is: %lu", sizeof(unsigned int));
    //printf("sizeof unsigned long is: %lu", sizeof(unsigned long));

    printf("%%d of ucXXX: %d.\n", ucXXX);
    printf("%%ld of ucXXX: %ld.\n", ucXXX);
    printf("%%u of ucXXX: %u.\n", ucXXX);
    printf("%%lu of ucXXX: %lu.\n", ucXXX);
    printf("%%x of ucXXX: %x.\n", ucXXX);
    printf("%%lx of ucXXX: %lx.\n", ucXXX);

    printf("%%d of usXXX: %d.\n", usXXX);
    printf("%%ld of usXXX: %ld.\n", usXXX);
    printf("%%u of usXXX: %u.\n", usXXX);
    printf("%%lu of usXXX: %lu.\n", usXXX);
    printf("%%x of usXXX: %x.\n", usXXX);
    printf("%%lx of usXXX: %lx.\n", usXXX);

    printf("%%d of uiXXX: %d.\n", uiXXX);
    printf("%%ld of uiXXX: %ld.\n", uiXXX);
    printf("%%u of uiXXX: %u.\n", uiXXX);
    printf("%%lu of uiXXX: %lu.\n", uiXXX);
    printf("%%x of uiXXX: %x.\n", uiXXX);
    printf("%%lx of uiXXX: %lx.\n", uiXXX);

    printf("%%d of ulXXX: %d.\n", ulXXX);
    printf("%%ld of ulXXX: %ld.\n", ulXXX);
    printf("%%u of ulXXX: %u.\n", ulXXX);
    printf("%%lu of ulXXX: %lu.\n", ulXXX);
    printf("%%x of ulXXX: %x.\n", ulXXX);
    printf("%%lx of ulXXX: %lx.\n", ulXXX);

    return 0;
}
