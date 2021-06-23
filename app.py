#! /usr/bin/env python3
from custom_modules.log import log
from custom_modules.user_data import start
from custom_modules.utils import clear


def init():
    user = start()
    if (type(user) == dict):
        clear()
        log('\n\n\tHi ' + user['name'] + '\n\n')
    else:
        log('\n\tDone\n')


init()
