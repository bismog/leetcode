#include <stdio.h>


int singleNumber(int A[], int n) {
    //特殊情况1,2  
    int i = 0;

    if(n<=0) return -1;
    if(n==1) return A[0];

    int result = 0;
    for (i = 0; i < n; i ++) {
        result = result ^ A[i];
    }
    return result;
}

int main()
{
    int arr[10] = {2, 3, 2 , 5 , 4 , 2, 3, 4};
    int o = 0;
    int out = 0;

    out = singleNumber(arr, 5);
    printf("result: %d.\n" ,out);
}
