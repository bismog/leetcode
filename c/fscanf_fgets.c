# include <stdio.h>

# define BUF_SIZE  20

int play_fscanf()
{
    char buffer[BUF_SIZE];
    FILE *fp; 

    fp = fopen("./beread.sample", "r");
    while(!feof(fp)) {
        fscanf(fp, "%20s", buffer);
        printf("%s", buffer);
    }
    fclose(fp);
    return 0;
}

int play_fgets()
{
    char buffer[BUF_SIZE];
    char ch;
    FILE *fp; 

    fp = fopen("./beread.sample", "r");
//    while(!feof(fp)) {
//        if(fgets(buffer, BUF_SIZE, fp) == NULL) {
//            printf("%s", buffer);
//            break;
//        }
//    }
    while(!feof(fp)) {
        fgets(buffer, BUF_SIZE, fp);
        //if(buffer[sizeof buffer - 1] == '\0' && buffer[sizeof buffer -1] != '\n') {
        if(buffer[BUF_SIZE - 1] == '\0' && buffer[BUF_SIZE -1] != '\n') {
            // Read and toss
            do {
                ch = fgetc(fp);
            }while(ch != '\n' && ch != EOF);
        }
    }
    fclose(fp);
    return 0;
}

int main()
{
//    printf("Play fscanf...\n");
//    play_fscanf();
    printf("Play fgets...\n");
    play_fgets();
    return 0;
}
