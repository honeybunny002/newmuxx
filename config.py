
import os

class Config:

    BOT_TOKEN = '5853151932:AAF9KzjwTU-l_FeJ0lHOXobTKzuD9R495jg'
    APP_ID = '6025826'
    API_HASH = 'aa30aef34398fb638500d18e514447f1'
    USERS = '1226841901, 1671626669, 866649963, 5160169373, 1958851206, 778988294, 947859478, 1157557110, 1772988300, 2135072465, 1363236962, 956022686, 5443081541'
    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in USERS.split(',')]

    DOWNLOAD_DIR = 'downloads'
