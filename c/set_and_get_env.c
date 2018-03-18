#include <stdio.h>
#include <stdlib.h>

/* This example came from https://www.lemoda.net/c/set-get-env/ */
static void run_get_env(const char * name)
{
    char * value;

    value = getenv(name);
    if (! value) {
        printf ("'%s' is not set.\n", name);
    }
    else {
        printf ("%s = %s\n", name, value);
    }
}

int main()
{
    char * name = "foo";

    /* Variable is not set */
    run_get_env(name);

    /* Write into empty variable */
    setenv("foo", "chops", 0);
    run_get_env(name);

    /* This doesn't change because 'overwrite' is 0. */
    setenv("foo", "drops", 0);
    run_get_env(name);

    /* This change the value because 'overwrite' is 1. */
    setenv("foo", "drops", 1);
    run_get_env(name);

    return 0;
}
