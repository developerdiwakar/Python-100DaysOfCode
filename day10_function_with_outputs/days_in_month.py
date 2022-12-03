# Define the function is_leap year
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False
    
    return leap_year 

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    month_days_index = month - 1
    # If Leap year and February Month
    if is_leap(year) and month_days_index == 1:
        return month_days[month_days_index] + 1
    return month_days[month_days_index]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
