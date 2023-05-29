def print_red_colour(text):
    print("\033[31m{}".format(text))


def print_green_colour(text):
    print("\033[32m{}".format(text))


def print_black_colour(text):
    print("\033[30m{}".format(text))


def privet():
    print("Привет, ниже ты увидишь меню нашего справочника")


def menu():
    print_black_colour("Меню: \n"
                       "1 - Показать контакты\n"
                       "2 - Добавить контакты\n"
                       "3 - Поиск номера телефона\n"
                       "4 - Изменить номер телефона\n"
                       "5 - Удалить контакт\n"
                       "6 - Выход")


def contacts(data):  # 1 пункт. Демонстрация контактов.
    print_red_colour(data)


def success(res):  # 2 пункт. Добавление контакта.
    print_green_colour('Записано')


def show_find(resalt):  # 3 пункт. Поиск номера телефона.
    print_green_colour("Результаты поиска: ")
    print_red_colour(resalt)


def success_number(res1):  # 4 пункт.Изменение номера телефона.
    print_green_colour('Записано')


def not_number(res1):  # 4 пункт. Изменение номера телефона.
    print_red_colour("Error")


def success_del(res2):  # 5 пункт. Удаление контакта.
    print_green_colour("Пользователь удален успешно")


def not_del(res2):
    print_red_colour("Не удалось удалить пользователя")  # 5 пункт. Удаление контакта.


def error():
    print_red_colour("Неизвестная ошибка")