import json
import os
import requests
from flask import Flask, jsonify, make_response

from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

PORT = 5000
HOST = 'localhost'


@app.route("/activites", methods=['GET'])
def get_activites():
    activites = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?limit=44&apikey={os.getenv('API_KEY')}")
    res = make_response(activites.json(), 200)
    return res


@app.route("/activites/<activite>", methods=['GET'])
def get_activites_filter(activite):
    print(activite)
    print(type(activite))
    encoded_activite = quote(activite)
    print(encoded_activite)
    URL = f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?limit=44&where=nom%3D%20%22{encoded_activite}%22&apikey={os.getenv('API_KEY')}"
    activites = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?limit=44&where=nom%3D%20%22{encoded_activite}%22&apikey={os.getenv('API_KEY')}")
    res = make_response(activites.json(), 200)
    print(URL)
    return res

if __name__ == "__main__":
    print("Server running in port %s" % PORT)
    app.run(host=HOST, port=PORT)