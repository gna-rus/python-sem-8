import viev, model
def start():
    viev.privet()
    while True:
        viev.menu()
        point = input('введите команду из меню:')
        if point == '1':
            data = model.get_data()
            viev.contacts(data)
        elif point == '2':
            contact = input('введите контакт в формате фамилия имя;телефон')
            res = model.add_contact(contact)
            viev.success(res)          
        elif point == '3':
            surname = input('введите фамилию имя для поиска номера:')
            resalt = model.find(surname)
            viev.show_find(resalt)
        elif point == '4':
            surname1 = input('введите фамилию имя для изменения номера:')
            number = input('введите новый номер')
            res1 = model.add_number(surname1,number) 
            viev.success_number(res1)
             
            
        elif point == '5':
            surname2 = input('введите фамилию имя для удаления контакта:')
            res2 = model.del_contact(surname2) 
            viev.success_del(res2) 
            
        elif point == '6':
            break
        else:
            viev.error() 
                                                
    