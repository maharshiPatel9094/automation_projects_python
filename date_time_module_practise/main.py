import datetime as dt

current_time = dt.datetime.now()
# print(current_time)
# 2024-11-01 11:48:01.318906

year = current_time.year
# if year == 2024:
#     print("hello")
# print(year)
# 2024

day_of_week = current_time.weekday()
print(day_of_week)