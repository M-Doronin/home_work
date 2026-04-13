#task_1
def find_max(a, b):
    if a > b:
        print(a)
    else:
        print(b)

find_max(10, 20)


#task_2
def check_difference(a, b):
    if abs(a - b) == 135:
        print("yes")
    else:
        print("No")

check_difference(200, 65)


#task_3
def get_season(month):
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    else:  # 9, 10, 11
        print("осень")

get_season(1)


#task_4
def check_numbers(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")

check_numbers(15, 20, 25)


#task_5
def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    print(count)

count_positive([1, -2, 3, -4, 5])


#task_6
def count_days(years, months):
    total_days = years * 12 * 29 + months * 29
    print(total_days)

count_days(1, 0)
