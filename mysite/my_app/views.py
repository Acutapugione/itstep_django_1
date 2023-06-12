from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {"data": "Вітаю!"}
    return render(request, "index.html", context)


def curr_date_time(request):
    context = {"data": datetime.now().strftime("%d.%M.%Y : %H.%m.%S")}
    return render(request, "index.html", context)

def get_multiplication_table(n):
    table = {}
    for i in range(1, n+1):
        row = {}
        for j in range(1, n+1):
            row[j] = i*j
        table[i] = row
    return table

def multiplication_table(request):
    context = {
        "data": get_multiplication_table(10),
    }
    #
    return render(request, "multiplication_table.html", context)

def get_programmers_day():
    year = datetime.now().year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        day = datetime(year, 9, 12)  # Leap year
    else:
        day = datetime(year, 9, 13)  # Non-leap year
    return day

def programmers_day(request):
    context = {"data": get_programmers_day()}
    return render(request, "index.html", context=context)
