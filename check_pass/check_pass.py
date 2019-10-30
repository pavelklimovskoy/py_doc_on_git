mail="blablabla@mail.ru"
#password=input("enter your password ")

def check_password(password):
    if len(password)<6 :
        return 0
    else:
        return 1

def check_mail(mail):
    for i in mail:
        if i=="@":
            return 1
        else:
            return 0

if check_mail(mail):
    print("ok")
    
