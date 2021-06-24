#! /usr/bin/env python3
from custom_modules.log import log
from custom_modules.user_data import start, getPassword
from custom_modules.utils import clear
from custom_modules.hasher import hash_password, check_password
from custom_modules.input_validation import isString
from custom_modules.jwt import generate_token, get_info, get_meta, refresh_token, verify_token


def init():
    user = start()
    if (type(user) == dict):
        clear()

        log('\n\n\tHi ' + user['username'].capitalize() +
            '. Now you have to create a password\n')
        password = getPassword()
        hashed = hash_password(password)

        if (isString(password)):
            user.update({'password': str(hashed)})
            token = generate_token(user)
            info = get_info(token)
            meta = get_meta(token)
            token = refresh_token(token)
            verified = verify_token(token)
            if verified and check_password(password, hashed):
                print('\n\tToken Info: ' + str(info[1]) + '\n')

    else:
        log('\n\tDone\n')


init()
