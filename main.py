import secrets
import string

letters = string.ascii_letters
digits = string.digits
schars = string.punctuation
uppercases = string.ascii_uppercase 
alphabet = letters + digits

def generate_password(digit=False,uppercase=False,schar=True,length=12):
    length=int(length)
    digit_index=uppercase_index=schar_index= -1     #index variable
    password = ''


    while(digit_index == uppercase_index == schar_index):
        if(digit):
            digit_index=secrets.randbelow(length)
        if(uppercase):
            uppercase_index=secrets.randbelow(length)
        if(schar):
            schar_index=secrets.randbelow(length)
    
    for i in range(length):
        if(i==digit_index):
            password += ''.join(secrets.choice(digits))
        elif(i==uppercase_index):
            password += ''.join(secrets.choice(uppercases))
        elif(i==schar_index):
            password += ''.join(secrets.choice(schars))
        else:
            password += ''.join(secrets.choice(alphabet))

    return password

if(__name__=='__main__'):
    print(generate_password())