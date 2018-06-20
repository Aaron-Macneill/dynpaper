from timing import *

def get_index(args):

    dawn_time = args.dawn
    dusk_time = args.dusk
    current_time = time_string_to_float('{}:{}'.format(
        datetime.datetime.now().hour, datetime.datetime.now().second))
    day_duration = dusk_time-dawn_time
    night_duration = 24.0 - day_duration

    day_size = args.file_range[0]
    night_size = args.file_range[1]-day_size

    if dawn_time+day_duration >= current_time and current_time >= dawn_time:
        # It's day
        index = (current_time - dawn_time)/(day_duration/day_size)
    else:
        # It's night
        if current_time > dawn_time:
            index = day_size + (current_time-day_duration -
                                dawn_time)/(night_duration/night_size)
        else:
            index = day_size + (current_time + 24-dawn_time-day_duration) / \
                (night_duration/night_size)
    return int(index+1)
