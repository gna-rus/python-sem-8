import viev
def add_contact(contact):
    res = 0

# функция вывода всех контактов на экран
def get_data():
    with open("test.txt", "r", encoding="UTF-8" ) as file1:
        fl = file1.readlines()
        for i in fl:
            # выводим информацию на экран
            viev.print_result(i)

def find():
    pass

def add_number():
    pass

def del_contact():
    pass
