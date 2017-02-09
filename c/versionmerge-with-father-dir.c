





void _inputFilePathHandle(char *pfilepath)
{
    char actemp[MERGE_LINE_SIZE] ;
    WORD16  i;
    BYTE flag =0 ; 
    WORD16  wlength = strlen(pfilepath) ;
    strcpy(actemp, pfilepath );
    if(0==wlength)
    {
        return;
    }
    for ( i = wlength  ;  ; i--)
    {
        if( (actemp[i] == '/') ||( actemp[i] == '\\' ))
        {
            flag =1;
            break;
        }
    }
    if(flag ==0 )
    {
        return;
    }
    memset(pfilepath , 0 , MERGE_LINE_SIZE);
    memcpy(pfilepath, actemp+i +1, wlength -i );
}
