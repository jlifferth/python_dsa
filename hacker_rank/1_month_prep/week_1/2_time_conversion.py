

def time_conversion(s):
    time = s.split(':')
    if 'AM' in s:
        if time[0] == '12':
            hour = '00'
        else:
            hour = time[0]
        time_out = hour + ':' + time[1] + ':' + time[2][:-2]
    elif 'PM' in s:
        if time[0] == '12':
            hour = '12'
        else:
            hour = int(time[0]) + 12
        time_out = str(hour) + ':' + time[1] + ':' + time[2][:-2]
    else:
        time_out = "Error"

    return time_out


time0 = '12:01:00PM'
time1 = '12:01:00AM'
time3 = '07:05:45PM'

print(time_conversion(time3))
