#ifndef __CHECKIP_H
#define __CHECKIP_H

struct arpMsg {
    struct ethhdr ethhdr;       /* Ethernet header */
    u_short htype;              /* hardware type (must be ARPHRD_ETHER) */
    u_short ptype;              /* protocol type (must be ETH_P_IP) */
    u_char  hlen;               /* hardware address length (must be 6) */
    u_char  plen;               /* protocol address length (must be 4) */
    u_short operation;          /* ARP opcode */
    u_char  sHaddr[6];          /* sender's hardware address */
    u_char  sInaddr[4];         /* sender's IP address */
    u_char  tHaddr[6];          /* target's hardware address */
    u_char  tInaddr[4];         /* target's IP address */
    u_char  pad[18];            /* pad for min. Ethernet payload (60 bytes) */
};

struct server_config_t {
    u_int32_t server;       /* Our IP, in network order */
    u_int32_t start;        /* Start address of leases, network order */
    u_int32_t end;          /* End of leases, network order */
    struct option_set *options; /* List of DHCP options loaded from the config file */
    char *interface;        /* The name of the interface to use */
    int ifindex;            /* Index number of the interface to use */
    unsigned char arp[6];       /* Our arp address */
    unsigned long lease;        /* lease time in seconds (host order) */
    unsigned long max_leases;   /* maximum number of leases (including reserved address) */
    char remaining;         /* should the lease file be interpreted as lease time remaining, or * as the time the lease expires */
    unsigned long auto_time;    /* how long should udhcpd wait before writing a config file.  * if this is zero, it will only write one on SIGUSR1 */
    unsigned long decline_time;     /* how long an address is reserved if a client returns a * decline message */
    unsigned long conflict_time;    /* how long an arp conflict offender is leased for */
    unsigned long offer_time;   /* how long an offered address is reserved */
    unsigned long min_lease;    /* minimum lease a client can request*/
    char *lease_file;
    char *pidfile;
    char *notify_file;      /* What to run whenever leases are written */
    u_int32_t siaddr;       /* next server bootp option */
    char *sname;            /* bootp server name */
    char *boot_file;        /* bootp boot file option */
};

#endif /* __CHECKIP_H */


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <time.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>

#include <netinet/in.h>
#include <netinet/if_ether.h>
#include <net/if.h>
#include <net/if_arp.h>
#include <arpa/inet.h>

#include "checkip.h"

#define MAC_BCAST_ADDR      (unsigned char *) "/xff/xff/xff/xff/xff/xff"
#define ETH_INTERFACE       "eth0"

struct server_config_t server_config;

int main(int argc, char *argv[])
{
    if(argc < 2)
    {
        printf("Usage: checkip ipaddr/n");
        exit(0);
    }

    if (read_interface(ETH_INTERFACE, &server_config.ifindex,
               &server_config.server, server_config.arp) < 0)
    {
        exit(0);
    }

    if(check_ip(inet_addr(argv[1])) == 0)
    {
        printf("IP:%s can use/n", argv[1]);
    }
    else
    {
        printf("IP:%s conflict/n", argv[1]);
    }

    return 0;
}


int read_interface(char *interface, int *ifindex, u_int32_t *addr, unsigned char *arp)
{
    int fd;
    struct ifreq ifr;
    struct sockaddr_in *our_ip;

    memset(&ifr, 0, sizeof(struct ifreq));
    if((fd = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)) >= 0) {
        ifr.ifr_addr.sa_family = AF_INET;
        strcpy(ifr.ifr_name, interface);

        if (addr) {
            if (ioctl(fd, SIOCGIFADDR, &ifr) == 0) {
                our_ip = (struct sockaddr_in *) &ifr.ifr_addr;
                *addr = our_ip->sin_addr.s_addr;
                printf("%s (our ip) = %s/n", ifr.ifr_name, inet_ntoa(our_ip->sin_addr));
            } else {
                printf("SIOCGIFADDR failed, is the interface up and configured?: %s/n",
                        strerror(errno));
                return -1;
            }
        }

        if (ioctl(fd, SIOCGIFINDEX, &ifr) == 0) {
            printf("adapter index %d/n", ifr.ifr_ifindex);
            /*ָÕifindex »ñ÷*/
            *ifindex = ifr.ifr_ifindex;
        } else {
            printf("SIOCGIFINDEX failed!: %s/n", strerror(errno));
            return -1;
        }

        if (ioctl(fd, SIOCGIFHWADDR, &ifr) == 0) {
            memcpy(arp, ifr.ifr_hwaddr.sa_data, 6);
            printf("adapter hardware address %02x:%02x:%02x:%02x:%02x:%02x/n",
                arp[0], arp[1], arp[2], arp[3], arp[4], arp[5]);
        } else {
            printf("SIOCGIFHWADDR failed!: %s/n", strerror(errno));
            return -1;
        }
    }
    else {
        printf("socket failed!: %s/n", strerror(errno));
        return -1;
    }
    close(fd);
    return 0;
}

