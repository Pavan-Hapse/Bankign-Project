'''
@Group Members Name@

1. Prajakta Dilip Chavhan
--------------------------------------
2. Pushpak Jitendra Jadhav
------------------------------------
3. Pavan Anil Hapse
-----------X--X---X-----------------------------------------------------------
'''


import re
print(".....welcome in bank system.....")
amt=int(input("enter amount is:"))
def menu():
    print("1.create an account")
    print("2.Credit Money")
    print("3.Debit Money")
    print("4.check balance")
    print("5.Exist")

menu()   
c = int(input("Enter your choice...."))

if c == 1:
    n = (input("Enter your name:"))
    mail = input("Enter your mail:")
    x = True
    while x:
        if len(mail) == 50:
            break
        elif not re.search('[a-z]', mail):
            print('password must containt a letter from [a-z]')
            break
        elif not re.search('[0-9]', mail):
            print('password must containt a figure from [0-9]')
            break

        elif not re.search('[@]', mail):
            print('password must containt a special char from [@]')
            break
        elif not re.search('[gmail]', mail):
            print('mail must containt a special char from [gmail.com]')
            break

        elif not re.search("\s", mail):
            break
        else:
            #print("valid mail", mail)
            x = False
            break
    if x:
        print('invalid mail')
        

    mo = input("Enter Mobile No:")
    x = True
    while x:
        if len(mo) == 10:
            break
        elif not re.search('[0-9]', mo):
            print('Number must containt a number from [0-9]')
        elif not re.search("\s", mo):
            break
        else:
            print("valid Number", mo)
            x = False
            break
    if x:
        print('invalid number')

    pas = input("Enter password:")
    x = True
    while x:
        if (len(pas) < 4) or len(pas) > 15:
            break
        elif not re.search('[a-z]', pas):
            print('password must containt a letter from [a-z]')
            break
        elif not re.search('[0-9]', pas):
            print('password must containt a figure from [0-9]')
            break
        elif not re.search('[A-Z]', pas):
            print('password must containt a letter from [A-Z]')
            break
        elif not re.search('[$@#]', pas):
            print('password must containt a special char from [$#@]')
            break
        elif not re.search("\s", pas):
            break
        else:
            #print("valid password is", pas)
            x = False
            break
    if x:
        print('invalid password')
    print("Your account created successfully..")


if c == 2:

    n = (input("Name of account Holder:"))
    mail = input(" Enter your mail:")
    x = True
    while x:
        if len(mail) == 50:
            break
        elif not re.search('[a-z]', mail):
            print('mail must containt a letter from [a-z]')
            break
        elif not re.search('[0-9]', mail):
            print('mailmust containt a figure from [0-9]')
            break

        elif not re.search('[@]', mail):
            print('mail must containt a special char from [@]')
            break
        elif not re.search('[gmail]', mail):
            print('mail must containt a special char from [gmail.com]')
            break

        elif not re.search("\s", mail):
            break
        else:
            #print("valid mail", mail)
            x = False
            break
    if x:
        print('invalid mail')

    pas = input("password:")
    x = True
    while x:
        if (len(pas) < 4) or len(pas) > 15:
            break
        elif not re.search('[a-z]', pas):
            print('password must containt a letter from [a-z]')
            break
        elif not re.search('[0-9]', pas):
            print('password must containt a figure from [0-9]')
            break
        elif not re.search('[A-Z]', pas):
            print('password must containt a letter from [A-Z]')
            break
        elif not re.search('[$@#]', pas):
            print('password must containt a special char from [$#@]')
            break
        elif not re.search("\s", pas):
            break
        else:
            #print("valid password is", pas)
            x = False
            break
    if x:
        print("invalid")
    mo = input("Enter Mobile No")
    x = True
    while x:
        if len(mo) == 10:
            break
        elif not re.search('[0-9]', mo):
            print('Number must containt a number from [0-9]')
        elif not re.search("\s", mo):
            break
        else:
            #print("valid Number", mo)
            x = False
            break
    if x:
        print('invalid number')

    d = int(input("Enter the Credit Amount"))
    if amt > d:
       amt=amt+d
       print("Your amount is",amt)
       
    print("amount is credited sucessfully...")



if c == 3:


    n = (input("Name of account Holder:"))
    mail = input("Enter mail")
    x = True
    while x:
        if len(mail) == 50:
            break
        elif not re.search('[a-z]', mail):
            print('mail must containt a letter from [a-z]')
            break
        elif not re.search('[0-9]', mail):
            print('mail must containt a figure from [0-9]')
            break

        elif not re.search('[@]', mail):
            print('mail must containt a special char from [@]')
            break
        elif not re.search('[gmail]', mail):
            print('mail must containt a special char from [gmail.com]')
            break

        elif not re.search("\s", mail):
            break
        else:
            print("valid mail", mail)
            x = False
            break
    if x:
        print('invalid mail')


   
    mo = input("Enter Mobile No")
    x = True
    while x:
        if len(mo) == 10:
            break
        elif not re.search('[0-9]', mo):
            print('Number must containt a number from [0-9]')
        elif not re.search("\s", mo):
            break
        else:
            #print("valid Number", mo)
            x = False
            break
    if x:
        print('invalid number')


    d = int(input("Enter the Debit Amount"))
    if amt > d:
       amt=amt-d
       print("remaining amount is",amt)
       print("sucessfully debited", d)


if c==4:
    print("Your Balance is", amt)

if c==5:
    print("Exit")
