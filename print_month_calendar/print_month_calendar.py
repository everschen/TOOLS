#!/usr/bin/env python

import calendar
import datetime
import sys

split = " "
split = "\t"


if split == "\t":
    tri_split = "\t"
else:
    tri_split = split*3

def print_month_calendar(year, month):
    # 输出月历表头
    print(calendar.month_name[month] + split + str(year))
    print("Mo" + split + "Tu" + split + "We" + split + "Th" + split + "Fr" + split + "Sa" + split + "Su")

    # 获取该月第一天是星期几，以及该月的天数
    first_weekday, month_days = calendar.monthrange(year, month)

    # 初始化当前日期
    current_day = 1
    first_week = True

    # 输出每一行日期
    while current_day <= month_days:
        row = ""
        for weekday in range(7):
            #print(first_weekday, weekday)
            if current_day > month_days:
                # 如果当前日期已经超过了该月的天数，输出空格
                row += tri_split
            elif weekday < first_weekday and first_week:
                # 如果当前日期还未到该月的第一天，输出空格
                row += tri_split
            else:
                # 输出日期，并在数字不足两位时补充空格
                row += str(current_day).rjust(2) + split
                current_day += 1
        print(row)
        first_week = False



arg_num = len(sys.argv)

now = datetime.datetime.now()
current_year = now.year
current_month = now.month

if arg_num == 3:
    current_year = int(sys.argv[1])
    current_month = int(sys.argv[2])

elif arg_num == 2:
    current_year = int(sys.argv[1])


print_month_calendar(current_year, current_month)
