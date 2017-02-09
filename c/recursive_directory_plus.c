#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <string.h>
#include <errno.h>
/* "readdir" etc. are defined here. */
#include <dirent.h>
/* limits.h defines "PATH_MAX". */
#include <limits.h>

#define MAX_FILE_CNT 30000

/* List the files in "dir_name". */
static void list_dir (const char * dir_name, char **fl, int *cur)
{
    DIR * d;

    /* Open the directory specified by "dir_name". */
    d = opendir (dir_name);

    /* Check it was opened. */
    if (! d) {
        fprintf (stderr, "Cannot open directory '%s': %s\n",
                dir_name, strerror (errno));
        exit (EXIT_FAILURE);
    }
    while (1) {
        struct dirent * entry;
        const char * d_name;

        /* "Readdir" gets subsequent entries from "d". */
        entry = readdir (d);
        if (! entry) {
            /* There are no more entries in this directory, so break out of the while loop. */
            break;
        }
        d_name = entry->d_name;
#if 0
        /* Print the name of the file and directory. */
        //printf ("%s/%s\n", dir_name, d_name);
        printf ("%s/%s\t\t----%s\n", dir_name, d_name, (entry->d_type & DT_DIR)?"D":"F");

#else
        /* If you don't want to print the directories, use the following line: */
        if (! (entry->d_type & DT_DIR)) {
            //printf ("%s/%s\n", dir_name, d_name);
            if (*cur >= MAX_FILE_CNT) {
                fprintf (stderr, "Too many files.\n");
                exit (EXIT_FAILURE);
            }
            snprintf(fl[(*cur)++], PATH_MAX, "%s/%s", dir_name, d_name);
        }
#endif /* 0 */


        if (entry->d_type & DT_DIR) {
            /* Check that the directory is not "d" or d's parent. */
            if (strcmp (d_name, "..") != 0 && strcmp (d_name, ".") != 0) {
                int path_length;
                char path[PATH_MAX];

                path_length = snprintf (path, PATH_MAX, "%s/%s", dir_name, d_name);
                //printf ("%s\n", path);
                if (path_length >= PATH_MAX) {
                    fprintf (stderr, "Path length has got too long.\n");
                    exit (EXIT_FAILURE);
                }
                /* Recursively call "list_dir" with the new path. */
                list_dir (path, fl, cur);
            }
        }
    }
    /* After going through all the entries, close the directory. */
    if (closedir (d)) {
        fprintf (stderr, "Could not close '%s': %s\n", dir_name, strerror (errno));
        exit (EXIT_FAILURE);
    }
}

int main ()
{
    int i = 0;
    int cur = 0;
    char **flist;

    /* max_file_cnt is the number of rows  */
    if (( flist = malloc( MAX_FILE_CNT*sizeof( char* ))) == NULL )
    { /* error */ }

    for ( i = 0; i < MAX_FILE_CNT; i++ )
    {
        /* x_i here is the size of given row, no need to
         * multiply by sizeof( char ), it's always 1
         */
        if (( flist[i] = malloc(PATH_MAX)) == NULL )
        { /* error */ }

        /* probably init the row here */
        memset(flist[i], 0, PATH_MAX*sizeof(char));
    }

    /* access matrix elements: c[i] give you a pointer
     * to the row array, c[i][j] indexes an element
     */
    list_dir ("/usr/share", flist, &cur);
    for (i=0; i<cur; i++) {
        if(strlen(flist[i]) != 0) {
            printf("%s\n", flist[i]);
        }
    }
    
    free(flist);
    return 0;
}
