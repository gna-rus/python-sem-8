import viev

# функция вывода всех контактов на экран
def get_data():
    with open("test.txt", "r", encoding="UTF-8" ) as file1:
        fl = file1.readlines()
        for i in fl:
            # выводим информацию на экран
            viev.print_result(i)

# функция добавления контакта в БД
# необходимо добавить стилизацию текста и вывод результата (успешно получилось добавить или нет)
def add_contact(contact, contact_num):
    with open("test.txt", "a", encoding="UTF-8" ) as file1:
        file1.write(f"{contact};{contact_num}" + "\n")

# функция поиска номера телефона по имени и фамилии
def find(surname):
    with open("test.txt", "r", encoding="UTF-8" ) as file1:
        fl = file1.readlines()
        for i in fl:
            res = i.split(";")
            if res[0] == surname:
                viev.print_result(res[1][:-1])


def add_number():
    pass

def del_contact():
    pass
