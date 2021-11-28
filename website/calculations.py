def calculate_bmi(height, weight):
    return weight/(height ** 2) * 10000

def calculate_calories(cal_data):
    cal = [x.calorie for x in cal_data]
    return sum(cal)