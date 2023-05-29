def privet():
    print('Привет, ниже ты увидешь меню нашего справочника')

def menu():
    print('''Меню
1- показать контакты
2- добавить контакты
3- поиск номера телефона
4- изменить номер телефона
5- удалить контакт
6- выход''')

def print_result(str1):
    if str1 != None:
        print(str1)

def success_number():
    print('записано')

def success_del():
    print("пользователь удален")

def contacts(data):
    print(data)

def show_find(resalt):
    print(resalt)

def not_number():
    print("Error")

def error():
    print("Неизвестная ошибка!")



    