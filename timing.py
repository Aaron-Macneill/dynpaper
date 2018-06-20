# functions dealing with dates and time


import datetime

def time_string_to_float(time):
    if ':' not in time:
        return 'Should be in form HH:mm.'
    time = time.split(':')
    if len(time) != 2:
        return 'Should be in this form: HH:mm.'

    try:

        hours = int(time[0])
    except:
        return 'Hours should be an int.'

    if not (0 <= hours <= 23):
        return 'Hours should be in range [0,23].'

    try:
        minutes = int(time[1])
    except:
        return 'Minutes should be an int.'

    if not (0 <= minutes < 60):
        return 'Minutes should be in range [0,23].'

    return hours+minutes/60.0
