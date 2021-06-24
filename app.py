#! /usr/bin/env python3
from custom_modules.log import log
from custom_modules.user_data import start
from custom_modules.utils import clear
from custom_modules.jwt import generate_token, get_info, get_meta, refresh_token, verify_token


def init():
    user = start()
    if (type(user) == dict):
        clear()
        token = generate_token(user)

        log('\n\n\tHi ' + user['name'] + '\n')
        log('\tToken Verified? ' + str(verify_token(token)))
        log('\tToken Info: ' + str(get_info(token)))
        log('\tToken Meta: ' + str(get_meta(token)))
        log('\tRefreshing Token')
        refresh_token(token)
        log('\tToken Info: ' + str(get_info(token)))

    else:
        log('\n\tDone\n')


init()
