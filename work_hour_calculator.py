from datetime import timedelta
from greetings import *
# Calculates net pay (float) based on given time data by user
# return: pounds_after_tax
def calc_net_pay() -> float:
    """
    Calculates net pay based on given time data by user
    :return: pounds_after_tax
    """
    # Greet and introduce (https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/)
    print(welcome[1] + welcome[2])
    # Get data from the user (START / FINISH TIMES + BREAK duration)
    user_start_time: str = input("START Time? (example 0400): ")

    if len(user_start_time) == 1:
        user_start_time = '0' + user_start_time + '00'
    elif len(user_start_time) == 3:
        user_start_time = '0' + user_start_time

    user_finish_time = input("FINISH Time? (example 1515): ")

    if len(user_finish_time) == 2:
        user_finish_time = user_finish_time + '00'
    elif len(user_finish_time) == 3:
        user_finish_time = '0' + user_finish_time

    start_hour_by_user = int(user_start_time[0] + user_start_time[1])
    start_minute_by_user = int(user_start_time[2] + user_start_time[3])
    finish_hour_by_user = int(user_finish_time[0] + user_finish_time[1])
    finish_minute_by_user = int(user_finish_time[2] + user_finish_time[3])
    breaks = ['00', '15', '30', '45']
    correct_break_entered = False
    while not correct_break_entered:
        break_minutes_by_user = (input('Break MINUTES? (00, 15, 30, 45) '))
        # Make sure input is only numbers
        if break_minutes_by_user in breaks:
              print(f'You had {break_minutes_by_user} minutes break')
              if break_minutes_by_user == '00':
                  print('Please make sure you had no break today')
              break_minutes_by_user = int(break_minutes_by_user)
              correct_break_entered = True
        else:
            print(f'You entered: {break_minutes_by_user}\nPlease enter 00, 15, 30, 45')
    
    # Pay rates
    available_pay_rates = (12.3, 13.8,)
    
    # Deductin 
    deduction_percentage = 24

    start_hour_delta = timedelta(hours=start_hour_by_user, minutes=start_minute_by_user)
    finish_hour_delta = timedelta(hours=finish_hour_by_user, minutes=finish_minute_by_user)
    break_duration = timedelta(hours=0, minutes=break_minutes_by_user)

    # Calculate total worked hours
    total_worked_hours = finish_hour_delta - start_hour_delta

    # Calculate paid hours
    paid_hours = total_worked_hours - break_duration
    to_display_paid_hours = str(paid_hours)

    # Ask for pay rate
    ask_for_rate = input('Did you drive class 1 today? (y/n): ')
    ask_for_rate = ask_for_rate[0].lower()
    if ask_for_rate == 'y':
        rate_for_the_day = available_pay_rates[1]  # Float
        # print('class 1 rate')
    else:
        rate_for_the_day = available_pay_rates[0]  # Float
        
    # Hours
    paid_hours_string = str(paid_hours)
    paid_hours_integer = int(paid_hours_string[:2])
    whole_hours = paid_hours_integer

    # Minutes contribute to hours
    paid_minutes_integer = int(paid_hours_string[3:5])
    if paid_minutes_integer == 15:
        minutes_to_hours = 0.25
    elif paid_minutes_integer == 30:
        minutes_to_hours = 0.5
    elif paid_minutes_integer == 45:
        minutes_to_hours = 0.75
    else:
        minutes_to_hours = 0

    float_timedata_to_pay_calculation = whole_hours + minutes_to_hours  # Float number
    pounds_before_tax = float_timedata_to_pay_calculation * rate_for_the_day

    # Make it two decimal points long
    pounds_before_tax = round(pounds_before_tax, 2)

    pounds_after_tax = pounds_before_tax - (pounds_before_tax / 100 * deduction_percentage)
    pounds_after_tax = round(pounds_after_tax, 2)
    print(f'\nBased on your inputs, here are your results:\nPaid hours: {to_display_paid_hours[:5]}')
    print(f'Earnings before tax: £{pounds_before_tax}\nNet Earnings today: £{pounds_after_tax}')
    return pounds_after_tax
calc_net_pay()
