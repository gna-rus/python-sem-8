import viev


# функция вывода всех контактов на экран
def get_data():
    try:
        with open("test.txt", "r", encoding="UTF-8") as file1:
            fl = file1.readlines()
            for i in fl:
                # выводим информацию на экран
                viev.print_result(i)
    except FileNotFoundError:
        # оповещение что файла нет и создание необходимого пустого файла
        print("Файл отсутствует!")
        open("test.txt", "w").close()


# функция добавления контакта в БД
# необходимо добавить стилизацию текста и вывод результата (успешно получилось добавить или нет)
def add_contact(contact):
    with open('test.txt', 'a', encoding='utf-8') as file:
        file.writelines(contact)
        file.write("\n")


# функция поиска номера телефона по имени и фамилии
def find(surname):
    with open('test.txt', 'r', encoding='utf-8') as file:
        ds = file.readlines()
        for line in ds:
            a = line.split(';')
            if a[0] == surname:
                return a[1]


# Функция изменения номера телефона пользователя
def add_number(surname1, number):
    try:
        with open("test.txt", "r", encoding="UTF-8") as file1:
            fl = file1.readlines()
            with open("test1.txt", "a", encoding="UTF-8") as file2:
                for i in fl:
                    if i.split(";")[0] == surname1:
                        file2.writelines(f"{surname1};{number}")  # загружает в файл строку с изменнным номером телефона
                    else:
                        file2.write(i)  # загружает всю строку без изменений
        open("test.txt", "w").close()  # очищаем старый файл полностью
        # далее алгорит перезаливки данных из нового в старый файл
        with open("test.txt", "r+", encoding="UTF-8") as file1, open("test1.txt", "r", encoding="UTF-8") as file2:
            fl = file2.readlines()
            for i in fl:
                file1.writelines(i)  # заполняю старый файл новыми данными
        open("test1.txt", "w").close()  # очищаем новый файл полностью (может стоит прописать алгоритм уделания файла)
        return True
    except:
        return False


# Функция удаления пользователя по имени
def del_contact(surname1):
    try:
        with open("test.txt", "r", encoding="UTF-8") as file1:
            fl = file1.readlines()
            with open("test1.txt", "a", encoding="UTF-8") as file2:
                for i in fl:
                    if i.split(";")[0] == surname1:
                        continue
                    else:
                        file2.write(i)  # загружает всю строку без изменений
        open("test.txt", "w").close()  # очищаем старый файл полностью
        # далее алгорит перезаливки данных из нового в старый файл
        with open("test.txt", "r+", encoding="UTF-8") as file1, open("test1.txt", "r", encoding="UTF-8") as file2:
            fl = file2.readlines()
            for i in fl:
                file1.writelines(i)  # заполняю старый файл новыми данными
        open("test1.txt", "w").close()  # очищаем новый файл полностью (может стоит прописать алгоритм уделания файла)
        return True
    except:
        return False
