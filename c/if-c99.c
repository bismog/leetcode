#include <stdio.h>

int main(void)
{
#ifdef __STDC__
     printf("%s\n", "stardard C");
#endif
#ifdef __STDC_VERSION__
     printf("%i\n", __STDC_VERSION__);
#endif
     return 0;
}

