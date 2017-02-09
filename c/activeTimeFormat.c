
#include "stdio.h"
#include "stdlib.h"

#define YEAR_MASK    0xFFF00000
#define MONTH_MASK   0xF0000
#define DAY_MASK     0xF800
#define HOUR_MASK    0x7C0
#define MINUTE_MASK  0x3F

int main ( int argc, char *argv[] )
{
    int ch;
    FILE *in;
    FILE *out;

    if ( argc != 2 ) {
        fprintf ( stderr, "Usage: %s <activetime> \n", argv[0] );
        exit ( EXIT_FAILURE );
    }

    //in = open_file ( argv[1], "r" );
    unsigned int year, month, day, hour, minute;
    unsigned int input_time;
    input_time = atoi(argv[1]);

    year = (input_time & YEAR_MASK) >> 20;
    month = (input_time & MONTH_MASK) >> 16;
    day = (input_time & DAY_MASK) >> 11;
    hour = (input_time & HOUR_MASK) >> 6;
    minute = input_time & MINUTE_MASK;

    printf("formatted time is %u/%u/%u %u:%u(y/m/d h:m)\n", year, month, day, hour, minute);

    return 0;
}
