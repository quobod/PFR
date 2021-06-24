#! /usr/bin/env python3
from custom_modules.log import log
from custom_modules.user_data import start, getPassword
from custom_modules.utils import clear
from custom_modules.hasher import hash_password
from custom_modules.input_validation import isString
from custom_modules.jwt import generate_token, get_info, get_meta, refresh_token, verify_token


def init():
    user = start()
    if (type(user) == dict):
        clear()
        token = generate_token(user)
        verified = verify_token(token)
        info = get_info(token)
        meta = get_meta(token)
        token = refresh_token(token)

        log('\n\n\tHi ' + user['name'] +
            '. Now you have to create a password\n')
        password = getPassword()
        hashed = hash_password(password)

        if (isString(password)):
            print('\tOriginal Password: ' + password)
            print('\tHashed Password: ' + str(hashed))
            print('\n\n')

    else:
        log('\n\tDone\n')


init()
