#include <stdio.h>

int main()
{
    int i;
    char base[20];
    char *arr[20]; 
    char **parr=arr;//�����arr����ָ��Ļ���arrҲ��ָ����ʽ 
    char *str; 

    for(i=0; i<20; i++)
    {
        base[i] = i;
        arr[i] = &base[i];
    }

    str=*parr;//*parr��ָ����ʽ 
    str=*(parr+1);//*(parr+1)��ָ����ʽ 
    str=*(parr+2);//*(parr+2)��ָ����ʽ 
    
    printf("*str is: %d\n", *str);
    printf("**parr is: %d\n", **parr);

    printf("parr is: 0x%lx\n", parr);
    printf("&base is: 0x%lx\n", &base);
    printf("&arr is: 0x%lx\n", &arr);
    printf("&str is: 0x%lx\n", &str);
    printf("str is: 0x%lx\n", str);

    return 0;
}
