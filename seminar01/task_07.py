year = int(input("введите год "))

yes = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if yes:
    print("yes")
else:
    print("no")
