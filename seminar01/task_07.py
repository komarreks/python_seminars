# year = int(input("введите год "))
#
# yes = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
#
# if yes:
#     print("yes")
# else:
#     print("no")

import re

stroka = 'Пух'

listSlov = stroka.split()

# countA = len(listSlov[0].split("а|е|ё|и|о|у|э|ю|я"))
countA = len(re.split("а|е|ё|и|о|у|э|ю|я",listSlov[0]))

def isParaPam(listSlov, countA):
    paraPam = "Парам пам-пам"
    for i in listSlov:
        if len(re.split("а|е|ё|и|о|у|э|ю|я",i)) != countA:
            paraPam = "Пам парам"
            return paraPam
    return paraPam

if len(listSlov) == 1:
    print("Количество фраз должно быть больше одной!")
else:
    print(isParaPam(listSlov, countA))