#include<cstring>
#include<iostream>
using namespace std;

#define uint32 unsigned int
typedef struct _normal_array_t
{
    char a;
    uint32 b;
    int *c;
}__attribute ((packed)) normal_array_t;
 
typedef struct _dynamic_array_t
{
    char a;
    uint32 b;
    int c[]; //c[0] is the same
}__attribute ((packed)) dynamic_array_t;
 
int main()
{
    normal_array_t* n1 = (normal_array_t*)malloc(sizeof(normal_array_t) );
    cout << "n1: before malloc size is " << sizeof(*n1) << endl;
    n1->c = (int*) malloc(100);
    n1->c[50] =  100;
    cout << "n1: after malloc c, n1->c[50] is " << n1->c[50] << endl;
    cout << "n1: after malloc c, size is " << sizeof(*n1) << endl;
    free(n1->c);
    free(n1);
 
    dynamic_array_t* d1 = (dynamic_array_t*)malloc(sizeof(dynamic_array_t) + 100 * sizeof(int) );
    cout << "d1: size is " << sizeof(*d1) << endl;
    d1->c[50] = 200;
    cout << "d1: d1->c[50] is " << d1->c[50] << endl;
    free(d1);
}

