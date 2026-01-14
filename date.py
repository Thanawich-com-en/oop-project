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

def is_valid_date(day, month, year):

    if month < 1 or month > 12:
        return False
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        days_in_month[1] = 29

    return 1 <= day <= days_in_month[month - 1]

def day_in_year(year):
    
    if is_leap(year):
        return 366 
    else: 
        return 365
    
def date_to_days(day, month, year):
    total_days = 0
    
    for y in range(1, year):
        total_days += day_in_year(y)
        
    total_days += day_of_year(day, month, year)
    return total_days
    
def date_diff(date1, date2):
    d1, m1, y1 = map(int, date1.strip().split("-"))
    d2, m2, y2 = map(int, date2.strip().split("-"))
    if not is_valid_date(d1, m1, y1) or not is_valid_date(d2, m2, y2):
        return "Invalid"
    days1 = date_to_days(d1, m1, y1)
    days2 = date_to_days(d2, m2, y2)
    return days2 - days1 + 1

print(day_of_year(29, 2, 2024))
