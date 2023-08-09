import secrets
import string

letters = string.ascii_lowercase
digits = string.digits
schars = string.punctuation
uppercases = string.ascii_uppercase 

def generate_password(digit=True,uppercase=True,schar=True,length=12):
    generation_pool = letters
    length=int(length)
    password = ''

    if digit:
        generation_pool=generation_pool+digits
    if uppercase:
        generation_pool=generation_pool+uppercases
    if schar:
        generation_pool=generation_pool+schars
    
    for i in range(length):
        password += ''.join(secrets.choice(generation_pool))

    return password

if(__name__=='__main__'):
    print(generate_password())