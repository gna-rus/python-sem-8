def add_contact(contact):
    with open('file.text','a',encoding='utf-8') as file:
        file.write(contact)
        file.write('/n')
                 
def get_data():
    file = open ('file.text','r', encoding = 'utf-8')
    data = file.read().split('/n')[:-1]
    file.close()
    return(data)
def find(surname):
     with open('file.text','r',encoding='utf-8') as file:
         ds = file.read().split('/n')[:-1] 
         exp = []         
         for line in ds:
             a = line.split(';')
             if a[0] == surname:
                 exp.append(a[1])
     return exp
def add_number(surname1,number):
    with open('file.text','r',encoding='utf-8') as file:
         ds = file.read().split('/n')[:-1]
         x = 0
         for line in ds:
             a = line.split(';')
             if a[0] == surname1:
                ds[x] = surname1 +';'+ number 
             x = x +1 
    with open('file.text','w',encoding='utf-8') as file:
        for value in ds:
            file.write(value)
            file.write('/n') 
def del_contact(surname2):
    with open('file.text','r',encoding='utf-8') as file:
         ds = file.read().split('/n')[:-1]
         x = 0
         for line in ds:
             a = line.split(';')
             if a[0] == surname2:
                ds.remove(ds[x]) 
             x = x +1 
    with open('file.text','w',encoding='utf-8') as file:
        for value in ds:
            file.write(value)
            file.write('/n')
                                                        
          
          
                                
         
                            