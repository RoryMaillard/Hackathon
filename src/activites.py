import json
import os
import requests
from flask import Flask, jsonify, make_response, render_template

from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 5000))
HOST = '0.0.0.0'


@app.route("/", methods=['GET'])
def get_homepage():
    return render_template('index.html.jinja2')

@app.route("/activites", methods=['GET'])
def get_activites():
    activites = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?limit=44&apikey={os.getenv('API_KEY')}")
    res = make_response(activites.json(), 200)
    return res


@app.route("/activites/<activite>", methods=['GET'])
def get_activites_filter(activite):

    encoded_activite = quote(activite)
    activites = requests.get(f"https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_agenda-animations-culturelles-bibliotheque-municipale-nantes/records?limit=44&where=nom%3D%20%22{encoded_activite}%22&apikey={os.getenv('API_KEY')}")
    res = make_response(activites.json(), 200)
    return res

if __name__ == "__main__":
    print("Server running in port %s" % PORT)
    app.run(host=HOST, port=PORT)