int check_ip(u_int32_t addr)
{
    struct in_addr temp;

    if (arpping(addr, server_config.server, server_config.arp, ETH_INTERFACE) == 0)
    {
        temp.s_addr = addr;
        printf("%s belongs to someone, reserving it for %ld seconds/n",
            inet_ntoa(temp), server_config.conflict_time);
        return 1;
    }
    else
        return 0;
}

int arpping(u_int32_t yiaddr, u_int32_t ip, unsigned char *mac, char *interface)
{
    int timeout = 2;
    int optval = 1;
    int s;                      /* socket */
    int rv = 1;                 /* return value */
    struct sockaddr addr;       /* for interface name */
    struct arpMsg arp;
    fd_set fdset;
    struct timeval tm;
    time_t prevTime;

    if((s = socket (PF_PACKET, SOCK_PACKET, htons(ETH_P_ARP))) == -1) {
        printf("Could not open raw socket/n");
        return -1;
    }

    if (setsockopt(s, SOL_SOCKET, SO_BROADCAST, &optval, sizeof(optval)) == -1) {
        printf("Could not setsocketopt on raw socket/n");
        close(s);
        return -1;
    }

    memset(&arp, 0, sizeof(arp));
    memcpy(arp.ethhdr.h_dest, MAC_BCAST_ADDR, 6);   /* MAC DA */
    memcpy(arp.ethhdr.h_source, mac, 6);        /* MAC SA */
    arp.ethhdr.h_proto = htons(ETH_P_ARP);      /* protocol type (Ethernet) */
    arp.htype = htons(ARPHRD_ETHER);        /* hardware type */
    arp.ptype = htons(ETH_P_IP);            /* protocol type (ARP message) */
    arp.hlen = 6;                   /* hardware address length */
    arp.plen = 4;                   /* protocol address length */
    arp.operation = htons(ARPOP_REQUEST);       /* ARP op code */
    *((u_int *) arp.sInaddr) = ip;          /* source IP address */
    memcpy(arp.sHaddr, mac, 6);         /* source hardware address */
    *((u_int *) arp.tInaddr) = yiaddr;      /* target IP address */

    memset(&addr, 0, sizeof(addr));
    strcpy(addr.sa_data, interface);
    if (sendto(s, &arp, sizeof(arp), 0, &addr, sizeof(addr)) < 0)
        rv = 0;

    tm.tv_usec = 0;
    time(&prevTime);
    while (timeout > 0) {
        FD_ZERO(&fdset);
        FD_SET(s, &fdset);
        tm.tv_sec = timeout;
        if (select(s + 1, &fdset, (fd_set *) NULL, (fd_set *) NULL, &tm) < 0) {
            printf("Error on ARPING request: %s/n", strerror(errno));
            if (errno != EINTR) rv = 0;
        } else if (FD_ISSET(s, &fdset)) {
            if (recv(s, &arp, sizeof(arp), 0) < 0 )
                rv = 0;
            if (arp.operation == htons(ARPOP_REPLY) &&
                bcmp(arp.tHaddr, mac, 6) == 0 &&
                *((u_int *) arp.sInaddr) == yiaddr) {
                printf("Valid arp reply receved for this address/n");
                rv = 0;
                break;
            }
        }
        timeout -= time(NULL) - prevTime;
        time(&prevTime);
    }
    close(s);
    return rv;
}

