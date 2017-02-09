#include <pthread.h>
#include <stdio.h>

typedef struct{
    char character;
    int count;
}char_print_params;

void * char_print(void *args)
{ 
    int i = 0;
    char_print_params params = *(char_print_params *)args;
    
    if(params.count <= 0) {
        return (void *)1;
    }
    for(i=0; i<params.count; i++) {
        printf("%c", params.character);
    }

    return (void *)0;
}

int main ()
{
    pthread_t thread1_id;
    pthread_t thread2_id;
    char_print_params thread1_args;
    char_print_params thread2_args;
    /* Create a new thread to print 30,000 x’s. */
    thread1_args.character = 'x';
    thread1_args.count = 3000;
    pthread_create (&thread1_id, NULL, &char_print, &thread1_args);
    /* Create a new thread to print 20,000 o’s. */
    thread2_args.character = 'o';
    thread2_args.count = 2000;
    pthread_create (&thread2_id, NULL, &char_print, &thread2_args);
    /* Make sure the first thread has finished. */
    pthread_join (thread1_id, NULL);
    /* Make sure the second thread has finished. */
    pthread_join (thread2_id, NULL);
    /* Now we can safely return. */
    return 0;
}
