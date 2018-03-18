#include <stdio.h>
#include <stdlib.h>

/*
https://stackoverflow.com/questions/16082593/how-to-export-integer-value-to-the-environment-variable-in-c
The environment can only hold string values. To store an integer you will have 
to convert it to a string and then store that. When reading it you can then 
convert the string back to an integer.
*/

/* cmladd: No need to store integer, store a string,
then get and atoi convert. */

#define MASTER  1
#define SLAVE   2

int main()
{
    char env_var[20]; // length of 'ENV_VAR=' plus 12
    char *state;
    setenv("MS_STATE", "1", 0);
    state = getenv("MS_STATE");
    if(atoi(state) == MASTER) {
        printf("current state is Master.\n");
    }
    else if(atoi(state) == SLAVE) {
        printf("current state is Slave.\n");
    }
    else {
        printf("unknown state.\n");
    }

    return 0;
}
