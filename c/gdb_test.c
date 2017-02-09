#include <stdio.h>

int func(int n)
{
        int sum=0,i;
        for(i=0; i<n; i++)
        {
                sum+=i;
        }
        return sum;
}


main()
{
        int mi;
        long result = 0;
        for(mi=1; mi<=100; mi++)
        {
                result += mi;
        }

       printf("result[1-100] = %d \n", result );
       printf("result[1-250] = %d \n", func(250) );
}

