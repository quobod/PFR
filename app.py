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
        verified = verify_token(token)
        info = get_info(token)
        meta = get_meta(token)
        token = refresh_token(token)

        log('\n\n\tHi ' + user['name'] + '\n')
        log('\tToken Verified? ' + str(verified))
        log('\tToken Info: ' + str(info[1]))
        log('\tToken Meta: ' + str(meta[0]))
        log('\tRefreshing Token')
        log('\nToken:\t' + str(token))

    else:
        log('\n\tDone\n')


init()
