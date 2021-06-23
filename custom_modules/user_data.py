from custom_modules.input_validation import isString, isLetters
from custom_modules.utils import clear


def getUsername():
    un = input('Create a username:\t')
    return un


def getEmail():
    em = input('Enter email address:\n')
    return em


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
            print(username + ' ' + email)
            if (isLetters(username.strip()) and isString(email.strip())):
                return {'name': username.strip(), 'email': email.strip()}
            else:
                start()
