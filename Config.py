import os
from os import getenv, environ
from dotenv import load_dotenv

class Var(object):
    # Bot Information
    API_ID = int(getenv('API_ID', '21821499'))
    API_HASH = str(getenv('API_HASH', '31eda964c848701b76931b1a5446f301'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '7631945627:AAH6N63eYDSjCf_-lR6lSMEiBoYURQPBnDg'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))

    #Channel Information
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002464183743'))
    LOG_CHANNEL = int(getenv('LOG_CHANNEL', '-1002464183743'))
    
    # Users Information
    OWNER_ID = int(os.environ.get("OWNER_ID", "7158245271"))
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "7158245271").split()]
    
    MULTI_CLIENT = False
    MULTI_TOKEN1 = ""
    MULTI_TOKEN2 = ""
    MULTI_TOKEN3 = ""
    MULTI_TOKEN4 = ""
    MULTI_TOKEN5 = ""
    MULTI_TOKEN6 = ""
    MULTI_TOKEN7 = ""
    MULTI_TOKEN8 = ""
    MULTI_TOKEN9 = ""
    MULTI_TOKEN10 = ""
    
    # Server Information
    PORT = int(getenv('PORT', '8080'))
    NO_PORT = bool(getenv('NO_PORT', False))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    IF_DM = True
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(environ.get('APP_NAME', 'vortexstreambot-80bf2539e62a'))
    else:
        ON_HEROKU = False
    FQDN = (str(environ.get('FQDN', f'{BIND_ADDRESS}:{PORT}')) if not ON_HEROKU or environ.get('FQDN', '') else f"{APP_NAME}.herokuapp.com")
    HAS_SSL = bool(getenv('HAS_SSL', 'False'))
    if HAS_SSL:
        URL = "http://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
