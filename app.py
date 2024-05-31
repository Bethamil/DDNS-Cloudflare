import cloudflare as cf
import os

API_TOKEN = os.getenv('API_TOKEN')
NAME = os.getenv('NAME')
ZONE = os.getenv('ZONE')

if API_TOKEN and NAME and ZONE:
  cloudflare = cf.Cloudflare(NAME, API_TOKEN, ZONE)
  cloudflare.updateDNS()
else:
  raise ValueError('API_TOKEN, NAME, ZONE must be set as environment variables')