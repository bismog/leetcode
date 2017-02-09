/*//////////////////////////////////////////////////////////////////////////*/
/*////////////////////////////     Include     //////////////////////////////////*/
/*//////////////////////////////////////////////////////////////////////////*/

//#include "dhcp.h"

#include <stdio.h>


/*//////////////////////////////////////////////////////////////////////////*/
/*//////////////////////////    Flow Context    /////////////////////////////////*/
/*//////////////////////////////////////////////////////////////////////////*/


typedef struct  
{
    short    wVerType; 
    char      ucNewOrOld;               
    char      ucVerNum;                  /**< 请求的版本数量 */
    short    wFuncType[10];   
    char      aucReserve[40];
} T_Rq;

typedef struct  
{
	char      ucNewOrOld;     
    short    wVerType; 
    char      ucVerNum;                  /**< 请求的版本数量 */
    short    wFuncType[10];   
    char      aucReserve[40];
} T_Rq1;

typedef struct  
{
	char      ucNewOrOld;     
    short    wVerType; 
    char      ucVerNum;                  /**< 请求的版本数量 */
    short    wFuncType[10];   
    char      aucReserve[40];
} __attribute__((packed))T_Rq2;

typedef struct  
{
	char      ucNewOrOld;     
    short    wVerType; 
    char      ucVerNum;                  /**< 请求的版本数量 */
	char      ucppp1;   
    short    wFuncType[10];   
    char      aucReserve[40];
} T_Rq3;


typedef struct  
{
	char      ucNewOrOld;     
    short    wVerType; 
    char      ucVerNum;                  /**< 请求的版本数量 */
	short      ucppp1;   
    short    wFuncType[10];   
    char      aucReserve[40];
} T_Rq4;



int main()
{

	printf("sizeof T_Rq is %d.\n", sizeof(T_Rq));
	printf("sizeof T_Rq1 is %d.\n", sizeof(T_Rq1));
	printf("sizeof T_Rq2 is %d.\n", sizeof(T_Rq2));
	printf("sizeof T_Rq3 is %d.\n", sizeof(T_Rq3));
	printf("sizeof T_Rq4 is %d.\n", sizeof(T_Rq4));
	
	
	
	return 0;

}

