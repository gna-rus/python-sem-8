import viev, model
def start():
    viev.privet() # Приветствие
    while True:
        viev.menu()
        point = input('Введите команду из меню: ')
        # 1 - показать контакты
        if point == '1':
            model.get_data()
            input() # ждем ввода чего либо для комфортного отображения информации

        # 2 - добавить контакты
        elif point == '2':
            contact = input('Введите имя и фамилию нового котакта: ')
            contact_num = input('Введите номер телефона контакта: ')
            res = model.add_contact(contact, contact_num)
            if res:
                viev.success(res)
            else:
                viev.not_success(res)

        # 3 - поиск номера телефона
        elif point == '3':
            surname = input('Введите фамилию для поиска номера: ')
            resalt = model.find(surname)
            # viev.show_find(resalt)
            input() # ожидание

        # 4 - изменить номер телефона
        elif point == '4':
            surname1 = input('Введите фамилию для изменения номера:')
            number = input('Введите новый номер')
            res1 = model.add_number(surname1,number) 
            if res1:
                viev.success_number(res1) 
            else:
                viev.not_number(res1)
        # 5 - удалить контакт
        elif point == '5':
            surname2 = input('Введите фамилию для удаления контакта:')
            res2 = model.del_contact(surname2) 
            if res2:
                viev.success_del(res2) 
            else:
                viev.not_del(res2)
        # 6 - выход
        elif point == '6':
            break
        else:
            viev.error() 
                                                
    