
import os

class Config:

    BOT_TOKEN = '5816246888:AAFlxo_PL-2Ea-rwlYRz5Nb8mWtyr64EgbM'
    APP_ID = '5080899'
    API_HASH = '6fc7f813cf96e6692990b752b43fd9c7'

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1098504493').split(',')]

    DOWNLOAD_DIR = 'downloads'
