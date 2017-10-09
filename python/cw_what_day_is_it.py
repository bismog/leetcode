#!/usr/bin/env python

import datetime
import sys

def day(day_str):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    # year = int(str(day_str[:4]))
    # month = int(str(day_str[4:6]))
    # day = int(str(day_str[6:]))
    # print days[datetime.datetime(year, month, day).weekday()]
    return days[datetime.datetime.strptime(day_str, "%Y%m%d").weekday()]


def main():
    day_of_week = day(sys.argv[1])
    print day_of_week

if __name__ == "__main__":
    main()
