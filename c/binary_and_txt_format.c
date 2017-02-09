# conclusion: in operation-system like UNIX / LINUX, fopen with or without 'b' has no difference.
#include <stdio.h>
#include<string.h>

typedef unsigned char BYTE;
typedef unsigned short WORD16;
typedef unsigned int WORD32;
typedef char CHAR;

typedef struct {
    WORD16 VerBodyCrc;		/**< 版本校验和 *//* 0 */
    WORD16 signature;		/**<  版本头标识:"V3、V4、T8000等" *//* 2 */
    WORD32 sections;		/**< 未使用，为与V3保持一致保留下来*//* 4 */
    WORD32 lowest;		/**< lowest address *//* 8 */
    WORD32 highest;		/**< highest address    *//* 12 */
    BYTE version[32];		/**< 未使用，为与V3保持一致保留下来*//* 16 */
    WORD32 lowestadd;		/**< 附加校验地址 = lowest *//* 48 */
    WORD32 checkvalue;		/**< 附加校验特殊值 = 0xeaeaeaea *//* 52 */
    WORD16 phybrdtype;		/**< 物理板类型 *//* 56 */
    WORD16 logicbrdtype;	/**< 逻辑板类型：V3使用 *//* 58 */
    WORD16 vertype;		/**< 版本类型:配置、CPU版本、DSP版本等*//* 60 */
    WORD16 verfunctype;		/**< 版本功能类型 *//* 62 */
    WORD16 cputype;		/**< cpu类型 *//* 64 */
    WORD16 VerHeadSize;		/**< 文件头长度，V3为保留字节 *//* 66 */
    WORD32 verno;		/**< 内部版本号：跟随版本发布 *//* 68 */
    WORD32 pcbno;		/**< 前3个字节表示生产批次，后1个字节表示PCB号，对于CPU类型版本，表示物理单板PCB；对于子卡版本，表示子卡PCB *//* 72 */
    WORD32 fileh_binno;	/**< 版本头的版本号：做版本头升级用 *//* 76 */
    WORD32 maketime;		/**< 版本制作时间 *//* 80 */
    WORD32 MemoryNeeded;	/**< cpu版本运行需要的内存 *//* 84 */
    WORD16 Compressed;		/**< cpu版本是否压缩标识 *//* 88 */
    BYTE BootType;		/**< debug0x11;release0x22;else:0xff *//* 90 */
    BYTE MulFlags;		/**<  没有使用*//* 91 */
    WORD32 SectionSize;		/**< 文件大小 *//* 92 */
    WORD32 NextSection;		/**< 下一个文件偏移*//* 96 */
    WORD32 ExtVerNo;		/**< 外部版本号：对局方用户呈现*//* 100 */
    WORD32 BomId;		/**< 料单:母板、子卡，暂时不用 *//* 104 */
    BYTE VerPkgType;		/**< 版本包类型：基本包、应用包等 *//* 108 */
    BYTE VerIsSep;		/**< 版本可拆分标志：标志链式文件 *//* 109 */
    BYTE ucRsv1[6];		/**< 填充字，用于扩展*//* 110 */
    WORD32 VerPkgId;		/**< 版本包版本号 *//* 116 */
    CHAR VerFileName[80];	/**< 版本文件名 *//* 120 */
    BYTE Reserve[52];		/**< 保留字节，后续扩展 *//* 200 */
    WORD16 DevIndex;		/**< 设备索引：比如多种CPU跑不同版本时，标志CPU编号 *//* 252 */
    WORD16 VerHeadCrc;		/**< 文件头校验和：计算时不计入此字段 *//* 254 */
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

