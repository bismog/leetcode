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
    WORD32  dwJno;          /**< JOB号, 高16位为JOB 类型, 低16位为JOB 实例号 */
    WORD32  dwDevId;        /**< 设备ID, 包含本局的局号信息, 高8位为局号，不支持传递其他信息*/
    WORD16  wModule;        /**< MP编号 */
    WORD16  wUnit;          /**< 单板号 */
    BYTE    ucSUnit;        /**< 单板上的处理器号 */
    BYTE    ucSubSystem;    /**< 子系统号 */
    BYTE    ucRouteType;    /**< 路由类型，区别业务/管理消息，左右板位，主备通信*/
    BYTE    ucExtendFlag;   /**< 扩展标志 */
}JID;


typedef struct 
{
    WORD16  wSystem;       /**<   系统号 */
    WORD16  wModule;        /**< MP编号 */
    WORD16  wUnit;          /**< 单元号 */
    WORD16  wIndex;        /**< 索引号，在子单元号内部编号 */
    BYTE    ucSubSystem;    /**< 子系统号 */
    BYTE    ucSUnit;        /**< 单板上的处理器和业务处理芯片编号 */
    BYTE    ucPad[2];      /**< 填充字节，拼凑成DWORD*/
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
    BYTE    regCount;             /* 重发注册请求次数 */
    BYTE    regStatus;              /* 注册状态*/
    WORD16  jobMSStatus;               /* job当前主备状态*/
    WORD16  jobState;                /* job状态机*/
    BOOLEAN isServsetNotifyTimerSet; /* 服务集表变化通知超时是否已设置*/
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
