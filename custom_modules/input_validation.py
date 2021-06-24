import re

pLetters = "^[a-zA-Z]+$"
pNumbers = "^[0-9]+$"


def isString(arg):
    return (type(arg) == str and len(arg) > 0)


def isLetters(arg):
    return (type(arg) == str and len(arg) > 0 and re.search(pLetters, arg))


def isNumbers(arg):
    return ((type(arg) == int or type(arg) == float) and re.search(pNumbers, arg))


def isEmail(arg):
    re.compile(
        '^([a-zA-Z0-9]+)(\\.[a-zA-Z0-9]+)?@([a-zA-Z]+)\\.[a-zA-Z]{2,3}$')
    return re.search(arg)
