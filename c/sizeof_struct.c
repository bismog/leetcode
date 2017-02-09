#include "stdio.h"
#include "stdlib.h"
#include "string.h"

/* type definition */
typedef char            CHAR;
typedef unsigned char   BYTE;
typedef unsigned char   UCHAR;
typedef unsigned char   BOOLEAN;
typedef int             BOOL;
typedef int             INT;
typedef long            LONG;
typedef unsigned long   ULONG; 
typedef unsigned long   DWORD;
typedef unsigned short      WORD16;
typedef WORD16          WORD;
typedef signed short        SWORD16;
typedef unsigned long       WORD32;
typedef signed long         SWORD32;

#define  VM_WAIT_SERVSET_CHANGE_NUM_MAX   200
#define  VM_LADDR_SERVSETCFG_NUM_MAX      1000


typedef struct tagJID
{
    WORD32  dwJno;          /**< JOB��, ��16λΪJOB ����, ��16λΪJOB ʵ���� */
    WORD32  dwDevId;        /**< �豸ID, �������ֵľֺ���Ϣ, ��8λΪ�ֺţ���֧�ִ���������Ϣ*/
    WORD16  wModule;        /**< MP��� */
    WORD16  wUnit;          /**< ����� */
    BYTE    ucSUnit;        /**< �����ϵĴ������� */
    BYTE    ucSubSystem;    /**< ��ϵͳ�� */
    BYTE    ucRouteType;    /**< ·�����ͣ�����ҵ��/������Ϣ�����Ұ�λ������ͨ��*/
    BYTE    ucExtendFlag;   /**< ��չ��־ */
}JID;


typedef struct 
{
    WORD16  wSystem;       /**<   ϵͳ�� */
    WORD16  wModule;        /**< MP��� */
    WORD16  wUnit;          /**< ��Ԫ�� */
    WORD16  wIndex;        /**< �����ţ����ӵ�Ԫ���ڲ���� */
    BYTE    ucSubSystem;    /**< ��ϵͳ�� */
    BYTE    ucSUnit;        /**< �����ϵĴ�������ҵ����оƬ��� */
    BYTE    ucPad[2];      /**< ����ֽڣ�ƴ�ճ�DWORD*/
}T_LogicalAddr;

typedef struct 
{
    BYTE    ucRackId;       /**< rack no */
    BYTE    ucShelfId;      /**< shelf no */
    BYTE    ucSlotId;       /**< slot no */
    BYTE    ucCpuId;        /**< cpu no */
}T_PhysAddress;


typedef struct
{
    T_LogicalAddr logicalAddr;
    T_PhysAddress phyAddr;
    BOOLEAN       ifNeedHandle;
}T_ServsetAddr;

typedef struct
{
    BOOLEAN isDbgPrintEnable;
    JID     selfJID;
    BYTE    regCount;             /* �ط�ע��������� */
    BYTE    regStatus;              /* ע��״̬*/
    WORD16  jobMSStatus;               /* job��ǰ����״̬*/
    WORD16  jobState;                /* job״̬��*/
    BOOLEAN isServsetNotifyTimerSet; /* ���񼯱�仯֪ͨ��ʱ�Ƿ�������*/
    BYTE    changedServsetNum;
    WORD32  changedServset[VM_WAIT_SERVSET_CHANGE_NUM_MAX];
    WORD16  notifyAddrNum;
    T_ServsetAddr notifyAddr[VM_LADDR_SERVSETCFG_NUM_MAX+1]; //last one reserved for invalid index
} T_VMCfgMgtJobVar;


int main()
{
    printf("size: %d.\n", sizeof(T_VMCfgMgtJobVar));
    return 0;
}
