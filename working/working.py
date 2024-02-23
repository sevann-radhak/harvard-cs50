import re
import sys


def main():
    hours = input("Hours: ")
    print(convert(hours))


def convert_time(time, period):
    if ':' in time:        
        hours, minutes = map(int, time.split(':'))
    else:
        hours, minutes = int(time), 0

    if period == 'AM' and hours == 12:
        hours = 0 
    if period == 'PM' and hours != 12:
        hours += 12

    return hours, minutes
    

def convert(s):
    if matches := re.search(r'^((?:1[0-2]|0?\d)(?::[0-5]\d)?)\s(AM|PM)\sto\s((?:1[0-2]|0?\d)(?::[0-5]\d)?)\s(AM|PM)$', s):
        start_time, start_period, end_time, end_period =  matches.group(1), matches.group(2), matches.group(3), matches.group(4)
        hours_start, minutes_start = convert_time(start_time, start_period)
        hours_end, minutes_end = convert_time(end_time, end_period)
                
        return (f'{hours_start:02d}:{minutes_start:02d} to {hours_end:02d}:{minutes_end:02d}')        
    raise ValueError
    

if __name__ == "__main__":
    main()