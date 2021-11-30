def calculate_bmi(height, weight):
    return weight/(height ** 2) * 10000

def calculate_calories(cal_data):
    cal = [x.calorie for x in cal_data]
    return sum(cal)

from datetime import datetime
def calculate_sleeping_time(sleep_time, wakeup_time):
    sleep_time = list(map(int, sleep_time.split(":")))
    wakeup_time = list((map(int, wakeup_time.split(":"))))
    mins = wakeup_time[1] - sleep_time[1]
    if mins < 0:
        mins += 60
        wakeup_time[0] -= 1
    hrs = wakeup_time[0] - sleep_time[0]
    if hrs < 0:
        hrs += 24
    return {
        'hrs' : hrs,
        'mins' : mins,
        'total' : hrs*60+mins
    }

