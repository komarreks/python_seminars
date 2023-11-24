from typing import NoReturn

def show_commands():
    print("add - добавить контакт")
    print("show - показать все контакты")
    print("rem - Изменить контакт")
    print("copy 'номер строки контакта' 'имя файла без расширения' - копирование контакта в указанный файл")
    print("exit - закрыть программу")
    print("del - удалить контакт, будет выведен список для выбора")

def show_all(fileName, returnData = False):
    data = file_as_list(fileName)
    print("Список контактов")
    print_list(data)
    if returnData:
        return data

def add_new(fileName) -> NoReturn:
    lastName = input("Введите фамилию: ")
    firstName = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите телефон: ")

    with open(fileName, "a", encoding="utf-8") as file:
        file.write(f"{lastName} {firstName} {patronymic} - {phone}\n")

def file_as_list(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        data = file.readlines()
    return data

def list_in_file(list, file):
    with open(file, "w+", encoding="utf-8") as f:
        for d in list:
            f.write(f"{d}")

def delete_from_list(fileName):
    data = show_all(fileName, True)
    index = input("укажите номер записи или 0 если передумали: ")
    index = int(index) - 1

    if index>-1:
        del_contact = data.pop(index)
        list_in_file(data, fileName)
        print(f"{del_contact} удален")
    else:print("удаление отменено")

def remake(fileName):
    data = show_all(fileName, True)
    index = int(input("Укажите номер контакта для редактирования: ")) - 1

    if index>-1:
        listContact = data[index].split(" - ")
        contactData = listContact[0].split()

        print("Укажите данные для изменения, если менять не нужно - оставьте пустым")
        newLastName = input("Фамилия: ")
        newName = input("Имя: ")
        newPatronymic = input("Отчество: ")
        newPhone = input("Телефон: ")

        if newLastName != "":
            contactData[0] = newLastName
        if newName != "":
            contactData[1] = newName
        if newPatronymic != "":
            contactData[2] = newPatronymic
        if newPhone != "":
            listContact[1] = newPhone

        data[index] = f"{contactData[0]} {contactData[1]} {contactData[2]} - {listContact[1]}"

        list_in_file(data, fileName)

        print("Контакт изменен")

def find(fileName):
    data = file_as_list(fileName)
    findFlag = True
    while findFlag:
        findSubString = input("Введите значение для поиска или '-' для завершения: ")
        if findSubString != "-":
            data = list(filter(lambda x:findSubString in x,data))
            print("Найденные контакты: ")
            print_list(data)
        else:findFlag=False

def print_list(list):
    for item in list:
        print(f"{list.index(item)+1}. {item}")

def copy_item(item, newfileName, oldFileName):
    data = file_as_list(oldFileName)
    target = data[item-1]
    with open(newfileName+".txt","a",encoding="utf-8") as f:
        f.write(f"{target}\n")
    print(f"контакт {target} записан в файл {newfileName}")

def main():
    fileName = "phonebook.txt"
    print("=============================")
    print("====ТЕЛЕФОННЫЙ СПРАВОЧНИК====")
    print("? - Показать команды")
    while True:
        answer = input("Введите операцию или ? для справки: ").strip()

        if answer == "show":
            show_all(fileName)
        elif answer == "add":
            add_new(fileName)
        elif answer == "find":
            find(fileName)
        elif answer == "rem":
            remake(fileName)
        elif answer == "del":
            delete_from_list(fileName)
        elif "copy" in answer:
            commandParameters = answer.split()
            copy_item(int(commandParameters[1]),commandParameters[2], fileName)
        elif answer == "?":
            show_commands()
        elif answer == "exit":
            break


if __name__ == "__main__":
    main()
