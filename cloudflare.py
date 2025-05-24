import requests
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Cloudflare:
    URL = 'https://api.cloudflare.com/client/v4/'
    COMMENT = 'Updated by DDNS-Cloudflare-API'

    def __init__(self, name, token, zone, proxy=False):
        self.name = name
        self.token = token
        self.zone = zone
        self.proxy = proxy
        self.LISTURL = f'{self.URL}zones/{self.zone}/dns_records'
    
    def getHeaders(self):
        return {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
    
    def listDNS(self):        
        response = requests.get(self.LISTURL, headers=self.getHeaders())
        response.raise_for_status()

        return response.json()

    def updateDNS(self):
        logging.info('Updating DNS records')
        listDNS = self.listDNS()
        results = listDNS['result']
        newIP = self.getIp()

        for result in results:
            if result['type'] == 'A' and result['name'] == self.name:

                if result['content'] == newIP:
                    logging.info('IP address is the same, no need to update')
                    return
                
                updateUrl = f'{self.LISTURL}/{result["id"]}'

                body = {
                    'content': newIP,
                    'type': 'A',
                    'proxied': self.proxy,
                    'name': self.name,
                    'comment': self.COMMENT
                }

                response = requests.put(updateUrl, json=body, headers=self.getHeaders())
                response.raise_for_status()

                if response.json()['success'] == True:
                    logging.info(f'Updated {self.name} to {newIP}')
                else:
                    logging.error('Failed to update DNS record')
                
                return

    def getIp(self):
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']
