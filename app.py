import cloudflare as cf
import flask
import os

API_TOKEN = os.getenv('API_TOKEN')
NAME = os.getenv('NAME')
ZONE = os.getenv('ZONE')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

app = flask.Flask(__name__)
cloudflare = cf.Cloudflare(NAME, API_TOKEN, ZONE)

@app.route('/', methods=['GET'])
def main():
    # username = flask.request.args.get('username')
    # password = flask.request.args.get('password')
    ip = flask.request.args.get('ip')

    # if username != USERNAME or password != PASSWORD:
    #     return {'error': 'Invalid credentials'}

    if ip:
        return cloudflare.updateDNS(ip)
    else:
        return {'error': 'No IP provided'}
    