def is_leap(year):
    if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def day_of_year(day, month, year):
    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        day_in_month[1] = 29

    day_of_year = sum(day_in_month[:month - 1] + day)
    return day_of_year

print(day_of_year(29, 2, 2024))
