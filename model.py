import viev
import os


# функция вывода всех контактов на экран
def get_data():
    with open("test.txt", "r", encoding="UTF-8") as file1:
        fl = file1.readlines()
        for i in fl:
            # выводим информацию на экран
            viev.print_result(i)


# функция добавления контакта в БД
# необходимо добавить стилизацию текста и вывод результата (успешно получилось добавить или нет)
def add_contact(contact):
    with open('file.text', 'a', encoding='utf-8') as file:
        file.write(contact)
        file.write('/n')


# функция поиска номера телефона по имени и фамилии
def find(surname):
    with open('file.text', 'r', encoding='utf-8') as file:
        ds = file.read().split('/n')
        exp = []
        for line in ds:
            a = line.split(';')
            if a[0] == surname:
                exp.append(a[1])
    return exp


# Функция изменения номера телефона пользователя
def add_number(surname1, number):
    with open("test.txt", "r", encoding="UTF-8") as file1:
        fl = file1.readlines()
        with open("test1.txt", "a", encoding="UTF-8") as file2:
            for i in fl:
                if i.split(";")[0] == surname1:
                    file2.write(f"{surname1};{number}\n")
                else:
                    file2.write(i)
    open("test.txt", "w").close()
    with open("test.txt", "r+", encoding="UTF-8") as file1, open("test1.txt", "r", encoding="UTF-8") as file2:
        fl = file2.readlines()
        file1.truncate()
        for i in fl:
            file1.writelines(i)
    open("test1.txt", "w").close()

    return True


def del_contact():
    pass
