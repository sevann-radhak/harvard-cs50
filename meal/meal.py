def main():
    time_string = input('What time is it: ')
    breackfast_time = (7.00, 8.00)
    lunch_time = (12.00, 13.00)
    dinner_time = (18.00, 19.00)
    
    value = convert(time_string)
    
    if breackfast_time[0] <= value <= breackfast_time[1]:
        print("breakfast time")
    elif lunch_time[0] <= value <= lunch_time[1]:
        print("lunch time")
    elif dinner_time[0] <= value <= dinner_time[1]:
        print("dinner time")
    

def convert(time_string):      
    hours, minutes = map(int, time_string.split(':'))
    return round((hours + minutes / 60.0), 2)


if __name__ == '__main__':
    main()