from custom_modules.input_validation import isString, isLetters
from custom_modules.utils import clear


def getUsername():
    un = input('Create a username:\t')
    return un


def getEmail():
    em = input('Enter email address:\t')
    return em


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
            if (isLetters(username.strip()) and isString(email.strip())):
                return {'name': username.strip(), 'email': email.strip()}
            else:
                start()
