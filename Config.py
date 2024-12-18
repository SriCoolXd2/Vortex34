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
    
    MULTI_CLIENT = True
    MULTI_TOKEN1 = "8167133424:AAFOxR8RT2yc22nkQe2ZCmBaqazLxaX5sSg"
    MULTI_TOKEN2 = "7664260315:AAELL8fl55drmINQEvtmAgnudB1rTkdedjs"
    MULTI_TOKEN3 = "8139027297:AAHYIm9sFSQmfm30lhEPHWbF0BRjZBhbCJ0"
    MULTI_TOKEN4 = "8143922346:AAEGpGzrWbKR0aQbvMtG8EdI9wbsc8Inkpo"
    MULTI_TOKEN5 = "7501383740:AAHDsqVhS7chpanRkcfrPXj4HfaMdQ4FRNM"
    MULTI_TOKEN6 = "7504914172:AAHMDa-JiNuIwyBOXYzd9zyfRYDkr2JDkBw"
    MULTI_TOKEN7 = "7247168009:AAGYeLpRTbwmzYFcATR0z15LxXwmfv7_ozA"
    MULTI_TOKEN8 = "7371830140:AAGbHG-DMLTvBxXDSeoIhUkMJ1RZi4Vnhoo"
    MULTI_TOKEN9 = "7763535690:AAFaiUfrbFXp1kcFm0rsh62TFqKg2yzoLQU"
    MULTI_TOKEN10 = "7593692462:AAEJ_mhSt35jgNdg76qTCzs4OXec4Atz9Jc"
    
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
