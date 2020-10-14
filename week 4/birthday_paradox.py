import random
month = random.randint(1,12)
year = random.randint(1993,2020)
print(year)
print(month)


if (month % 2 == 0):
    if (month == 2):
        if (year % 4 ==0  and year % 100 != 0 or year % 400 == 0):
            print("29 days")
        else:
            print("28 days")
    else:
        print("30 days")
else:
    print("31 days")