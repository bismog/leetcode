#include <stdio.h>

int main()
{
    int a=12; 
    int b; 
    int *p; 
    int **ptr; 
    p=&a;//&a�Ľ����һ��ָ�룬������int*��ָ���������int��ָ��ĵ�ַ 
    //��a�ĵ�ַ�� 
    *p=24;//*p�Ľ��������������������int������ռ�õĵ�ַ��p��ָ��ĵ� 
    //ַ����Ȼ��*p���Ǳ���a�� 
    ptr=&p;//&p�Ľ���Ǹ�ָ�룬��ָ���������p�����ͼӸ�*����������int 
    //**����ָ����ָ���������p�����ͣ�������int*����ָ����ָ��ĵ�ַ����ָ�� 
    //p�Լ��ĵ�ַ�� 
    *ptr=&b;//*ptr�Ǹ�ָ�룬&b�Ľ��Ҳ�Ǹ�ָ�룬��������ָ������ͺ��� 
    //ָ���������һ���ģ�������&b����*ptr��ֵ���Ǻ���������ˡ� 
    **ptr=34;//*ptr�Ľ����ptr��ָ��Ķ�������������һ��ָ�룬�����ָ 
    //������һ��*���㣬�������һ��int���͵ı����� 

    printf("a is: %d\n", a);
    printf("b is: %d\n", b);
    printf("*p is: %d\n", *p);
    printf("**ptr is: %d\n", **ptr);

    return 0;
}