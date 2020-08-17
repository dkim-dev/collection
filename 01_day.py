#!/usr/bin/env python3

import sys
def usage():
    daynm = sys.argv[1]
    nmbr = int(sys.argv[2])
    num_of_arguments = len(sys.argv)
    if num_of_arguments != 3:
        print('Usage: ' + sys.argv[0] + ' day number (between 0 and 500) ex: ' + sys.argv[0] + ' Mon 100')
        exit()
    elif daynm not in weekDays:
        print('Usage: ' + sys.argv[0] + ' day number (between 0 and 500) ex: ' + sys.argv[0] + ' Mon 100')
        exit()
    elif not nmbr in range(0, 501):
        print('Usage: ' + sys.argv[0] + ' day number (between 0 and 500) ex: ' + sys.argv[0] + ' Mon 100')
        exit()

def input(day, num):
    if day == "Mon":
        dayofweek = 1
    elif day == "Tue":
        dayofweek = 2
    elif day == "Wed":
        dayofweek = 3
    elif day == "Thu":
        dayofweek = 4
    elif day == "Fri":
        dayofweek = 5
    elif day == "Sat":
        dayofweek = 6
    elif day == "Sun":
        dayofweek = 0
    day_sum=((int(dayofweek) + int(num))%7)
    return(weekDays[day_sum])

if __name__ == "__main__":
    weekDays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    usage()
    day = sys.argv[1]
    num = sys.argv[2]
    dayofweek = 0

    print(input(day, num))