import os
from os import getenv, environ
from dotenv import load_dotenv

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

class Var(object):
    # Bot Information
    API_ID = int(getenv('API_ID', '21879629'))
    API_HASH = str(getenv('API_HASH', 'dcb6bfd6d51a8ff5f6aadb01b9fdd11b'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6858868230:AAHnIIjfFIpIs5Y4TeACU7K6uO2oA7zj-pw'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))

    #Channel Information
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002124078334'))
    LOG_CHANNEL = int(getenv('LOG_CHANNEL', '-1002124078334'))
    
    # Users Information
    OWNER_ID = int(os.environ.get("OWNER_ID", "5591007272"))
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "6675573927 1001581247 1303394531 607305878 854128672 5514721611 1110489315 1487388920 1092476790 5329521369 1356815354").split()]
    MULTI_CLIENT = True
 
    # Server Information
    PORT = int(getenv('PORT', '8080'))
    NO_PORT = bool(getenv('NO_PORT', False))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '195.154.182.71'))
    IF_DM = True
    FQDN = getenv('FQDN', '195.154.182.71:8080') if IF_DM else getenv('BIND_ADDRESS', '195.154.182.71:8080')
    HAS_SSL = bool(getenv('HAS_SSL', 'False'))
    if HAS_SSL:
        URL = "http://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
