#include <stdio.h>

void arrayTest(char str[])
{
    printf("size of str: %d\n", sizeof(str));
}

int main(int argc, char* argv[])
{
    char str1[20] = "I Love U,abcdefg";
    arrayTest(str1); 
    return 0;
}
