# conclusion: in operation-system like UNIX / LINUX, fopen with or without 'b' has no difference.
#include <stdio.h>
#include<string.h>

typedef unsigned char BYTE;
typedef unsigned short WORD16;
typedef unsigned int WORD32;
typedef char CHAR;

typedef struct {
    WORD16 VerBodyCrc;		/**< �汾У��� *//* 0 */
    WORD16 signature;		/**<  �汾ͷ��ʶ:"V3��V4��T8000��" *//* 2 */
    WORD32 sections;		/**< δʹ�ã�Ϊ��V3����һ�±�������*//* 4 */
    WORD32 lowest;		/**< lowest address *//* 8 */
    WORD32 highest;		/**< highest address    *//* 12 */
    BYTE version[32];		/**< δʹ�ã�Ϊ��V3����һ�±�������*//* 16 */
    WORD32 lowestadd;		/**< ����У���ַ = lowest *//* 48 */
    WORD32 checkvalue;		/**< ����У������ֵ = 0xeaeaeaea *//* 52 */
    WORD16 phybrdtype;		/**< ��������� *//* 56 */
    WORD16 logicbrdtype;	/**< �߼������ͣ�V3ʹ�� *//* 58 */
    WORD16 vertype;		/**< �汾����:���á�CPU�汾��DSP�汾��*//* 60 */
    WORD16 verfunctype;		/**< �汾�������� *//* 62 */
    WORD16 cputype;		/**< cpu���� *//* 64 */
    WORD16 VerHeadSize;		/**< �ļ�ͷ���ȣ�V3Ϊ�����ֽ� *//* 66 */
    WORD32 verno;		/**< �ڲ��汾�ţ�����汾���� *//* 68 */
    WORD32 pcbno;		/**< ǰ3���ֽڱ�ʾ�������Σ���1���ֽڱ�ʾPCB�ţ�����CPU���Ͱ汾����ʾ������PCB�������ӿ��汾����ʾ�ӿ�PCB *//* 72 */
    WORD32 fileh_binno;	/**< �汾ͷ�İ汾�ţ����汾ͷ������ *//* 76 */
    WORD32 maketime;		/**< �汾����ʱ�� *//* 80 */
    WORD32 MemoryNeeded;	/**< cpu�汾������Ҫ���ڴ� *//* 84 */
    WORD16 Compressed;		/**< cpu�汾�Ƿ�ѹ����ʶ *//* 88 */
    BYTE BootType;		/**< debug0x11;release0x22;else:0xff *//* 90 */
    BYTE MulFlags;		/**<  û��ʹ��*//* 91 */
    WORD32 SectionSize;		/**< �ļ���С *//* 92 */
    WORD32 NextSection;		/**< ��һ���ļ�ƫ��*//* 96 */
    WORD32 ExtVerNo;		/**< �ⲿ�汾�ţ��Ծַ��û�����*//* 100 */
    WORD32 BomId;		/**< �ϵ�:ĸ�塢�ӿ�����ʱ���� *//* 104 */
    BYTE VerPkgType;		/**< �汾�����ͣ���������Ӧ�ð��� *//* 108 */
    BYTE VerIsSep;		/**< �汾�ɲ�ֱ�־����־��ʽ�ļ� *//* 109 */
    BYTE ucRsv1[6];		/**< ����֣�������չ*//* 110 */
    WORD32 VerPkgId;		/**< �汾���汾�� *//* 116 */
    CHAR VerFileName[80];	/**< �汾�ļ��� *//* 120 */
    BYTE Reserve[52];		/**< �����ֽڣ�������չ *//* 200 */
    WORD16 DevIndex;		/**< �豸�������������CPU�ܲ�ͬ�汾ʱ����־CPU��� *//* 252 */
    WORD16 VerHeadCrc;		/**< �ļ�ͷУ��ͣ�����ʱ��������ֶ� *//* 254 */
} T_FileHeader;

typedef struct {
    BYTE aaa[16];
    WORD16 bbb[8];
    WORD32 ccc[4];
}T_Bin;

typedef struct {
    char bbb[200];
}T_Str;

int main()
{
    int i;
    T_FileHeader h_bin;
    T_Bin  h_bin2;  
    T_Str  h_str;
    FILE * fpb, *fpb2, *fpt, *fpt2;

    memset(&h_bin, 0xff, sizeof(T_FileHeader));
    h_bin.checkvalue = 0xeaeaeaea;
    h_bin.phybrdtype = 0x1234;
    h_bin.vertype = 0x2;
    h_bin.verfunctype = 0x3;
    h_bin.verno = 0xabcdef49;
    strcpy(h_bin.VerFileName, "fuck_GFW.ddd");

    memset(&h_bin2, 0xff, sizeof(T_Bin));
    for(i=0; i<16; i++)
        h_bin2.aaa[i] = i;
    for(i=0; i<8; i++)
        h_bin2.bbb[i] = i;
    for(i=0; i<4; i++)
        h_bin2.ccc[i] = i;

    memset(&h_str, 0xff, sizeof(T_Str));
    //strcpy(h_str.bbb, "abcdefg_hijklmn");
    h_str.bbb[0] = (char )0x34;
    h_str.bbb[1] = (char )0x35;
    h_str.bbb[2] = (char )0x36;
    h_str.bbb[3] = (char )0x37;

    fpb = fopen("verfile_binary.bin","w+b");
    if(fpb == NULL) return;
    fwrite(&h_bin, sizeof(T_FileHeader), 1, fpb);
    fclose(fpb);

    fpb2 = fopen("verfile_binary2.bin", "w+b");
    if(fpb2 == NULL) return;
    fwrite(&h_bin2, sizeof(T_Bin), 1, fpb2);
    fclose(fpb2);

    fpt = fopen("verfile_txt.txt", "w+");
    if(fpt == NULL) return;
    fwrite(&h_str, sizeof(T_Str), 1, fpt);
    fclose(fpt);

    fpt2 = fopen("verfile_txt2.bin", "w+b");
    if(fpt2 == NULL) return;
    fwrite(&h_str, sizeof(T_Str), 1, fpt2);
    fclose(fpt2);
    return 0;
}

