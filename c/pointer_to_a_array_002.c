#include <stdio.h>

int main()
{
    int i;
    int c[4]={1,2,3,4};
    int *a[4]; //ָ������
    int (*b)[4]; //����ָ��
    b=&c;
    //������c��Ԫ�ظ�������a
    for(i=0;i<4;i++)
    {
        a[i]=&c[i];
        printf("a[%d] is: 0x%lx\n", i, a[i]);
    }
    //������½��
    printf("*a[1]: %u\n", *a[1]);
    printf("(*b)[2]: %u\n",(*b)[2]);

    printf("size of a:%d\n", sizeof(a));  //32  8(pointer len) * [4]
    printf("size of *a:%d\n", sizeof(*a)); //?
    printf("size of b:%d\n", sizeof(b));  //8(pointer len)
    printf("size of *b:%d\n", sizeof(*b)); //16  sizeof(int) * [4]
    
    printf("*a is: 0x%lx\n", (long)*a); //*a is same with a[0]

    return 0;
}
