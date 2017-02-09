#include <stdio.h>

struct test1 {
    char a:1;
    char:2;
    long b:3;
    char c:2;
}; // size: long 8bytes

struct test2 {
    char a:1;
    char:2;
    char b:3;
    long c:2;
}; // size: long 8bytes 

struct test3 {
    char a:1;
    char:2;
    char b:3;
    char c:2;
}; // size: 1byte

struct bs
{
    int a:8;
    int b:2;
    int c:6;
}; //size: int 4bytes

struct test5 {
    char a:1;
    char:2;
    long b:3;
    char c:2;
    int d;
    char e;
}; //size: long + (int + char)(if not big than 8byteS, fill to 8bytes),8+8=16bytes 

int main()
{
    struct test1 t1;
    struct test2 t2;
    struct test3 t3;
    struct bs t4;
    struct test5 t5;

    int len1 = sizeof(t1);
    int len2 = sizeof(t2);
    int len3 = sizeof(t3);
    int len4 = sizeof(t4);
    int len5 = sizeof(t5);


    printf("size of long:%d\n", sizeof(long));

    printf("len of len1:%d\n", len1);
    printf("len of len2:%d\n", len2);
    printf("len of len3:%d\n", len3);
    printf("len of len4:%d\n", len4);
    printf("len of len5:%d\n", len5);

    return 0;
}
