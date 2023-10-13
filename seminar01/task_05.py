number_cross_head = int(input("в какой вагон сел Вася, по порядку? "))
number_vagon = int(input("какой номер имеет вагон? "))

numering_vagons = int(input("нумерация с хвоста? введите 1"))

if numering_vagons == 1:
    print(number_cross_head + number_vagon - 1)
else:
    print("посчитать невозможно")