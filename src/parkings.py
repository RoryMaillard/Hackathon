import os
import flask
import requests

from flask import Flask, make_response
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('API_KEY'))

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))
HOST = '0.0.0.0'


@app.route("/", methods=['GET'])
def get_homepage():
    return flask.render_template('index.html.jinja2')

@app.route("/parkings", methods=['GET'])
def get_parkings():
    parkings = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_parkings-publics-nantes-disponibilites/records?apikey={os.getenv('API_KEY')}")
    res = make_response(parkings.json(), 200)
    return res

if __name__ == "__main__":
    print("Server running in port %s" % port)
    app.run(host=HOST, port=port)