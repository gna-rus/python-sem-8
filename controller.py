import viev, model
def start():
    viev.privet() # Приветствие
    while True:
        viev.menu()
        point = input('введите команду из меню:')
        # 1 - показать контакты
        if point == '1':
            data = model.get_data()
            viev.contacts(data)
        # 2 - добавить контакты
        elif point == '2':
            contact = input('введите контакт в формате фамилия имя;телефон')
            res = model.add_contact(contact)
            if res:
                viev.success(res)
            else:
                viev.not_success(res)
        # 3 - поиск номера телефона
        elif point == '3':
            surname = input('введите фамилию для поиска номера:')
            resalt = model.find(surname)
            viev.show_find(resalt)
        # 4 - изменить номер телефона
        elif point == '4':
            surname1 = input('введите фамилию для изменения номера:')
            number = input('введите новый номер')
            res1 = model.add_number(surname1,number) 
            if res1:
                viev.success_number(res1) 
            else:
                viev.not_number(res1)
        # 5 - удалить контакт
        elif point == '5':
            surname2 = input('введите фамилию для удаления контакта:')
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
                                                
    