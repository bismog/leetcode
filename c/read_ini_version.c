#include "stdio.h"
#include "string.h"

int read_version(char *file)
{
    FILE*fp;
    char c1[100];
    char c[10][100];
    int i = 0 ;
    char * p ;
    int num[4]={0};
    unsigned int VersionNo= 0 ;

    if((fp=fopen(file,"r"))==NULL){
        printf("open file[%s] failed \n",file);
        return 0xff ;
    }

    while(fscanf(fp,"%s",c1)==1)
    {
        if(i >= 4)
        {
            printf(" out of the max index[%d] \n",i);
            fclose(fp);
            return 0xff ;
        }
        //printf("%d %s \n",i,c1);
        memcpy(c[i],c1,sizeof(c1));
        //printf("%d %s  %d\n",i,c[i],sizeof(c1));
        p = strrchr(c[i],'=');
        printf("result[str %s], ",p+1);
        num[i] = atoi(p+1);
        printf("    --  int[%d]:[%d]\n",i,num[i]%255);
        i++;
     }
     VersionNo |= (((unsigned int)num[0]) << 24);
     VersionNo |= (((unsigned int)num[1]) << 16);
     VersionNo |= (((unsigned int)num[2]) << 8);
     VersionNo |= (((unsigned int)num[3]) );
     //printf(" VersionNo[0X%x]\n ",VersionNo);


    if(fclose(fp)!=0)
        return 0xff;
    return VersionNo;
}

int main()
{
    char file_path[100];
    unsigned int ver = 0;

    strcpy(file_path, "/tmp/version.ini");
    ver = read_version(file_path);
    printf("version is 0x%x.\n", ver);

    return 0;
}
