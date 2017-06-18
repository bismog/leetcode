/* -*- coding:utf-8 -*- */


#include <stdio.h>

void while_loop()
{
    int uc = 0;

    while(10 > uc++)
    {
        printf("uc: %u. \n", uc);
    }
}

void for_loop()
{
    int uc = 0;

    for(uc = 0; uc < 10; uc++)
    {
        printf("uc: %u. \n", uc);
    }
}

int main()
{
    while_loop();
    for_loop();
}
