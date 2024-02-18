import requests
import urllib.parse
import hashlib
import hmac
import base64

class KrakenAPI:
    def __init__(self):
        self.api_key = None
        self.api_sec = None
        self.load_api_keys()

    def load_api_keys(self):

        with open('keys.txt', "r") as f:
            lines = f.read().splitlines()
            self.api_key = lines[0]
            self.api_sec = lines[1]

    def kraken_request(self,url_path, data, api_key, api_sec):

        api_url = "https://api.kraken.com"

        headers = {"API-Key": api_key, "API-Sign": self.get_kraken_signature(url_path, data, api_sec)}
        req = requests.post((api_url + url_path), headers = headers, data = data)
        return req

    def get_kraken_signature(self,urlpath, data, secret):
        postdata = urllib.parse.urlencode(data)
        encoded = (str(data['nonce']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()

        mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()

    def request(self,urlPath,data):
        resp = self.kraken_request(urlPath,
                                   data, 
                                   self.api_key, 
                                   self.api_sec)
        return resp.json()