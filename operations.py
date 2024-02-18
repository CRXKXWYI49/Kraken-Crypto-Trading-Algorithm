import time
from api.api import *


def get_balance():
    api = KrakenAPI()
    return(api.request("/0/private/Balance",
                    {"nonce": str(int(1000 * time.time()))}
                    )['result'])