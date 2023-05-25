import viev

# функция вывода всех контактов на экран
def get_data():
    with open("test.txt", "r", encoding="UTF-8" ) as file1:
        fl = file1.readlines()
        for i in fl:
            # выводим информацию на экран
            viev.print_result(i)

# добавляем контакт в БД
def add_contact(contact, contact_num):
    with open("test.txt", "a", encoding="UTF-8" ) as file1:
        file1.write(f"{contact};{contact_num}" + "\n")


def find():
    pass

def add_number():
    pass

def del_contact():
    pass
