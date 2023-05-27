def add_contact(contact):
    with open('file.text','a',encoding='utf-8') as file:
        file.write(contact)
        file.write('/n')
                 
def get_data():
    file = open ('file.text','r', encoding = 'utf-8')
    data = file.read().split('/n')
    file.close()
    return(data)
def find(surname):
     with open('file.text','r',encoding='utf-8') as file:
         ds = file.read().split('/n') 
         exp = []         
         for line in ds:
             a = line.split(';')
             if a[0] == surname:
                 exp.append(a[1])
     return exp
                      
         
                            