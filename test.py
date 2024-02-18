import time
from api.api import *

api = KrakenAPI()
print(api.request("/0/private/Balance",
                      {"nonce": str(int(1000 * time.time()))}
                      ))