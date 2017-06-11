#include <stdio.h>

int our_function(int num_numbers, int *numbers) {
    int i;
    int sum=0;
    printf("1. sum is %d\n", sum);
    for (i = 0; i < num_numbers; i++) {
        sum += numbers[i];
    }
    printf("2. sum is %d\n", sum);
    return sum;
}
