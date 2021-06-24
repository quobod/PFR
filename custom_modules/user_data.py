import re
from custom_modules.input_validation import isString, isLetters
from custom_modules.utils import clear


def getUsername():
    pun = re.compile('^[a-zA-Z]+$')
    un = input('Create a username:\t')
    if pun.search(un.strip()):
        return un
    else:
        print('\tUsername: ' + un + ' must contain letters only ... try again\n')
        getUsername()


def getEmail():
    pem = re.compile(
        '^([a-zA-Z0-9]+)(\\.[a-zA-Z0-9]+)?@([a-zA-Z]+)\\.[a-zA-Z]{2,3}$')
    em = input('Enter email address:\t')
    if (pem.search(em.strip())):
        return em
    else:
        print('\tEmail: ' + em + ' is not valid ... Try again\n')
        getEmail()


def getPassword():
    p1 = input('Create a password:\t')
    p2 = input('\nConfirm password\t')

    if (p1.strip() != p2.strip()):
        print('\n\tPasswords don\'t match ... Try again\n')
        getPassword()
    elif (len(p1) < 6 or len(p2) < 6):
        print('\nPassword must be at least 6 characters ... Try again\n')
        getPassword()
    else:
        return p1.strip()


def getCredentials():
    return getUsername(), getEmail()


def start():
    username = ""
    email = ""
    exit = ""

    while (len(exit) == 0):
        clear()
        exit = input("\n\tType x, q or exit, quit to stop the program:")
        if (exit.strip() == "x" or exit.strip() == "exit" or exit.strip() == "q" or exit.strip() == "quit"):
            clear()
            break
        else:
            username, email = getCredentials()
            if (isLetters(username) and isString(email)):
                return {'name': username.strip(), 'email': email.strip()}
            else:
                start()
